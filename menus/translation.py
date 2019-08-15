from modeltranslation.translator import translator, TranslationOptions

from .models.models import MenuItem
from .models import custom_menus


class BaseMenuTranslationOptions(TranslationOptions):
    fields = (
        'title', 
        'link', 
    )

class CustomFakeTranslationOptions(TranslationOptions):
    fields = ()


translator.register(MenuItem, BaseMenuTranslationOptions)
for menu in custom_menus:
    translator.register(menu, CustomFakeTranslationOptions)
