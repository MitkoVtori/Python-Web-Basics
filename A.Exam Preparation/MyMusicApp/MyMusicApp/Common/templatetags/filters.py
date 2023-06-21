from django import template


register = template.Library()


@register.filter(name="decimal")
def second_decimal(value):
    return f"{value:.2f}"

