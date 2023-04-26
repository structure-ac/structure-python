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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.LoginApplicationJSON(
    email="Kenny50@yahoo.com",
    password="rem",
)

res = s.user.login(req)

if res.body is not None:
    # handle response
```

## me

Show current user

### Example Usage

```python
import sdk


s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.user.me()

if res.body is not None:
    # handle response
```
