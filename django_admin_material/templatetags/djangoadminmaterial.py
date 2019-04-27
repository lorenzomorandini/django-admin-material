import re
from django import template
register = template.Library()

@register.filter(name='div')
def div(value, arg):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = int( value )
        arg = int( arg )
        if arg: return int(value / arg)
    except: pass
    return ''

@register.filter(name='clean_material_tab')
def clean_material_tab(value):
    import pdb; pdb.set_trace()
    lol = re.search('material-tab-', value).group(1)
    return lol