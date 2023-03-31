"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthsApplicationJSON:
    
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""The email of the user"""  
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""The password of the user"""  
    

@dataclasses.dataclass
class AuthsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    body: Optional[bytes] = dataclasses.field(default=None)  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    