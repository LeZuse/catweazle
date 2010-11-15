import sys
import os
import re

from hama.textutils import hama_case
from hama.utilities.clioptions import parse_arguments

def hama_case_cli():
    '''
    Entry point for :ref:`hama-case <cli_hama-case>` console command.
    
    .. todo:: Implement filter functionality ($ echo nimh | hama-case => 'NiMH')
    .. todo:: Format for `more_capitalisation` file is too strict. Allow also line ends (at least)
    .. todo:: `more_capitalisation` list doesn't allow group of words
    
    '''
    
    VERSION = '0.1'
    
    cli_options = {
        'description': '''Converts any text to Title-case. It honours grammar rules and applies correct case to all words defined in the dictionary''',
        
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

# Parsing cli arguments to determine what the `text` 
# & `additional_dictionary` are. If asked to print version 
# or given no arguments, the script will exit here, printing
# either the version or short help with the usage example.
    
    parser = parse_arguments(cli_options)
    (options, args) = parser.parse_args()

    if options.version:
        print VERSION
        sys.exit(0)
    
    if len(args) == 0:
        parser.print_help()
        sys.exit(0)

    if options.additional_dictionary:
        try:
        	with open(os.path.expanduser(options.additional_dictionary)) as more_capitalisation:
        		# -d option is a path to readable file
        		additional_dictionary = re.split(r'\s+', more_capitalisation.read())
        
        except IOError:
        	# -d option is a list of custom-capitalised words
            additional_dictionary = options.additional_dictionary.split(' ')
    else:
    	# -d option not given
		additional_dictionary = []

    text = ' '.join(args)



# With everything prepared, we are ready to run. Calling hama.textutils.hama_case
        
    print hama_case(text, custom_capitalisation=additional_dictionary)
    sys.exit(0)
