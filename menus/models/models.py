from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey

from .queysets import BaseMenuManager


__all__ = ("MenuItem")


if hasattr(settings, "MENU_SETTINGS"):
    variations = settings.MENU_SETTINGS.get("variations", None)
else:
    variations = None


def get_position(variations):
    if variations:
        return [
            (variation.get("position"), variation.get("label")) 
            for variation in variations
        ]
    return []


class MenuItem(MPTTModel):
    """
        Base menu item model

        title(CharField): Menu title.
        link(CharField): Menu link.
        position(CharField): Menu position.
        parent(TreeForeignKey): Menu parent (MPTTModel tree implementation).
    """
    _position = None
    _config = None

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255
    )
    link = models.CharField(
        verbose_name=_("Link"),
        max_length=255
    )
    position = models.CharField(
        verbose_name=_("Position"),
        max_length=255,
        choices=get_position(variations),
    )
    parent = TreeForeignKey(
        "self",
        verbose_name=_("Parent item"),
        related_name="subitem",
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    objects = BaseMenuManager()

    class Meta:
        verbose_name = _("Menu item")
        verbose_name_plural = _("Menu items")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.position = (
            self._position 
            if self._position else None
        )
        super().save(*args, **kwargs)
