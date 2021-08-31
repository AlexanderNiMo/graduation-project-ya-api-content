# content.HealthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_content_api_api_health_get**](HealthApi.md#health_check_content_api_api_health_get) | **GET** /content_api/api/health/ | Health Check

# **health_check_content_api_api_health_get**
> Object health_check_content_api_api_health_get()

Health Check

### Example
```python
from __future__ import print_function
import time
import content
from content.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content.HealthApi()

try:
    # Health Check
    api_response = api_instance.health_check_content_api_api_health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->health_check_content_api_api_health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

