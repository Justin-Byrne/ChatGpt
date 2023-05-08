import os
import openai
import sys

# from utilities.util     import Util
# from core.generator     import Generator
# from core.linker 		import Linker

OPEN_API_KEY = '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'

OPEN_API_ORG = 'org-Ro4HHf3ig7IQFG69E0JXwid9'

ERROR = -1

def main ( commands ):

	openai.organization = OPEN_API_ORG

	# openai.api_key 		= os.getenv ( OPEN_API_KEY )
	openai.api_key 		= OPEN_API_KEY

	openai_list = openai.Model.list ( )

	print ( openai_list )


main ( sys.argv )
