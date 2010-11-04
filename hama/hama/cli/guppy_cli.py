import sys

from hama.utilities.clioptions import parse_arguments
from hama.guppy import guppy

def guppy_cli():
    '''\
    Entry point for :ref:`guppy <cli_guppy>`
        
    .. todo::
       Write ``guppy_cli`` docstring
        '''
    VERSION = '0.1'
    
    cli_options = {
        'description': ''' d ''',
        
        'usage': '\n'.join(['', '%prog "text"', '%prog -v']), 
        
        'options': [
            [   '-v', 
                '--version', 
                {   'dest': 'version', 
                    'help': 'prints the version', 
                    'default': False, 
                    'action': "store_true"
                    }
                ],
                
            [   '-d', 
                '--additional-dictionary', 
                {   'dest': 'additional_dictionary', 
                    'help': 'list of custom-capitalised words'
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
    
    
    
    return 'guppy'