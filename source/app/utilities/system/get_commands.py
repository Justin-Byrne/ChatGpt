import os

from .parse_commands 			import parse_commands

ERROR = -1

def get_commands   ( commands ):

	arguments = parse_commands ( commands )

	return arguments
