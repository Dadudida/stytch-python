# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.consumer.models.passwords_existing_password import ResetResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class ExistingPassword:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def reset(
        self,
        email: str,
        existing_password: str,
        new_password: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> ResetResponse:
        """Reset the User’s password using their existing password.

        Note that a successful password reset via an existing password will revoke all active sessions for the `user_id`.

        Fields:
          - email: The email address of the end user.
          - existing_password: The user's existing password.
          - new_password: The new password for the user.
          - session_token: The `session_token` associated with a User's existing Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        data: Dict[str, Any] = {
            "email": email,
            "existing_password": existing_password,
            "new_password": new_password,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/passwords/existing_password/reset", data)
        res = self.sync_client.post(url, data)
        return ResetResponse.from_json(res.response.status_code, res.json)

    async def reset_async(
        self,
        email: str,
        existing_password: str,
        new_password: str,
        session_token: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_jwt: Optional[str] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> ResetResponse:
        """Reset the User’s password using their existing password.

        Note that a successful password reset via an existing password will revoke all active sessions for the `user_id`.

        Fields:
          - email: The email address of the end user.
          - existing_password: The user's existing password.
          - new_password: The new password for the user.
          - session_token: The `session_token` associated with a User's existing Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will not be created.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.

          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes.
        """  # noqa
        data: Dict[str, Any] = {
            "email": email,
            "existing_password": existing_password,
            "new_password": new_password,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims

        url = self.api_base.url_for("/v1/passwords/existing_password/reset", data)
        res = await self.async_client.post(url, data)
        return ResetResponse.from_json(res.response.status, res.json)
