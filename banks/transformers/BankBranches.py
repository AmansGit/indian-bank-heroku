
def transform(data, name=None):
	# return type(data)
	return {
		'name': name,
		'ifsc': data.ifsc,
		'branch': data.branch,
		'address': data.address,
		'city': data.city,
		'district': data.district,
		'state': data.state
	}