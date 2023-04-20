<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.EnrichCompanyRequest(
    id="89bd9d8d-69a6-474e-8f46-7cc8796ed151",
)
    
res = s.companies.enrich(req)

if res.body is not None:
    # handle response
```
<!-- End SDK Example Usage -->