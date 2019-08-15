from django.template import Library
from ..models import MenuItem


__all__ = ('get_menus', )


register = Library()


@register.simple_tag
def get_menus(position: str) -> 'models.QuerySet':
    """Return queryset of menu items getting by position."""
    return MenuItem.objects.get_by_position(position)
