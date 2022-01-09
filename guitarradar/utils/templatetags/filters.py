from django.template.defaulttags import register


@register.filter(name='range')
def _range(times: int):
    return range(times)


@register.filter(name='range_til_five')
def _range_til_five(times: int):
    return range(times, 5)
