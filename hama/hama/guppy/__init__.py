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
    
#     for i in options:
#         os.mkdir(i)
    
    
    resources = {
        'get_packaging_artwork': get_packaging_artwork,
        'get_images': get_images,
        'get_product_text': get_product_text,
        'get_packshots': get_packshots 
    
    }
    
    
    for code in codes:
        for request in options:
            supplier = code[1]
            supplier_code = code[2]
            resource_request_handler = resources[request]
            
            resource_data = resource_request_handler(supplier_code, supplier)
            
            output_file = '%s/%s/%s%s.%s' % (CWD, request, code[0], resource_data.name, resource_data.format)
            
            with open(output_file, 'w') as output:
                if request == 'get_product_text':
                    product_description_template = '%s\n%s\n%s\n%s\n%s'
                    product_description = (
                        resource_data.data.code,
                        resource_data.data.link,
                        resource_data.data.name,
                        resource_data.data.remark,
                        resource_data.data.description)
                    
                    output.write(product_description_template % product_description)
                else:
                    output.write(data.data)
            
    
    
    
