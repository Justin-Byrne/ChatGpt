import os
import re
import datetime

ERROR = -1

def is_cached_file_old ( file ):

	#### 	GLOBALS 	####################################

	FILE   = f"{os.getcwd ( ).split ( 'utilities', 1 ) [ 0 ]}/cache/{file}"

	CONFIG = f"{os.getcwd ( ).split ( 'utilities', 1 ) [ 0 ]}/config/config.txt"

	#### 	FUNCTIONS 	####################################

	def get_time_diference ( ):

		time_created = os.path.getctime ( FILE )

		time_created = datetime.datetime.fromtimestamp ( time_created )


		time_current = datetime.datetime.now ( )


		time_elapsed = ( time_current - time_created )

		time_elapsed = str ( time_elapsed ).split ( '.' ) [ 0 ]

		time_elapsed = time_elapsed.split ( ':' )


		return time_elapsed

	def get_cache_interval ( ):

		value   = None

		lines   = open ( CONFIG, 'r' ).readlines ( )

		capture = False


		for line in lines:

			if re.search ( r'CACHING', line ):

				capture = True

				continue

			if capture:

				if re.search ( r'CLEAR_INTERVAL=(\d{2}\:\d{2}\:\d{2})\s', line ):

					value = re.search ( r'CLEAR_INTERVAL=(\d{2}\:\d{2}\:\d{2})\s', line ).group ( 1 ).split ( ':' )

					value = [ str ( int ( entry ) ) for entry in value ]


					for i, character in enumerate ( value ):

						if ( len ( character ) - 1 ) == 0:

							value [ i ] = f'0{character}'

				else:

					continue

			if value:

				return value


		return ERROR

	def compare_timestamps ( ):

		elasped  = int ( ''.join (  time_elapsed  ) )

		interval = int ( ''.join ( cache_interval ).lstrip ( '0' ) )


		return True if elasped > interval else False

	#### 	LOGIC 	########################################

	if os.path.isfile ( FILE ):

		time_elapsed   = get_time_diference ( )

		cache_interval = get_cache_interval ( )


		if cache_interval == -1:

			print ( ' >> [ERROR] is_cached_file_old.py\n\t~ Could not locate caching settings in config.txt !' )

			return ERROR

		else:

			return compare_timestamps ( )

	else:

		return True
