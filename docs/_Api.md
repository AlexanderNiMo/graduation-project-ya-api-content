# swagger_client._Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_films_content_api_api_v1_film_search_get**](_Api.md#search_films_content_api_api_v1_film_search_get) | **GET** /content_api/api/v1/film/search/ | Поиск кинопроизведений
[**search_persons_content_api_api_v1_person_search_get**](_Api.md#search_persons_content_api_api_v1_person_search_get) | **GET** /content_api/api/v1/person/search/ | Поиск по людям

# **search_films_content_api_api_v1_film_search_get**
> list[Film] search_films_content_api_api_v1_film_search_get(query, page_size=page_size, page_number=page_number)

Поиск кинопроизведений

Полнотекстовый поиск по кинопроизведениям

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client._Api()
query = 'query_example' # str | search text_query
page_size = 50 # int | Page size (optional) (default to 50)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Поиск кинопроизведений
    api_response = api_instance.search_films_content_api_api_v1_film_search_get(query, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling _Api->search_films_content_api_api_v1_film_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| search text_query | 
 **page_size** | **int**| Page size | [optional] [default to 50]
 **page_number** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[Film]**](Film.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_persons_content_api_api_v1_person_search_get**
> list[FullPerson] search_persons_content_api_api_v1_person_search_get(query, page_size=page_size, page_number=page_number)

Поиск по людям

Полнотекстовый поиск по людям, учавствовшим в создании произведения

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client._Api()
query = 'query_example' # str | search text_query
page_size = 50 # int | Page size (optional) (default to 50)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Поиск по людям
    api_response = api_instance.search_persons_content_api_api_v1_person_search_get(query, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling _Api->search_persons_content_api_api_v1_person_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| search text_query | 
 **page_size** | **int**| Page size | [optional] [default to 50]
 **page_number** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[FullPerson]**](FullPerson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

