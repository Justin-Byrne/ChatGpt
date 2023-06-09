def output ( source, message, type = 'error' ):

	result = ''

	start  = '\t~ '

	cursor = '>> '


	source = f'{source}.py\n'

	ahead  = f'{cursor}[{type.upper ( )}] - '


	match message:

		case str ( ):

			result = f'{start}{message.title ( )}'

		case list ( ):

			if len ( message ) > 1:

				for note in message:

					result += f'{start}{note.title ( )}\n'


				result = result.rstrip ( '\n' )

			else:

				result = f'{start}{message [ 0 ].title ( )}'


	print ( f'{ahead}{source}{result}')
