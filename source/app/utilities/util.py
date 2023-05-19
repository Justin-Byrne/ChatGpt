# SYSTEM
from .system.validation.is_directory 	import is_directory
from .system.validation.is_file      	import is_file
from .system.get_commands 			 	import get_commands
from .system.debug.output 				import output

# CUSTOM
from .custom.connect.openai_certify 	import openai_certify
from .custom.model.get_models			import get_models
from .custom.prompt.get_completion 		import get_completion

class Util:

	def __init__ (  ): pass

	#### 	SYSTEM 	########################################

	# VALIDATION

	def is_directory   ( path ) 				  			: return is_directory   ( path )

	def is_file 	   ( path,   type = None ) 				: return is_file        ( path, type )

	# DEBUG

	def output 		   ( source, message, type = 'ERROR' )	: return output 		( source, message, type )

	# GENERAL

	def get_commands   ( commands ) 		 	  			: return get_commands   ( commands )

	#### 	CUSTOM 	########################################

	# CONNECT

	def openai_certify ( API_ORG, API_KEY ) 				: return openai_certify ( API_ORG, API_KEY )

	# MODEL

	def get_models     ( arguments )                 		: return get_models     ( arguments )

	# PROMPT

	def get_completion ( arguments )						: return get_completion ( arguments )
