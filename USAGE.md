<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="YOUR_API_KEY",
    ),
)

    
res = s.accounts.accounts()

if res.body is not None:
    # handle response
```
<!-- End SDK Example Usage -->