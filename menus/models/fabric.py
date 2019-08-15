from typing import Dict, List, Iterator

from django.utils.module_loading import import_string
from django.utils.translation import ugettext_lazy as _

from .models import MenuItem


__all__ = ("ModelFabric", )


class ConfigError(ValueError):
    pass


class ModelFabric:

    def __init__(self, variations: List, base_menu: str=None):
        """
            variations: [{
                "label": "some label", - not required
                "label_plural": "some plural label", - not required
                "position": "position", - required
            }, ...]
            base_menu: str path to custom base menu model
        """
        if base_menu:
            try:
                self.base_menu = import_string(base_menu)
            except Exception as e:
                raise ConfigError(
                    f"Field `base_menu` contain invalid path: `{e}`"
                )
        else:
            self.base_menu = MenuItem
        
        self.variations = variations

    def validate_variation(self, variation: Dict):
        """Validate inputted variation data."""
        if 'position' not in variation:
            raise ConfigError(
                "Field `position` does`t exists in variation`s configs"
            )

    def generate_klass_name(self, position: str):
        return f"{position.capitalize()}Item"

    def model_init(self, position: str, label: str=None, label_plural: str=None, **kwargs):
        """Generate model."""
        if not label:
            label = position.capitalize()
        if not label_plural:
            label_plural = label.capitalize()

        klass_name = self.generate_klass_name(position)

        class Meta:
            proxy = True
            verbose_name = label
            verbose_name_plural = label_plural

        klass = type(
            klass_name,
            (self.base_menu, ),
            {
                "__module__": "menus.models",
                "_position": position,
                "_config": kwargs,
                "Meta": Meta
            }
        )                

        return klass, klass_name

    def model_iteration(self) -> Iterator:
        """Dynamic menu models iterator."""
        for variation in self.variations:
            self.validate_variation(variation)
            klass, klass_name = self.model_init(**variation)
            yield klass_name, klass
