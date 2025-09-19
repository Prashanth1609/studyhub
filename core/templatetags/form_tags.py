from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(field, css):
    """
    Add a CSS class to a form field.
    Usage: {{ form.field_name|addclass:"form-control" }}
    """
    return field.as_widget(attrs={"class": css})
