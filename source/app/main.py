import sys

from utilities.util     import Util

ERROR = -1

def main ( commands ):

	arguments = Util.get_commands ( commands )


	if arguments != ERROR:

		list_models = Util.openai_connect ( arguments [ 'org' ], arguments [ 'key' ] )

		if list_models != ERROR:

			list = Util.get_list_models ( list_models )


			print ( 'list:', list )

main ( sys.argv )
