from django.conf.urls import url
from banks.views import branch_details, branch_details_city

urlpatterns = [
	# this url get the details of banks branches according to bank name and city
	url(r'^details', branch_details_city),
	# this url get the bank details according to the ifsc code
	url(r'^ifsc/(?P<ifsc>[0-9a-zA-Z]+)$', branch_details)
]
