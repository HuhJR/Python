# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:48:28 2024

@author: KITCOOP

1) __init__.py
2) custom tag 수정 후에 server reset 해야함
3) html에 연결 tag 추가 {% load board_tags %}

"""

from django import template

register = template.Library()

@register.filter # {{start|nextpage:bottomLine}}
def nextpage(startpage, bottomLine): 
    return startpage+bottomLine

@register.filter # {{start|prepage:bottomLine}}
def prepage(startpage, bottomLine):
    return startpage-bottomLine

@register.simple_tag
def addtags(value1, value2) : #{% addtags value1 value2 %}
    return value1 + value2

@register.simple_tag
def minustags(value1, value2) : #{% minustags value1 value2 %}
    return value1 - value2
