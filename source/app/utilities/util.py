# SYSTEM
from .system.validation.is_directory 	import is_directory
from .system.validation.is_file      	import is_file
from .system.validation.is_flag      	import is_flag
from .system.get_command_type       	import get_command_type
from .system.get_commands 			 	import get_commands

# CUSTOM
from .custom.connect.openai_certify		import openai_certify
from .custom.get_models					import get_models

class Util:

	def __init__ (  ): pass

	#### 	SYSTEM 	########################################

	# VALIDATION

	def is_directory 	 ( path ) 				  			: return is_directory     ( path )

	def is_file 	     ( path,   type = None ) 			: return is_file          ( path, type )

	def is_flag          ( string, flag = '-'  )  			: return is_flag 	      ( string, flag )

	# GENERAL

	def get_command_type ( command  ) 		 	  			: return get_command_type ( command  )

	def get_commands     ( commands ) 		 	  			: return get_commands     ( commands )

	# FILE

	def get_file_info	 ( file )							: return get_file_info 	  ( file )

	#### 	CUSTOM 	########################################

	# CONNECT

	def openai_certify   ( API_ORG, API_KEY ) 				: return openai_certify   ( API_ORG, API_KEY )

	# GENERAL

	def get_models       ( arguments )                 		: return get_models       ( arguments )

	# def get_model        ( arguments )                 		: return get_model        ( arguments )
