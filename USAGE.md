<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth=shared.SchemeBearerAuth(
            authorization="Bearer YOUR_BEARER_TOKEN_HERE",
        ),
    ),
)

    
res = s.accounts.accounts()

if res.body is not None:
    # handle response
```
<!-- End SDK Example Usage -->