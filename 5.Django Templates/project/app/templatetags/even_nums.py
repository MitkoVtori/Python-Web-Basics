from django import template

register = template.Library()


@register.filter(name="even")
def even_nums(nums: list):
    ''' Filter the even nums in a list of numbers '''
    return [x for x in nums if x % 2 == 0]

