import json

from .parse_list_models 	import parse_list_models
from .file.write_file 		import write_file

def get_list_models ( list ):

	dictionary = parse_list_models ( list )


	if dictionary:

		write_file ( 'models', dictionary, True )
