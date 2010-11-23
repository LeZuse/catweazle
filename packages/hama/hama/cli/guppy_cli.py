"""
# TODO write guppy docstring!
"""

import sys

from hama.utilities.clioptions import parse_arguments
from hama.guppy import guppy

VERSION = '0.1'

def guppy_cli():
    '''\
    Entry point for :ref:`guppy <cli_guppy>`
        
    .. todo::
       Write ``guppy_cli`` docstring
        '''
    
    cli_options = {
        'description': '''Guppy gets resources for given codes''',
        
        'usage': '\n'.join(['', '%prog [-m -a -t -c] codes', '%prog -v']), 
        
        'options': [
            [   '-v', 
                '--version', 
                {   'dest': 'version', 
                    'help': 'prints the version', 
                    'default': False, 
                    'action': "store_true"
                    }
                ],
                
            [   '-m', 
                '--get_images', 
                {   'dest': 'get_images', 
                    'help': 'downloads images',
                    'default': False, 
                    'action': "store_true"                    
                    }
                ],
                
            [   '-c', 
                '--get-packshots', 
                {   'dest': 'get_packshots', 
                    'help': 'gets packshot images',
                    'default': False, 
                    'action': "store_true"                    
                    }
                ],                

            [   '-a', 
                '--get-packaging-artwork', 
                {   'dest': 'get_packaging_artwork', 
                    'help': 'downloads all PDF files',
                    'default': False, 
                    'action': "store_true"                    
                    }
                ],
                
            [   '-t', 
                '--get-product-text', 
                {   'dest': 'get_product_text', 
                    'help': 'gets the description from hama.de',
                    'default': False, 
                    'action': "store_true"                    
                    }
                ]                 

            ]
        }    
    
    parser = parse_arguments(cli_options)
    (options, args) = parser.parse_args()   
    
    if options.version:
        print VERSION
        sys.exit(0)
    
    if len(args) == 0:
        parser.print_help()
        sys.exit(0)
    
    options = eval(str(options))
    options = [i for i in options if options[i] == True]
    guppy(options=options, args=args)
    
    