# people

## Overview

People

### Available Operations

* [enrich](#enrich) - Enrich a person profile
* [search](#search) - Search People

## enrich

Enrich a person profile

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.EnrichPersonRequest(
    id="d019da1f-fe78-4f09-bb00-74f15471b5e6",
)

res = s.people.enrich(req)

if res.body is not None:
    # handle response
```

## search

Search People

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.SearchPeopleApplicationJSON(
    filter="repudiandae",
    limit="quae",
    page="ipsum",
    query="quidem",
)

res = s.people.search(req)

if res.body is not None:
    # handle response
```
