from banks.repository import *
from banks.models import *

def getBranchDetails(ifsc):
	# this will return the database result according for ifsc code
	filterAttr = {
		'ifsc': ifsc
	}
	return filterByAttribute(Branches, filterAttr)

def getBranchName(code):
	# this will return class object for Banks model for transformer.BranchDetails.py
	filterAttr = {
		'id': code
	}
	return filterByAttribute(Banks, filterAttr)

def getBranchCity(bank, city):
	# this method will filter out the database result according to bank and city
	filterAttr1 = {
		'name': bank
	}
	bank = filterByAttribute(Banks, filterAttr1)
	filterAttr2 = {
		'bank_id': bank.id,
		'city': city 
	}
	return filterAttribute(Branches, filterAttr2), bank.name