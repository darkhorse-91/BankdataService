
def data_format_utility(raw_data):

	formatted_data = []

	for data in raw_data:
		data_to_put = {"ifsc":None, "bank_id":None, "branch":None, "address":None, "city":None, "district":None, "state":None}
		for index, key in enumerate(data_to_put):
			data_to_put[key] = data[index]
		formatted_data.append(data_to_put)
		del data_to_put
	return formatted_data


