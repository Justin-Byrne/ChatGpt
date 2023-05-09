import os
import openai

ERROR = -1

def openai_connect ( API_ORG, API_KEY ):

	result = ERROR


	openai.organization = API_ORG

	openai.api_key 		= API_KEY


	try:

		result = openai.Model.list ( )

	except:

		print ( '>> [ERROR] openai_connect.py\n\t~ Open AI connection failed !' )


	return result
