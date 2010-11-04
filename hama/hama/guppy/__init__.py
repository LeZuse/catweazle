'''
..todo: write hama.guppy docstring
'''

import os

from hama.jimbo import determine_supplier
from get_images import main as get_images
from get_packshots import main as get_packshots
from get_packaging_artwork import main as get_packaging_artwork
from get_product_text import main as get_product_text

def guppy(options, args):
    '''
    ..todo: write guppy docstring (hama.guppy.guppy)
    '''
    
    CWD = os.getcwd()
    codes = determine_supplier(args)
    
    for i in options:
        os.mkdir(i)
    
    
    resources = {
        'get_packaging_artwork': get_packaging_artwork,
        'get_images': get_images,
        'get_product_text': get_product_text,
        'get_packshots': get_packshots 
    
    }
    
    
    for code in codes:
        for request in options:
            data = resources[request](code[2])
            
            with open('%s/%s/%s' % (CWD, request, code[0]), 'w') as output:
                output.write(data)
            
    
    
    
