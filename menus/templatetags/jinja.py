from django.apps import apps

from ..models import MenuItem

__all__ = (
    'get_jinja_menus',
)


if apps.is_installed('django_jinja'):
    from django_jinja import library
    import jinja2

    @library.global_function
    def get_jinja_menus(position: str) -> 'models.QuerySet':
        """Return queryset of menu item by position"""
        return MenuItem.objects.get_by_position(position)
