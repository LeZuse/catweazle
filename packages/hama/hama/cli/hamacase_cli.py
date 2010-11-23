"""
# TODO write hama_case_cli docstring!
"""

import sys
import os
import re

from hama.textutils import hama_case
from hama.utilities.clioptions import parse_arguments

VERSION = '0.1'
DESCRIPTION =  '''Convert text to Title-case. 
Honour grammar rules and apply correct case to all words 
defined in the dictionary'''

def hama_case_cli():
    '''Entry point for :ref:`hama-case <cli_hama-case>` console command.
    
    .. todo:: Implement filter functionality ($ echo nimh | hama-case => 'NiMH')
    .. todo:: Format for `more_capitalisation` file is too strict. Allow also line ends (at least)
    .. todo:: `more_capitalisation` list doesn't allow group of words
    
    '''
    
    cli_options = {
        'description': DESCRIPTION,
        
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


    text = ' '.join(args)
    
    # determine additional custom capitalised words
    if options.additional_dictionary:
        try:
            additional_dictionary = (options.additional_dictionary)
            additional_dictionary = os.path.expanduser(additional_dictionary)
            with open(additional_dictionary) as more_capitalisation:
                # if -d option is a path to readable file
                additional_words = more_capitalisation.read()
                additional_dictionary = re.split(r'\s+', additional_words)
        
        except IOError:
            # if -d option is a list of custom-capitalised words
            additional_dictionary = options.additional_dictionary.split(' ')
    else:
        # if -d option not given
        additional_dictionary = []


    # With everything prepared, we are ready to run. 
    # Calling hama.textutils.hama_case
    print hama_case(text, custom_capitalisation=additional_dictionary)
    sys.exit(0)
