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
        bearer_auth="YOUR_API_KEY",
    ),
)

    
res = s.accounts.accounts()

if res.body is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


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

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
