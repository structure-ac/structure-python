"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sdk.models import operations

class People:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def enrich_person(self, request: operations.EnrichPersonRequest) -> operations.EnrichPersonResponse:
        r"""Enrich a person profile"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/people/enrich'
        
        query_params = utils.get_query_params(operations.EnrichPersonRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.EnrichPersonResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, '*/*'):
                res.body = http_res.content
        elif http_res.status_code in [401, 403, 404, 422]:
            pass

        return res

    def search_search(self, request: operations.SearchSearchApplicationJSON) -> operations.SearchSearchResponse:
        r"""Search People"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/people/search'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchSearchResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, '*/*'):
                res.body = http_res.content
        elif http_res.status_code in [401, 403]:
            pass

        return res

    