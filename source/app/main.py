import sys

from utilities.util     import Util

ERROR = -1

def main ( commands ):

	arguments = Util.get_commands ( commands )


	if arguments != ERROR:

		model_list = Util.openai_connect ( arguments [ 'org' ], arguments [ 'key' ] )

		if model_list != ERROR:

			print ( model_list )


main ( sys.argv )
