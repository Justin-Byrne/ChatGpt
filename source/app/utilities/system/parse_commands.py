import re
import os

from os.path 					import dirname, abspath, expanduser

from .list.list_to_string 		import list_to_string
from .get_command_type 			import get_command_type
from .validation.is_program 	import is_program

def parse_commands ( commands ):

	#### 	GLOBALS 	####################################

	arguments = {
		'org': None,
		'key': None
	}

	keys = {
		'org': 'org-',
		'key': 'sk-'
	}

	lengths = {
		'org': 28,
		'key': 48
	}

	regexes = {
		'org': r'\s*-o\s*|\s*--org\s*',
		'key': r'\s*-k\s*|\s*--key\s*'
	}

	#### 	FUNCTIONS 	####################################

	def check_command_line ( ):

		for i in range ( 1, len ( commands ) ):

			command = commands [ i ]


			for regex in regexes:

				if ( re.search ( regexes [ regex ], command ) ):

					if arguments [ regex ] == None:

						value  = commands [ i + 1 ]

						length = len ( value )


						match regex:

							case 'org':

								if value[:4] == keys [ regex ] and length == lengths [ regex ]:

									arguments [ regex ] = value


								if length == 24 and re.search ( rf'\w{{{length}}}', value ):

									arguments [ regex ] = f'org-{value}'

								else:

									print ( 'parse_commands.py: org key needs to be at least 24 characters long !' )


							case 'key':

								if value[:3] == keys [ regex ] and length == lengths [ regex ]:

									arguments [ regex ] = value


								if length == 48 and re.search ( rf'\w{{{length}}}', value ):

									arguments [ regex ] = f'sk-{value}'

								else:

									print ( 'parse_commands.py: secret key needs to be at least 48 characters long !' )

	def check_config_file  ( ):

		config_regex = {
			'org': r'OPEN\s*API\s*ORG',
			'key': r'OPEN\s*API\s*KEY'
		}

		for regex in config_regex:

			if arguments [ regex ] == None:

				list    = [ ]

				lines   = open ( './config/config.txt', 'r' ).readlines ( )

				capture = False


				for line in lines:

					if re.search ( config_regex [ regex ], line ):

						capture = True

						continue


					if capture:

						if line [ 0 ] in [ '\n', '\r\n', '#' ]: continue

						else: list.append ( line.replace ( '\n', '' ) )


					if len ( list ) > 0:

						arguments.update ( { regex: list } )

						break


	check_command_line ( )

	check_config_file  ( )


	return arguments
