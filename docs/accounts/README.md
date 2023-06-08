# accounts

## Overview

Accounts

### Available Operations

* [list_users](#list_users) - Show current user accounts

## list_users

Show current user accounts

### Example Usage

```python
import sdk


s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.accounts.list_users()

if res.body is not None:
    # handle response
```
