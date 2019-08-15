from django.conf import settings

from .models import MenuItem
from .fabric import ModelFabric


custom_menus = []
if hasattr(settings, 'MENU_SETTINGS'):
    menus_iterator = ModelFabric(**settings.MENU_SETTINGS).model_iteration()

    for menu_name, menu in menus_iterator:
        vars()[menu_name] = menu
        custom_menus.append(menu)
