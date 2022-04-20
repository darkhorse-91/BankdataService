from flask import Flask, request
from bankapp.models import bank_model, branches_model, branch_autocomplete_model

app = Flask(__name__)



@app.route('/')
def index():
    banks = bank_model()
    return {'data': banks}



@app.route('/api/branches/autocomplete/')
def autocomplete():
	param_search = request.args.get('q')
	param_limit = request.args.get('limit')	
	param_offset = request.args.get('offset')

	if param_search == None or param_search =="":
		return {'message': 'Please provide a valid search parameter'}

	try:
		autocomplete_data = branch_autocomplete_model(param_search, param_limit, param_offset)

		return {'data': autocomplete_data}

	except Exception as e:
		print(e)
		return {'Error':'Something has not worked'},500


@app.route('/api/branches/')
def branches():
	param_search = request.args.get('q')
	param_limit = request.args.get('limit')	
	param_offset = request.args.get('offset')

	if param_search == None or param_search =="":
		return {'message': 'Please provide a valid search parameter'}

	try:
		branches_data = branches_model(param_search, param_limit, param_offset)

		return {'data': branches_data}

	except Exception as e:
		return {'Error':'Something has not worked'},500

