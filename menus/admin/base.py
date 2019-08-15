from django.contrib import admin
from django.conf import settings

from ..models import custom_menus
from .utils import get_admin_base_class, get_admin_inline_base_class


class BaseMenuAdmin(get_admin_base_class()):
    """Base menu admin model."""
    exclude = ('position', 'parent')
    list_display = (
        'tree_actions', 
        'indented_title', 
        'title', 
        'link', 
    )
    list_editable = (
        'title', 
        'link', 
    )


for menu in custom_menus:
    kwargs = {}
    if menu._config and menu._config.get('is_nested', False):
        class BaseMenuInline(get_admin_inline_base_class()):
            exclude = ('position', )
            model = menu
            fk_field = 'parent'
            extra = 0
        kwargs['inlines'] = (BaseMenuInline, )
    admin.site.register(menu, BaseMenuAdmin, **kwargs)
