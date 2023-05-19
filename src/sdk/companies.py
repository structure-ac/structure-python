"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sdk.models import operations

class Companies:
    r"""Companies"""
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
        
    
    def enrich(self, request: operations.EnrichCompanyRequest) -> operations.EnrichCompanyResponse:
        r"""Enrich a company profile"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.EnrichCompanyRequest, base_url, '/companies/{id}/enrich', request)
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.EnrichCompanyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, '*/*'):
                res.body = http_res.content
        elif http_res.status_code in [401, 403, 404, 422]:
            pass

        return res

    
    def list_employees(self, request: operations.ListEmployeesRequest) -> operations.ListEmployeesResponse:
        r"""List company employees"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListEmployeesRequest, base_url, '/companies/{id}/employees', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListEmployeesRequest, request)
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListEmployeesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, '*/*'):
                res.body = http_res.content
        elif http_res.status_code in [401, 403, 404]:
            pass

        return res

    
    def list_jobs(self, request: operations.ListJobsRequest) -> operations.ListJobsResponse:
        r"""List company jobs"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListJobsRequest, base_url, '/companies/{id}/jobs', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListJobsRequest, request)
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListJobsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, '*/*'):
                res.body = http_res.content
        elif http_res.status_code in [401, 403, 404]:
            pass

        return res

    
    def search(self, request: operations.SearchCompaniesApplicationJSON) -> operations.SearchCompaniesResponse:
        r"""Search Companies"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/companies/search'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SearchCompaniesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, '*/*'):
                res.body = http_res.content
        elif http_res.status_code in [401, 403]:
            pass

        return res

    