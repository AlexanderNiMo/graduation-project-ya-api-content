# content_api.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**film_details_content_api_api_v1_film_film_id_get**](DefaultApi.md#film_details_content_api_api_v1_film_film_id_get) | **GET** /content_api/api/v1/film/{film_id}/ | Кинопроизведение
[**film_details_content_api_api_v1_film_film_id_get_0**](DefaultApi.md#film_details_content_api_api_v1_film_film_id_get_0) | **GET** /content_api/api/v1/film/{film_id}/ | Кинопроизведение
[**films_list_content_api_api_v1_film_get**](DefaultApi.md#films_list_content_api_api_v1_film_get) | **GET** /content_api/api/v1/film/ | Кинопроизведения
[**films_list_content_api_api_v1_film_get_0**](DefaultApi.md#films_list_content_api_api_v1_film_get_0) | **GET** /content_api/api/v1/film/ | Кинопроизведения
[**genres_content_api_api_v1_genre_genre_id_get**](DefaultApi.md#genres_content_api_api_v1_genre_genre_id_get) | **GET** /content_api/api/v1/genre/{genre_id} | Жанр
[**genres_content_api_api_v1_genre_genre_id_get_0**](DefaultApi.md#genres_content_api_api_v1_genre_genre_id_get_0) | **GET** /content_api/api/v1/genre/{genre_id} | Жанр
[**genres_content_api_api_v1_genre_get**](DefaultApi.md#genres_content_api_api_v1_genre_get) | **GET** /content_api/api/v1/genre | Жанры кинопроизведений
[**genres_content_api_api_v1_genre_get_0**](DefaultApi.md#genres_content_api_api_v1_genre_get_0) | **GET** /content_api/api/v1/genre | Жанры кинопроизведений
[**get_person_content_api_api_v1_person_person_id_get**](DefaultApi.md#get_person_content_api_api_v1_person_person_id_get) | **GET** /content_api/api/v1/person/{person_id}/ | Детальное описание человека
[**get_person_content_api_api_v1_person_person_id_get_0**](DefaultApi.md#get_person_content_api_api_v1_person_person_id_get_0) | **GET** /content_api/api/v1/person/{person_id}/ | Детальное описание человека
[**get_person_film_content_api_api_v1_person_person_id_film_get**](DefaultApi.md#get_person_film_content_api_api_v1_person_person_id_film_get) | **GET** /content_api/api/v1/person/{person_id}/film/ | Фильмы человека
[**get_person_film_content_api_api_v1_person_person_id_film_get_0**](DefaultApi.md#get_person_film_content_api_api_v1_person_person_id_film_get_0) | **GET** /content_api/api/v1/person/{person_id}/film/ | Фильмы человека
[**search_films_content_api_api_v1_film_search_get**](DefaultApi.md#search_films_content_api_api_v1_film_search_get) | **GET** /content_api/api/v1/film/search/ | Поиск кинопроизведений
[**search_persons_content_api_api_v1_person_search_get**](DefaultApi.md#search_persons_content_api_api_v1_person_search_get) | **GET** /content_api/api/v1/person/search/ | Поиск по людям
[**short_film_detail_content_api_api_v1_film_short_film_id_get**](DefaultApi.md#short_film_detail_content_api_api_v1_film_short_film_id_get) | **GET** /content_api/api/v1/film/short/{film_id}/ | Кинопроизведение
[**short_film_detail_content_api_api_v1_film_short_film_id_get_0**](DefaultApi.md#short_film_detail_content_api_api_v1_film_short_film_id_get_0) | **GET** /content_api/api/v1/film/short/{film_id}/ | Кинопроизведение

# **film_details_content_api_api_v1_film_film_id_get**
> FilmDetail film_details_content_api_api_v1_film_film_id_get(film_id)

Кинопроизведение

Детальное описание кинопроизведения

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
film_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Кинопроизведение
    api_response = api_instance.film_details_content_api_api_v1_film_film_id_get(film_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->film_details_content_api_api_v1_film_film_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **film_id** | [**str**](.md)|  | 

### Return type

[**FilmDetail**](FilmDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **film_details_content_api_api_v1_film_film_id_get_0**
> FilmDetail film_details_content_api_api_v1_film_film_id_get_0(film_id)

Кинопроизведение

Детальное описание кинопроизведения

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
film_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Кинопроизведение
    api_response = api_instance.film_details_content_api_api_v1_film_film_id_get_0(film_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->film_details_content_api_api_v1_film_film_id_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **film_id** | [**str**](.md)|  | 

### Return type

[**FilmDetail**](FilmDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **films_list_content_api_api_v1_film_get**
> list[Film] films_list_content_api_api_v1_film_get(filter_genre=filter_genre, sort=sort, page_size=page_size, page_number=page_number)

Кинопроизведения

Список кинопроизведений с соритровкой, отборами и пагинацией

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
filter_genre = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | filter on genre (optional)
sort = 'sort_example' # str | sort on filed (order: \"-\" before filed name is desc) (optional)
page_size = 50 # int | Page size (optional) (default to 50)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Кинопроизведения
    api_response = api_instance.films_list_content_api_api_v1_film_get(filter_genre=filter_genre, sort=sort, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->films_list_content_api_api_v1_film_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_genre** | [**str**](.md)| filter on genre | [optional] 
 **sort** | **str**| sort on filed (order: \&quot;-\&quot; before filed name is desc) | [optional] 
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

# **films_list_content_api_api_v1_film_get_0**
> list[Film] films_list_content_api_api_v1_film_get_0(filter_genre=filter_genre, sort=sort, page_size=page_size, page_number=page_number)

Кинопроизведения

Список кинопроизведений с соритровкой, отборами и пагинацией

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
filter_genre = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | filter on genre (optional)
sort = 'sort_example' # str | sort on filed (order: \"-\" before filed name is desc) (optional)
page_size = 50 # int | Page size (optional) (default to 50)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Кинопроизведения
    api_response = api_instance.films_list_content_api_api_v1_film_get_0(filter_genre=filter_genre, sort=sort, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->films_list_content_api_api_v1_film_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_genre** | [**str**](.md)| filter on genre | [optional] 
 **sort** | **str**| sort on filed (order: \&quot;-\&quot; before filed name is desc) | [optional] 
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

# **genres_content_api_api_v1_genre_genre_id_get**
> Genre genres_content_api_api_v1_genre_genre_id_get(genre_id)

Жанр

Описание конкретного кинопроизведения

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
genre_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Жанр
    api_response = api_instance.genres_content_api_api_v1_genre_genre_id_get(genre_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->genres_content_api_api_v1_genre_genre_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genre_id** | [**str**](.md)|  | 

### Return type

[**Genre**](Genre.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genres_content_api_api_v1_genre_genre_id_get_0**
> Genre genres_content_api_api_v1_genre_genre_id_get_0(genre_id)

Жанр

Описание конкретного кинопроизведения

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
genre_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Жанр
    api_response = api_instance.genres_content_api_api_v1_genre_genre_id_get_0(genre_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->genres_content_api_api_v1_genre_genre_id_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genre_id** | [**str**](.md)|  | 

### Return type

[**Genre**](Genre.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genres_content_api_api_v1_genre_get**
> list[Genre] genres_content_api_api_v1_genre_get(sort=sort, page_size=page_size, page_number=page_number)

Жанры кинопроизведений

Список жанров кинопроизведений

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
sort = 'sort_example' # str | sort on filed (order: \"-\" before filed name is desc) (optional)
page_size = 50 # int | Page size (optional) (default to 50)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Жанры кинопроизведений
    api_response = api_instance.genres_content_api_api_v1_genre_get(sort=sort, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->genres_content_api_api_v1_genre_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| sort on filed (order: \&quot;-\&quot; before filed name is desc) | [optional] 
 **page_size** | **int**| Page size | [optional] [default to 50]
 **page_number** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[Genre]**](Genre.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genres_content_api_api_v1_genre_get_0**
> list[Genre] genres_content_api_api_v1_genre_get_0(sort=sort, page_size=page_size, page_number=page_number)

Жанры кинопроизведений

Список жанров кинопроизведений

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
sort = 'sort_example' # str | sort on filed (order: \"-\" before filed name is desc) (optional)
page_size = 50 # int | Page size (optional) (default to 50)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Жанры кинопроизведений
    api_response = api_instance.genres_content_api_api_v1_genre_get_0(sort=sort, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->genres_content_api_api_v1_genre_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| sort on filed (order: \&quot;-\&quot; before filed name is desc) | [optional] 
 **page_size** | **int**| Page size | [optional] [default to 50]
 **page_number** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[Genre]**](Genre.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_content_api_api_v1_person_person_id_get**
> FullPerson get_person_content_api_api_v1_person_person_id_get(person_id)

Детальное описание человека

Полная информация по человеку на основании его id

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
person_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Детальное описание человека
    api_response = api_instance.get_person_content_api_api_v1_person_person_id_get(person_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_person_content_api_api_v1_person_person_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | [**str**](.md)|  | 

### Return type

[**FullPerson**](FullPerson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_content_api_api_v1_person_person_id_get_0**
> FullPerson get_person_content_api_api_v1_person_person_id_get_0(person_id)

Детальное описание человека

Полная информация по человеку на основании его id

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
person_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Детальное описание человека
    api_response = api_instance.get_person_content_api_api_v1_person_person_id_get_0(person_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_person_content_api_api_v1_person_person_id_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | [**str**](.md)|  | 

### Return type

[**FullPerson**](FullPerson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_film_content_api_api_v1_person_person_id_film_get**
> list[Film] get_person_film_content_api_api_v1_person_person_id_film_get(person_id, page_size=page_size, page_number=page_number)

Фильмы человека

Информация фильмах, в которых учавствовал человек

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
person_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page_size = 50 # int | Page size (optional) (default to 50)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Фильмы человека
    api_response = api_instance.get_person_film_content_api_api_v1_person_person_id_film_get(person_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_person_film_content_api_api_v1_person_person_id_film_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | [**str**](.md)|  | 
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

# **get_person_film_content_api_api_v1_person_person_id_film_get_0**
> list[Film] get_person_film_content_api_api_v1_person_person_id_film_get_0(person_id, page_size=page_size, page_number=page_number)

Фильмы человека

Информация фильмах, в которых учавствовал человек

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
person_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page_size = 50 # int | Page size (optional) (default to 50)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Фильмы человека
    api_response = api_instance.get_person_film_content_api_api_v1_person_person_id_film_get_0(person_id, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_person_film_content_api_api_v1_person_person_id_film_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | [**str**](.md)|  | 
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

# **search_films_content_api_api_v1_film_search_get**
> list[Film] search_films_content_api_api_v1_film_search_get(query, page_size=page_size, page_number=page_number)

Поиск кинопроизведений

Полнотекстовый поиск по кинопроизведениям

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
query = 'query_example' # str | search text_query
page_size = 50 # int | Page size (optional) (default to 50)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Поиск кинопроизведений
    api_response = api_instance.search_films_content_api_api_v1_film_search_get(query, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_films_content_api_api_v1_film_search_get: %s\n" % e)
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
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
query = 'query_example' # str | search text_query
page_size = 50 # int | Page size (optional) (default to 50)
page_number = 1 # int | Page number (optional) (default to 1)

try:
    # Поиск по людям
    api_response = api_instance.search_persons_content_api_api_v1_person_search_get(query, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_persons_content_api_api_v1_person_search_get: %s\n" % e)
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

# **short_film_detail_content_api_api_v1_film_short_film_id_get**
> Film short_film_detail_content_api_api_v1_film_short_film_id_get(film_id)

Кинопроизведение

Краткое описание кинопроизведения

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
film_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Кинопроизведение
    api_response = api_instance.short_film_detail_content_api_api_v1_film_short_film_id_get(film_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->short_film_detail_content_api_api_v1_film_short_film_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **film_id** | [**str**](.md)|  | 

### Return type

[**Film**](Film.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **short_film_detail_content_api_api_v1_film_short_film_id_get_0**
> Film short_film_detail_content_api_api_v1_film_short_film_id_get_0(film_id)

Кинопроизведение

Краткое описание кинопроизведения

### Example
```python
from __future__ import print_function
import time
import content_api
from content_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = content_api.DefaultApi()
film_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Кинопроизведение
    api_response = api_instance.short_film_detail_content_api_api_v1_film_short_film_id_get_0(film_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->short_film_detail_content_api_api_v1_film_short_film_id_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **film_id** | [**str**](.md)|  | 

### Return type

[**Film**](Film.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

