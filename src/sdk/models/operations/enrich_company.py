"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class EnrichCompanyRequest:
    
    country_code: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'country_code', 'style': 'form', 'explode': True }})
    r"""Country code of the company"""  
    headquarters: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'headquarters', 'style': 'form', 'explode': True }})
    r"""The headquarters of the company"""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'id', 'style': 'form', 'explode': True }})
    r"""ID of the company"""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""Game of the company"""  
    

@dataclasses.dataclass
class EnrichCompanyResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    body: Optional[bytes] = dataclasses.field(default=None)  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    