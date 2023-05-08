import os
import openai
import sys

from utilities.util     import Util
# from core.generator     import Generator
# from core.linker 		import Linker

# OPEN_API_KEY = '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'
# OPEN_API_KEY = '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'
# OPEN_API_ORG = 'org-Ro4HHf3ig7IQFG69E0JXwid9'

ERROR = -1

def main ( commands ):

	# print ( commands )

	arguments = Util.get_commands ( commands )


	print ( arguments )



	# openai.organization = OPEN_API_ORG

	# openai.api_key 		= OPEN_API_KEY

	# openai_list 		= openai.Model.list ( )

	# print ( openai_list )


main ( sys.argv )


# arguments = Util.get_commands ( commands )


# 	if arguments != ERROR:

# 		if Generator ( arguments ) and arguments [ 'link_files' ]:

# 			Linker ( arguments )
#
