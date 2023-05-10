import json

def parse_list_models ( list ):

	#### 	GLOBALS 	####################################

	result = { }

	temp   = { 'data': { }, 'permissions': { } }


	model_data   = json.loads ( str ( list ) )

	model_amount = len ( model_data [ 'data' ] )

	#### 	FUNCTIONS 	####################################

	def filter_list ( ):

		for data in model_data [ 'data' ]:

			for entry in data:

				if entry == 'permission':

					for permission in data [ entry ] [ 0 ]:

						temp [ 'permissions' ] [ permission ] = data [ entry ] [ 0 ] [ permission ]

				else:

					temp [ 'data' ] [ entry ] = data [ entry ]


			ROOT = temp [ 'data' ] [ 'root' ]


			if ROOT not in result.keys ( ):

				result [ ROOT ]                   = temp [    'data'     ]
				result [ ROOT ] [ 'permissions '] = temp [ 'permissions' ]

	#### 	LOGIC 	########################################

	filter_list ( )


	return result
