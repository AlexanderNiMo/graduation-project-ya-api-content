# coding: utf-8

"""
    Read-only API для онлайн-кинотеатра

    Информация о фильмах, жанрах и людях, участвовавших в создании произведения  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from content_api.api_client import ApiClient


class _Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_films_content_api_api_v1_film_search_get(self, query, **kwargs):  # noqa: E501
        """Поиск кинопроизведений  # noqa: E501

        Полнотекстовый поиск по кинопроизведениям  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_films_content_api_api_v1_film_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: search text_query (required)
        :param int page_size: Page size
        :param int page_number: Page number
        :return: list[Film]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_films_content_api_api_v1_film_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_films_content_api_api_v1_film_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_films_content_api_api_v1_film_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """Поиск кинопроизведений  # noqa: E501

        Полнотекстовый поиск по кинопроизведениям  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_films_content_api_api_v1_film_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: search text_query (required)
        :param int page_size: Page size
        :param int page_number: Page number
        :return: list[Film]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'page_size', 'page_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_films_content_api_api_v1_film_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_films_content_api_api_v1_film_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page[size]', params['page_size']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page[number]', params['page_number']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/content_api/api/v1/film/search/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Film]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_persons_content_api_api_v1_person_search_get(self, query, **kwargs):  # noqa: E501
        """Поиск по людям  # noqa: E501

        Полнотекстовый поиск по людям, учавствовшим в создании произведения  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_persons_content_api_api_v1_person_search_get(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: search text_query (required)
        :param int page_size: Page size
        :param int page_number: Page number
        :return: list[FullPerson]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_persons_content_api_api_v1_person_search_get_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.search_persons_content_api_api_v1_person_search_get_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def search_persons_content_api_api_v1_person_search_get_with_http_info(self, query, **kwargs):  # noqa: E501
        """Поиск по людям  # noqa: E501

        Полнотекстовый поиск по людям, учавствовшим в создании произведения  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_persons_content_api_api_v1_person_search_get_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: search text_query (required)
        :param int page_size: Page size
        :param int page_number: Page number
        :return: list[FullPerson]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'page_size', 'page_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_persons_content_api_api_v1_person_search_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search_persons_content_api_api_v1_person_search_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page[size]', params['page_size']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page[number]', params['page_number']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/content_api/api/v1/person/search/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FullPerson]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
