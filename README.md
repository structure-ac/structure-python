# Structure

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/structure-ac/structure-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
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

<!-- Start SDK Available Operations -->
## SDK Available Operations


### accounts

* `accounts` - Show current user accounts

### auths

* `auths` - Login user

### companies

* `company_employees` - Show company employees
* `company_jobs` - Show company jobs
* `enrich_company` - Enrich a company profile
* `search_companies` - Search Companies

### me

* `me` - Show current user

### people

* `enrich_person` - Enrich a person profile
* `search_search` - Search People
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)