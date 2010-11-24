"""TODO docstring"""
# -*- coding: utf-8 -*-

import re

from titlecase import titlecase
from hama.textutils.capitalisation import CAPITALISATION_DICTIONARY

def hama_case(text, custom_capitalisation=[]):
    '''
    .. todo:: hama_case docstring
    .. todo:: doesn't work properly with numbers followed by unit (55mah e&.)
    .. todo:: forces dictionary capitalisation even at the start of a sentence
    .. todo:: write tests
    
    >>> from hama.textutils import hama_case
    >>> hama_case('usb hub 1:4, silver, bus powered')
    'USB Hub 1:4, Silver, Bus Powered'
    >>> hama_case('xxl stylus pen for nintendo dsi xl')
    'XXL Stylus Pen for Nintendo DSi XL'
    >>> hama_case('but not tonight')
    'But not Tonight'
    '''
    additional_dictionary = {}
    text = titlecase(text.lower())
    
    for word in custom_capitalisation:
        additional_dictionary[word.capitalize()] = word 
    
    CAPITALISATION_DICTIONARY.update(additional_dictionary)
    
    for key, value in CAPITALISATION_DICTIONARY.iteritems():
        pattern = re.compile(r'\b%s\b' % key, re.IGNORECASE)
        text = pattern.sub(value, text)
        text = text[0].capitalize() + text[1:]

    return text
