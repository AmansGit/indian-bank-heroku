from banks.helpers import getBranchName

def transform(data):
	# return type(data)
	return {
		'ifsc': data.ifsc,
		'branch': data.branch,
		'address': data.address,
		'city': data.city,
		'district': data.district,
		'state': data.state,
		'bank': getBranchName(data.bank_id).name
	}