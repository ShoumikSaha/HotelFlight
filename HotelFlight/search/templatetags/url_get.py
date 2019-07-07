from django import template

register = template.Library()


@register.simple_tag(name='url_get')
def active_request_get(request, key):
    getcopy = request.GET.copy()
    if getcopy.__contains__(key):
        print(getcopy.get(key, default=None))
        return getcopy.get(key, default=None)
    return ''
