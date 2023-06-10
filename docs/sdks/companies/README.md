# companies

## Overview

Companies

### Available Operations

* [enrich](#enrich) - Enrich a company profile
* [list_employees](#list_employees) - List company employees
* [list_jobs](#list_jobs) - List company jobs
* [search](#search) - Search Companies

## enrich

Enrich a company profile

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.EnrichCompanyRequest(
    id='a05dfc2d-df7c-4c78-8a1b-a928fc816742',
)

res = s.companies.enrich(req)

if res.body is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.EnrichCompanyRequest](../../models/operations/enrichcompanyrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.EnrichCompanyResponse](../../models/operations/enrichcompanyresponse.md)**


## list_employees

List company employees

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListEmployeesRequest(
    id='cb739205-9293-496f-aa75-96eb10faaa23',
    offset='corporis',
    per_page='explicabo',
)

res = s.companies.list_employees(req)

if res.body is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListEmployeesRequest](../../models/operations/listemployeesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.ListEmployeesResponse](../../models/operations/listemployeesresponse.md)**


## list_jobs

List company jobs

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListJobsRequest(
    id='c5955907-aff1-4a3a-afa9-467739251aa5',
    offset='odit',
    per_page='quo',
)

res = s.companies.list_jobs(req)

if res.body is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.ListJobsRequest](../../models/operations/listjobsrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.ListJobsResponse](../../models/operations/listjobsresponse.md)**


## search

Search Companies

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.SearchCompaniesApplicationJSON(
    filter='sequi',
    limit='tenetur',
    page='ipsam',
    query='id',
)

res = s.companies.search(req)

if res.body is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.SearchCompaniesApplicationJSON](../../models/operations/searchcompaniesapplicationjson.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.SearchCompaniesResponse](../../models/operations/searchcompaniesresponse.md)**

