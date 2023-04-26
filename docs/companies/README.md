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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.EnrichCompanyRequest(
    id="a05dfc2d-df7c-4c78-8a1b-a928fc816742",
)

res = s.companies.enrich(req)

if res.body is not None:
    # handle response
```

## list_employees

List company employees

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ListEmployeesRequest(
    id="cb739205-9293-496f-aa75-96eb10faaa23",
    offset="corporis",
    per_page="explicabo",
)

res = s.companies.list_employees(req)

if res.body is not None:
    # handle response
```

## list_jobs

List company jobs

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.ListJobsRequest(
    id="c5955907-aff1-4a3a-afa9-467739251aa5",
    offset="odit",
    per_page="quo",
)

res = s.companies.list_jobs(req)

if res.body is not None:
    # handle response
```

## search

Search Companies

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.SearchCompaniesApplicationJSON(
    filter="sequi",
    limit="tenetur",
    page="ipsam",
    query="id",
)

res = s.companies.search(req)

if res.body is not None:
    # handle response
```
