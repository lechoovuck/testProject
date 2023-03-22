from django import template

register = template.Library()


@register.simple_tag
def url_link(value, field_name, url_encode=None):
    url = f'{field_name}={value}'

    if url_encode:
        querystring = url_encode.split('&')
        filtered_querystring = filter(lambda x: x.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = f'{url}&{encoded_querystring}'

    return f'?{url}'
