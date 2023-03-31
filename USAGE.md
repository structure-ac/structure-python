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
    country_code="corrupti",
    headquarters="provident",
    id="distinctio",
    name="quibusdam",
)
    
res = s.companies.enrich(req)

if res.body is not None:
    # handle response
```
<!-- End SDK Example Usage -->