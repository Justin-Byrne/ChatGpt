import sys
import os
import unittest

from os.path 	import dirname, abspath

# APPEND PARENT 'SOURCE' PATH TO SYS.PATH
sys.path.append ( abspath ( '..' ) )

# IMPORTING DEVELOPER FUNCTIONS
from app.utilities.util    import Util

ORG='0123456789ABCDEFGHIJKLMN'
KEY='0123456789ABCDEFGHIJKLMNOPQRSTUV0123456789ABCDEF'

# WDIR  = f"{os.getcwd ( )}/cases"
# FILE  = f"{WDIR}/test-file.txt"
# FLAG  = "-f"
# DIRE  = f"{WDIR}"

ERROR = -1

class TestUtil ( unittest.TestCase ):

	#### 	SYSTEM 	########################################

	# VALIDATION

	# def test_is_directory     ( self ): 						# 01

	# 	self.assertTrue  ( Util.is_directory ( DIRE ) )

	# 	self.assertFalse ( Util.is_directory ( f"{DIRE}/testtesttest" ) )

	# def test_is_file          ( self ): 						# 02

	# 	self.assertTrue  ( Util.is_file ( FILE         ) )

	# 	self.assertFalse ( Util.is_file ( DIRE         ) )

	# 	self.assertTrue  ( Util.is_file ( FILE, '.txt' ) )

	# 	self.assertFalse ( Util.is_file ( FILE, 'txt'  ) )

	# def test_is_flag          ( self ): 						# 03

	# 	self.assertTrue  ( Util.is_flag ( FLAG ) )

	# 	self.assertFalse ( Util.is_flag ( '#f' ) )

	# COMMAND

	# def test_get_command_type ( self ): 						# 05

		# self.assertEqual ( Util.get_command_type ( FLAG ), 'flag'      )

		# self.assertEqual ( Util.get_command_type ( FILE ), 'file'      )

		# self.assertEqual ( Util.get_command_type ( DIRE ), 'directory' )

	def test_get_commands     ( self ): 						# 06

		pass

# TEST MAIN
if __name__ == '__main__':

	unittest.main ( )
