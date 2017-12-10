# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from indianBanks import BaseControllers
from banks.helpers import *
from banks.transformers import BranchDetails, BankBranches


def branch_details_city(request):
	# variable decleared to get the database result and return the reponse
	bankBranches = []
	if request.method == 'GET':
		try:
			name = request.GET.get('name')
			city = request.GET.get('city')
			# if condition check weather the query param is corret of not
			if ((request.GET) == {} or (name is None or city is None)): 
				raise
			try:
				# getBranchCity(name, city) method return the queryset for branch details and banks name
				bankBranches, bank = getBranchCity(name, city)
			except:
				return BaseControllers.respondWithError(500, 'Server Error')
		except:
			return BaseControllers.respondWithError(422, 'Please check url param')
		return BaseControllers.respondWithCollection(200, bankBranches, BankBranches, Optional=bank)
	else:
		return BaseControllers.respondWithError(405, 'Method not found')

def branch_details(request, ifsc):
	# variable decleared to get the database result and return the reponse
	branchData = {}
	if request.method == 'GET':
		try:
			# this will return the class object of Branches model
			branchData = getBranchDetails(ifsc)
		except: 
			return BaseControllers.respondWithError(422, 'Given Bank ifsc code not found')
		return BaseControllers.respondWithItem(200, branchData, BranchDetails)
	else:
		return BaseControllers.respondWithError(405, 'Method not found')
