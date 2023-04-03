<div align="center">
    <picture>
        <source srcset="https://user-images.githubusercontent.com/6267663/229523981-b357a689-adc6-4905-ac0e-e432aee5800b.png" media="(prefers-color-scheme: dark)">
        <img src="https://user-images.githubusercontent.com/6267663/229523981-b357a689-adc6-4905-ac0e-e432aee5800b.png">
    </picture>
    <h1>Python SDK</h1>
   <p>Discover rich information on people and companies</p>
   <a href="https://docs.structure.ac/"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=2564ec&style=for-the-badge" /></a>
   <a href="https://github.com/structure-ac/structure-python/actions"><img src="https://img.shields.io/github/actions/workflow/status/structure-ac/structure-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/structure-ac/structure-python/releases"><img src="https://img.shields.io/github/v/release/structure-ac/structure-python?sort=semver&style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install structure_py
```
<!-- End SDK Installation -->

## Authentication
You'll need to authenticate your requests to access any of the endpoints in the Structure API. In this guide, we'll look at how authentication works. Structure offers authentication for your API requests with a token.

### OAuth2 with bearer token
Authentication with the Structure API is using OAuth2. When establishing a connection using OAuth2, you will need your access token — you will find it in the [Structure dashboard](https://www.structure.ac/api_tokens) under API settings.

## SDK Example Usage
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

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### accounts

* `list_users` - Show current user accounts

### companies

* `enrich` - Enrich a company profile
* `list_employees` - List company employees
* `list_jobs` - List company jobs
* `search` - Search Companies

### people

* `enrich` - Enrich a person profile
* `search` - Search People

### user

* `login` - Login user
* `me` - Show current user
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
