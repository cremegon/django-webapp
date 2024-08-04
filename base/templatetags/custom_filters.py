from django import template

register = template.Library()

@register.filter
def truncate_words(val, num_words):
    words = val.split()
    if len(words) > num_words:
        return "".join(words[:num_words]) + ...
    return val
