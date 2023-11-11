from django import template

register = template.Library()


@register.filter
def ext_getfields(obj):
    return [(field.name, field.value_to_string(obj)) for field in obj._meta.fields]


@register.filter
def ext_getkeys(obj):
    return [field.name for field in obj._meta.fields]


@register.filter
def ext_getstrvalues(obj):
    return [field.value_to_string(obj) for field in obj._meta.fields]

@register.filter
def ext_getvalues(obj):
    return [field.value(obj) for field in obj._meta.fields]

@register.filter
def ext_removeempty(lst):
    return [val for val in lst if val]

