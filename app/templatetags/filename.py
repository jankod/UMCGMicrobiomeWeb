import os
from builtins import type

from django import template
from django.forms import FileField

register = template.Library()


@register.filter
def filename(value: FileField):
    """ Show only filename of uploaded files"""
    #print(type(value))
    return os.path.basename(value.file.name)
