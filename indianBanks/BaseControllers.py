from django.http import JsonResponse
import json

def respondWithItem(statusCode, data, transformer):
    response = {}
    response['data'] = transformer.transform(data)
    response['notification'] = {}
    response['notification']['hint'] = "Response Sent"
    response['notification']['message'] = "Success"
    response['notification']['code'] = 200
    response['notification']['type'] = "Success"
    
    return JsonResponse(response, content_type='application/json', status=statusCode)

# respond with error
def respondWithError(statusCode, message):
    response = {}
    response['data'] = []
    response['notification'] = {}
    response['notification']['hint'] = "Error"
    response['notification']['message'] = message
    response['notification']['code'] = statusCode
    response['notification']['type'] = "Failed"
    
    return JsonResponse(response, content_type='application/json', status=statusCode)

# respond with success
def respondWithSuccess(statusCode, message):
    response = {}
    response['data'] = []
    response['notification'] = {}
    response['notification']['hint'] = "Success"
    response['notification']['message'] = message
    response['notification']['code'] = statusCode
    response['notification']['type'] = "Success"
    return JsonResponse(response, content_type='application/json', status=statusCode)

def respondWithCollection(statusCode, collection, transformer, Optional=None):
    response = {}
    response['data'] = fetchData(transformer, collection, Optional)
    response['notification'] = {}
    response['notification']['hint'] = "Response Sent"
    response['notification']['message'] = "Success"
    response['notification']['code'] = 200
    response['notification']['type'] = "Success"
    return JsonResponse(response, content_type='application/json', status=statusCode)

def fetchData(transformer, collection, bank=None):
    return [transformer.transform(data, bank) for data in collection]