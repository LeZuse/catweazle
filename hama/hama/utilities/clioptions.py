from optparse import OptionParser

def parse_arguments(cli_options):
	'''
	.. todo:: upgrade to ``argparse``
	
	.. todo:: write parse_arguments docstring
	
	'''
	description = cli_options['description']
	parser = OptionParser(description=description)
	parser.usage = cli_options['usage']
	
	for option in cli_options['options']:
	    parser.add_option(option[0], option[1], **option[2])
	
	
	return parser