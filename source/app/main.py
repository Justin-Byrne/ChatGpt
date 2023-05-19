import sys

from utilities.util     import Util

ERROR = -1

def view_arguments ( arguments ):

	print ( '-' * 4, '[ Arguments ]', '-' * 41 )

	for argument in arguments:

		print ( f'{argument}: ', arguments [ argument ] )

	print ( '-' * 60 )


def main ( commands ):

	arguments = Util.get_commands ( commands )


	if arguments != ERROR:

		view_arguments ( arguments ) 	### TEMPORARY ###

		if Util.get_models ( arguments ):

			Util.get_completion ( arguments )

		else:

			Util.output ( 'main', 'Could not obtain open AI models !' )


main ( sys.argv )
