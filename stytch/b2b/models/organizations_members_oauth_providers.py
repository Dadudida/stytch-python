# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import List

from stytch.core.response_base import ResponseBase


class GoogleResponse(ResponseBase):
    """Response type for `OAuthProviders.google`.
    Fields:
      - provider_type: Denotes the OAuth identity provider that the user has authenticated with, e.g. Google, Microsoft, GitHub etc.
      - provider_subject: The unique identifier for the User within a given OAuth provider. Also commonly called the `sub` or "Subject field" in OAuth protocols.
      - access_token: The `access_token` that you may use to access the User's data in the provider's API.
      - access_token_expires_in: The number of seconds until the access token expires.
      - id_token: The `id_token` returned by the OAuth provider. ID Tokens are JWTs that contain structured information about a user. The exact content of each ID Token varies from provider to provider. ID Tokens are returned from OAuth providers that conform to the [OpenID Connect](https://openid.net/foundation/) specification, which is based on OAuth.
      - scopes: The OAuth scopes included for a given provider. See each provider's section above to see which scopes are included by default and how to add custom scopes.
    """  # noqa

    provider_type: str
    provider_subject: str
    access_token: str
    access_token_expires_in: int
    id_token: str
    scopes: List[str]


class MicrosoftResponse(ResponseBase):
    """Response type for `OAuthProviders.microsoft`.
    Fields:
      - provider_type: Denotes the OAuth identity provider that the user has authenticated with, e.g. Google, Microsoft, GitHub etc.
      - provider_subject: The unique identifier for the User within a given OAuth provider. Also commonly called the `sub` or "Subject field" in OAuth protocols.
      - access_token: The `access_token` that you may use to access the User's data in the provider's API.
      - access_token_expires_in: The number of seconds until the access token expires.
      - id_token: The `id_token` returned by the OAuth provider. ID Tokens are JWTs that contain structured information about a user. The exact content of each ID Token varies from provider to provider. ID Tokens are returned from OAuth providers that conform to the [OpenID Connect](https://openid.net/foundation/) specification, which is based on OAuth.
      - scopes: The OAuth scopes included for a given provider. See each provider's section above to see which scopes are included by default and how to add custom scopes.
    """  # noqa

    provider_type: str
    provider_subject: str
    access_token: str
    access_token_expires_in: int
    id_token: str
    scopes: List[str]
