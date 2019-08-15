from django.apps import apps
from django.contrib import admin
from django.utils.module_loading import import_string

from mptt.admin import DraggableMPTTAdmin


__all__ = (
    'get_admin_base_class',
    'get_admin_inline_base_class',
)


def get_admin_base_class() -> admin.ModelAdmin:
    """
        Return base admin parent class
        translatable or not.
    """
    if apps.is_installed('modeltranslation'):
        class TranslatableTreeAdmin(
            DraggableMPTTAdmin, 
            import_string('modeltranslation.admin.TranslationAdmin')
        ):
            pass

        return TranslatableTreeAdmin
    return DraggableMPTTAdmin


def get_admin_inline_base_class():
    """
        Return base admin inline class
        translatable or not.
    """
    if apps.is_installed('modeltranslation'):
        return import_string('modeltranslation.admin.TranslationStackedInline')
    return admin.StackedInline
