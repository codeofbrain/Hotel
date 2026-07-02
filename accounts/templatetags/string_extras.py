
from django import template

register = template.Library()

@register.filter()
def split_username(value,ind):
    ind = int(ind)
    if '_' in value:
        return value.split('_')[ind]
    return value





@register.filter(name='get_item')
def get_item(dictionary,key):
    return dictionary.get(key)

@register.filter()
def nums_comments(comments):
    return len(comments)