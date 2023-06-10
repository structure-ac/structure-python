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
        bearer_auth="",
    ),
)

req = operations.EnrichPersonRequest(
    id='d019da1f-fe78-4f09-bb00-74f15471b5e6',
)

res = s.people.enrich(req)

if res.body is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.EnrichPersonRequest](../../models/operations/enrichpersonrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.EnrichPersonResponse](../../models/operations/enrichpersonresponse.md)**


## search

Search People

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchPeopleApplicationJSON(
    filter='repudiandae',
    limit='quae',
    page='ipsum',
    query='quidem',
)

res = s.people.search(req)

if res.body is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.SearchPeopleApplicationJSON](../../models/operations/searchpeopleapplicationjson.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.SearchPeopleResponse](../../models/operations/searchpeopleresponse.md)**

