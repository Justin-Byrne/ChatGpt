import os
import subprocess
import json

from os.path 						import abspath
from stat 							import S_IREAD, S_IRGRP, S_IROTH

from ...system.validation.is_file 	import is_file


PATH = f"{abspath ( '.' )}/cache"


def write_file ( filename, data, readonly = False ):

	FILE = f'{PATH}/{filename}.info'

	DATA = json.dumps ( data, indent=4 )


	if is_file ( FILE, None ):

		subprocess.run ( f'rm {FILE}', shell=True )


	with open( FILE, 'w' ) as writer:

		writer.write ( str ( DATA ) )


	if readonly:

		os.chmod ( FILE, S_IREAD | S_IRGRP | S_IROTH )
