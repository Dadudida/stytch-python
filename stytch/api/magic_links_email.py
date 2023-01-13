# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, Optional, Union

import pydantic

from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.core.models import Name
from stytch.models.magic_links_email import (
    InviteResponse,
    LoginOrCreateResponse,
    RevokeInviteResponse,
    SendResponse,
)


class Email:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    @property
    def sub_url(self) -> str:
        return "magic_links/email"

    def send(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        locale: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
        code_challenge: Optional[str] = None,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> SendResponse:
        """[Stytch docs](https://stytch.com/docs/api/send-by-email)

        Send a magic link to an existing Stytch user using their email address. If you'd like to create a user and send them a magic link by email with one request, use our [log in or create endpoint](https://stytch.com/docs/api/log-in-or-create-user-by-email).

        Parameters:

        - `email`: The email of the user to send the invite magic link to.

        - `login_magic_link_url`: The url the user clicks from the login email magic link. This should be a url that your app receives and parses and subsequently send an API request to authenticate the magic link and log in the user. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.

        - `signup_magic_link_url`: The url the user clicks from the sign-up email magic link. This should be a url that your app receives and parses and subsequently send an api request to authenticate the magic link and sign-up the user. If this value is not passed, the default sign-up redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.

        - `login_expiration_minutes`: Set the expiration for the login email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

        - `signup_expiration_minutes`: Set the expiration for the sign-up email magic link, in minutes. By default, it expires in 1 week. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

        - `locale`: Used to determine which language to use when sending the user this delivery method. Parameter is a two character [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"` or `"es"`.

          Currently supported languages are English (en) and Spanish (es); if no value is provided, the copy defaults to English.

          Request more languages for support [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link)!

        - `attributes`: Provided attributes help with fraud detection.

        - `code_challenge`: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.

        - `user_id`: The `user_id` of the user to associate the email with. This parameter allows you to associate a new email address with an existing Stytch User.

          Only include a `user_id` if the user in question already has an active and valid session at the time of the send operation; without this safety check a malicious user may use this as an account takeover vector.

        - `session_token`: The `session_token` belonging to the user that you wish to associate the email with.

        - `session_jwt`: The `session_jwt` belonging to the user that you wish to associate the email with.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
        }

        if login_magic_link_url is not None:
            payload["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            payload["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if locale is not None:
            payload["locale"] = locale
        if attributes is not None:
            payload["attributes"] = attributes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "send")

        res = self.sync_client.post(url, json=payload)
        return SendResponse.from_json(res.response.status_code, res.json)

    async def send_async(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        locale: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
        code_challenge: Optional[str] = None,
        user_id: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> SendResponse:
        """[Stytch docs](https://stytch.com/docs/api/send-by-email)

        Send a magic link to an existing Stytch user using their email address. If you'd like to create a user and send them a magic link by email with one request, use our [log in or create endpoint](https://stytch.com/docs/api/log-in-or-create-user-by-email).

        Parameters:

        - `email`: The email of the user to send the invite magic link to.

        - `login_magic_link_url`: The url the user clicks from the login email magic link. This should be a url that your app receives and parses and subsequently send an API request to authenticate the magic link and log in the user. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.

        - `signup_magic_link_url`: The url the user clicks from the sign-up email magic link. This should be a url that your app receives and parses and subsequently send an api request to authenticate the magic link and sign-up the user. If this value is not passed, the default sign-up redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.

        - `login_expiration_minutes`: Set the expiration for the login email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

        - `signup_expiration_minutes`: Set the expiration for the sign-up email magic link, in minutes. By default, it expires in 1 week. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

        - `locale`: Used to determine which language to use when sending the user this delivery method. Parameter is a two character [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"` or `"es"`.

          Currently supported languages are English (en) and Spanish (es); if no value is provided, the copy defaults to English.

          Request more languages for support [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link)!

        - `attributes`: Provided attributes help with fraud detection.

        - `code_challenge`: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.

        - `user_id`: The `user_id` of the user to associate the email with. This parameter allows you to associate a new email address with an existing Stytch User.

          Only include a `user_id` if the user in question already has an active and valid session at the time of the send operation; without this safety check a malicious user may use this as an account takeover vector.

        - `session_token`: The `session_token` belonging to the user that you wish to associate the email with.

        - `session_jwt`: The `session_jwt` belonging to the user that you wish to associate the email with.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
        }

        if login_magic_link_url is not None:
            payload["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            payload["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if locale is not None:
            payload["locale"] = locale
        if attributes is not None:
            payload["attributes"] = attributes
        if code_challenge is not None:
            payload["code_challenge"] = code_challenge
        if user_id is not None:
            payload["user_id"] = user_id
        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "send")

        res = await self.async_client.post(url, json=payload)
        return SendResponse.from_json(res.response.status, res.json)

    def login_or_create(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        create_user_as_pending: Optional[bool] = None,
        locale: Optional[str] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> LoginOrCreateResponse:
        """[Stytch docs](https://stytch.com/docs/api/log-in-or-create-user-by-email)

        Send either a login or signup magic link to the user based on if the email is associated with a user already. A new or pending user will receive a signup magic link. An active user will receive a login magic link. For more information on how to control the status your users are created in see the `create_user_as_pending` flag.

        Parameters:

        - `email`: The email of the user to send the invite magic link to.

        - `login_magic_link_url`: The url the user clicks from the login email magic link. This should be a url that your app receives and parses and subsequently send an API request to authenticate the magic link and log in the user. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.

        - `signup_magic_link_url`: The url the user clicks from the sign-up email magic link. This should be a url that your app receives and parses and subsequently send an api request to authenticate the magic link and sign-up the user. If this value is not passed, the default sign-up redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.

        - `login_expiration_minutes`: Set the expiration for the login email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

        - `signup_expiration_minutes`: Set the expiration for the sign-up email magic link, in minutes. By default, it expires in 1 week. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

        - `create_user_as_pending`: Flag for whether or not to save a user as pending vs active in Stytch. Defaults to false. If true, new users will be created with status pending in Stytch's backend. Their status will remain pending and they will continue to receive sign-up magic links until a magic link is authenticated for that user. If false, new users will be created with status active. They will receive a sign-up magic link for their first magic link but subsequent magic links will use the login email template, even if the user never authenticated their initial magic link.

        - `locale`: Used to determine which language to use when sending the user this delivery method. Parameter is a two character [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"` or `"es"`.

          Currently supported languages are English (en) and Spanish (es); if no value is provided, the copy defaults to English.

          Request more languages for support [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link)!

        - `attributes`: Provided attributes help with fraud detection.

        - `code_challenge`: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
        }

        if login_magic_link_url is not None:
            payload["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            payload["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if create_user_as_pending is not None:
            payload["create_user_as_pending"] = create_user_as_pending
        if locale is not None:
            payload["locale"] = locale
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "login_or_create")

        res = self.sync_client.post(url, json=payload)
        return LoginOrCreateResponse.from_json(res.response.status_code, res.json)

    async def login_or_create_async(
        self,
        email: str,
        login_magic_link_url: Optional[str] = None,
        signup_magic_link_url: Optional[str] = None,
        login_expiration_minutes: Optional[int] = None,
        signup_expiration_minutes: Optional[int] = None,
        create_user_as_pending: Optional[bool] = None,
        locale: Optional[str] = None,
        login_template_id: Optional[str] = None,
        signup_template_id: Optional[str] = None,
    ) -> LoginOrCreateResponse:
        """[Stytch docs](https://stytch.com/docs/api/log-in-or-create-user-by-email)

        Send either a login or signup magic link to the user based on if the email is associated with a user already. A new or pending user will receive a signup magic link. An active user will receive a login magic link. For more information on how to control the status your users are created in see the `create_user_as_pending` flag.

        Parameters:

        - `email`: The email of the user to send the invite magic link to.

        - `login_magic_link_url`: The url the user clicks from the login email magic link. This should be a url that your app receives and parses and subsequently send an API request to authenticate the magic link and log in the user. If this value is not passed, the default login redirect URL that you set in your Dashboard is used. If you have not set a default login redirect URL, an error is returned.

        - `signup_magic_link_url`: The url the user clicks from the sign-up email magic link. This should be a url that your app receives and parses and subsequently send an api request to authenticate the magic link and sign-up the user. If this value is not passed, the default sign-up redirect URL that you set in your Dashboard is used. If you have not set a default sign-up redirect URL, an error is returned.

        - `login_expiration_minutes`: Set the expiration for the login email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

        - `signup_expiration_minutes`: Set the expiration for the sign-up email magic link, in minutes. By default, it expires in 1 week. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

        - `create_user_as_pending`: Flag for whether or not to save a user as pending vs active in Stytch. Defaults to false. If true, new users will be created with status pending in Stytch's backend. Their status will remain pending and they will continue to receive sign-up magic links until a magic link is authenticated for that user. If false, new users will be created with status active. They will receive a sign-up magic link for their first magic link but subsequent magic links will use the login email template, even if the user never authenticated their initial magic link.

        - `locale`: Used to determine which language to use when sending the user this delivery method. Parameter is a two character [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"` or `"es"`.

          Currently supported languages are English (en) and Spanish (es); if no value is provided, the copy defaults to English.

          Request more languages for support [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link)!

        - `attributes`: Provided attributes help with fraud detection.

        - `code_challenge`: A base64url encoded SHA256 hash of a one time secret used to validate that the request starts and ends on the same device.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
        }

        if login_magic_link_url is not None:
            payload["login_magic_link_url"] = login_magic_link_url
        if signup_magic_link_url is not None:
            payload["signup_magic_link_url"] = signup_magic_link_url
        if login_expiration_minutes is not None:
            payload["login_expiration_minutes"] = login_expiration_minutes
        if signup_expiration_minutes is not None:
            payload["signup_expiration_minutes"] = signup_expiration_minutes
        if create_user_as_pending is not None:
            payload["create_user_as_pending"] = create_user_as_pending
        if locale is not None:
            payload["locale"] = locale
        if login_template_id is not None:
            payload["login_template_id"] = login_template_id
        if signup_template_id is not None:
            payload["signup_template_id"] = signup_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "login_or_create")

        res = await self.async_client.post(url, json=payload)
        return LoginOrCreateResponse.from_json(res.response.status, res.json)

    def invite(
        self,
        email: str,
        invite_magic_link_url: Optional[str] = None,
        invite_expiration_minutes: Optional[int] = None,
        name: Optional[Union[Name, Dict[str, str]]] = None,
        locale: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
        invite_template_id: Optional[str] = None,
    ) -> InviteResponse:
        """[Stytch docs](https://stytch.com/docs/api/invite-by-email)

        Create a pending user and send an invite magic link to the provided email. The user will be created with a pending status until they click the magic link in the invite email.

        Parameters:

        - `email`: The email of the user to send the invite magic link to.

        - `invite_magic_link_url`: The url the user clicks from the email magic link. This should be a url that your app receives and parses and subsequently send an api request to authenticate the magic link and log in the user. If this value is not passed, the default invite redirect URL that you set in your Dashboard is used. If you have not set a default invite redirect URL, an error is returned.

        - `invite_expiration_minutes`: Set the expiration for the email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

        - `name`: The name of the user. Each field in the name object is optional.

        - `locale`: Used to determine which language to use when sending the user this delivery method. Parameter is a two character [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"` or `"es"`.

          Currently supported languages are English (en) and Spanish (es); if no value is provided, the copy defaults to English.

          Request more languages for support [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link)!

        - `attributes`: Provided attributes help with fraud detection.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
        }

        if invite_magic_link_url is not None:
            payload["invite_magic_link_url"] = invite_magic_link_url
        if invite_expiration_minutes is not None:
            payload["invite_expiration_minutes"] = invite_expiration_minutes
        if name is not None:
            payload["name"] = (
                name.dict() if isinstance(name, pydantic.BaseModel) else name
            )
        if locale is not None:
            payload["locale"] = locale
        if attributes is not None:
            payload["attributes"] = attributes
        if invite_template_id is not None:
            payload["invite_template_id"] = invite_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "invite")

        res = self.sync_client.post(url, json=payload)
        return InviteResponse.from_json(res.response.status_code, res.json)

    async def invite_async(
        self,
        email: str,
        invite_magic_link_url: Optional[str] = None,
        invite_expiration_minutes: Optional[int] = None,
        name: Optional[Union[Name, Dict[str, str]]] = None,
        locale: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None,
        invite_template_id: Optional[str] = None,
    ) -> InviteResponse:
        """[Stytch docs](https://stytch.com/docs/api/invite-by-email)

        Create a pending user and send an invite magic link to the provided email. The user will be created with a pending status until they click the magic link in the invite email.

        Parameters:

        - `email`: The email of the user to send the invite magic link to.

        - `invite_magic_link_url`: The url the user clicks from the email magic link. This should be a url that your app receives and parses and subsequently send an api request to authenticate the magic link and log in the user. If this value is not passed, the default invite redirect URL that you set in your Dashboard is used. If you have not set a default invite redirect URL, an error is returned.

        - `invite_expiration_minutes`: Set the expiration for the email magic link, in minutes. By default, it expires in 1 hour. The minimum expiration is 5 minutes and the maximum is 7 days (10080 mins).

        - `name`: The name of the user. Each field in the name object is optional.

        - `locale`: Used to determine which language to use when sending the user this delivery method. Parameter is a two character [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"` or `"es"`.

          Currently supported languages are English (en) and Spanish (es); if no value is provided, the copy defaults to English.

          Request more languages for support [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link)!

        - `attributes`: Provided attributes help with fraud detection.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
        }

        if invite_magic_link_url is not None:
            payload["invite_magic_link_url"] = invite_magic_link_url
        if invite_expiration_minutes is not None:
            payload["invite_expiration_minutes"] = invite_expiration_minutes
        if name is not None:
            payload["name"] = (
                name.dict() if isinstance(name, pydantic.BaseModel) else name
            )
        if locale is not None:
            payload["locale"] = locale
        if attributes is not None:
            payload["attributes"] = attributes
        if invite_template_id is not None:
            payload["invite_template_id"] = invite_template_id

        url = self.api_base.route_with_sub_url(self.sub_url, "invite")

        res = await self.async_client.post(url, json=payload)
        return InviteResponse.from_json(res.response.status, res.json)

    def revoke_invite(
        self,
        email: str,
    ) -> RevokeInviteResponse:
        """[Stytch docs](https://stytch.com/docs/api/revoke-pending-invite)

        Revoke a pending invite based on the email provided.

        Parameters:

        - `email`: The email of the user to revoke invite for.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "revoke_invite")

        res = self.sync_client.post(url, json=payload)
        return RevokeInviteResponse.from_json(res.response.status_code, res.json)

    async def revoke_invite_async(
        self,
        email: str,
    ) -> RevokeInviteResponse:
        """[Stytch docs](https://stytch.com/docs/api/revoke-pending-invite)

        Revoke a pending invite based on the email provided.

        Parameters:

        - `email`: The email of the user to revoke invite for.
        """  # noqa

        payload: Dict[str, Any] = {
            "email": email,
        }

        url = self.api_base.route_with_sub_url(self.sub_url, "revoke_invite")

        res = await self.async_client.post(url, json=payload)
        return RevokeInviteResponse.from_json(res.response.status, res.json)
