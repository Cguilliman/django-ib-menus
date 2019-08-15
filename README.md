# django-ib-menus

This app allows you to generate tree view menus dynamically.

## Installation

install with pip:

```shell
pip install django-ib-menus
```

If you want to make menu models translatable, you need to install [django-modeltranslation](https://github.com/deschler/django-modeltranslation) package. For create new fields in menu model for each language:

```shell
python manage.py makemigrations
python manage.py migrate
```

Update INSTALL_APPS:

```python
INSTALLED_APPS = [
	...
	"menus",
	"modeltranslation",  # optional
	"django_jinja",  # optional for jinja2 global function
	...
]
```

## Configuration

`MENU_SETTINGS` - Dict of configurations. Where:
- `base_menu`: path to base menu item model implementation (not required).
- `variations`: list of dicts with menu type configuration fields.
	- `label`: string, model admin label.
	- `label_plural`: string, model admin label plural.
	- `position`: string, model type name.
	- `is_nested`: bool, is tree view menu types.

```python
MENU_SETTINGS = {
    'variations': [
        {
            'label': 'Header', 
            'label_plural': 'Headers', 
            'position': 'header', 
            'is_nested': True,
        }
    ]
}
```

Make migrations:

```shell
python manage.py makemigrations
python manage.py migrate
```

## Basic example to use

Django queryset:

```python
...
from menus.models import MenuItem
...

...
qs = MenuItem.objects.get_by_position('header')
...
```

*.html:

```html
{% load menus %}
{% get_menus "header" as menus %}
<ol>
    {% for menu in menus %}
        <li><p>{{ menu }}</p></li>
    {% endfor %}
</ol>
```

*.jinja:

```html
<ol>
    {% for menu in get_jinja_menus("header") %}
        <li><p>{{ menu }}</p></li>
    {% endfor %}
</ol>
```
