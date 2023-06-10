# user

## Overview

User

### Available Operations

* [login](#login) - Login user
* [me](#me) - Show current user

## login

Login user

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.LoginApplicationJSON(
    email='Kenny50@yahoo.com',
    password='rem',
)

res = s.user.login(req)

if res.body is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.LoginApplicationJSON](../../models/operations/loginapplicationjson.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.LoginResponse](../../models/operations/loginresponse.md)**


## me

Show current user

### Example Usage

```python
import sdk


s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.user.me()

if res.body is not None:
    # handle response
```


### Response

**[operations.MeResponse](../../models/operations/meresponse.md)**

