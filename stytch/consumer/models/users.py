# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import datetime
import enum
from typing import Any, Dict, List, Optional

import pydantic

from stytch.core.response_base import ResponseBase


class SearchUsersQueryOperator(str, enum.Enum):
    OR = "OR"
    AND = "AND"


class BiometricRegistration(pydantic.BaseModel):
    """
    Fields:
      - biometric_registration_id: The unique ID for a biometric registration.
      - verified: The verified boolean denotes whether or not this send method, e.g. phone number, email address, etc., has been successfully authenticated by the User.
    """  # noqa

    biometric_registration_id: str
    verified: bool


class CryptoWallet(pydantic.BaseModel):
    """
    Fields:
      - crypto_wallet_id: The unique ID for a crypto wallet
      - crypto_wallet_address: The actual blockchain address of the User's crypto wallet.
      - crypto_wallet_type: The blockchain that the User's crypto wallet operates on, e.g. Ethereum, Solana, etc.
      - verified: The verified boolean denotes whether or not this send method, e.g. phone number, email address, etc., has been successfully authenticated by the User.
    """  # noqa

    crypto_wallet_id: str
    crypto_wallet_address: str
    crypto_wallet_type: str
    verified: bool


class Email(pydantic.BaseModel):
    """
    Fields:
      - email_id: The unique ID of a specific email address.
      - email: The email address.
      - verified: The verified boolean denotes whether or not this send method, e.g. phone number, email address, etc., has been successfully authenticated by the User.
    """  # noqa

    email_id: str
    email: str
    verified: bool


class Name(pydantic.BaseModel):
    """
    Fields:
      - first_name: The first name of the user.
      - middle_name: The middle name(s) of the user.
      - last_name: The last name of the user.
    """  # noqa

    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None


class OAuthProvider(pydantic.BaseModel):
    """
    Fields:
      - provider_type: Denotes the OAuth identity provider that the user has authenticated with, e.g. Google, Facebook, GitHub etc.
      - provider_subject: The unique identifier for the User within a given OAuth provider. Also commonly called the "sub" or "Subject field" in OAuth protocols.
      - profile_picture_url: If available, the `profile_picture_url` is a url of the User's profile picture set in OAuth identity the provider that the User has authenticated with, e.g. Facebook profile picture.
      - locale: If available, the `locale` is the User's locale set in the OAuth identity provider that the user has authenticated with.
      - oauth_user_registration_id: The unique ID for an OAuth registration.
    """  # noqa

    provider_type: str
    provider_subject: str
    profile_picture_url: str
    locale: str
    oauth_user_registration_id: str


class Password(pydantic.BaseModel):
    """
    Fields:
      - password_id: The unique ID of a specific password
      - requires_reset: Indicates whether this password requires a password reset
    """  # noqa

    password_id: str
    requires_reset: bool


class PhoneNumber(pydantic.BaseModel):
    """
    Fields:
      - phone_id: The unique ID for the phone number.
      - phone_number: The phone number.
      - verified: The verified boolean denotes whether or not this send method, e.g. phone number, email address, etc., has been successfully authenticated by the User.
    """  # noqa

    phone_id: str
    phone_number: str
    verified: bool


class ResultsMetadata(pydantic.BaseModel):
    """
    Fields:
      - total: The total number of results returned by your search query.
      - next_cursor: The `next_cursor` string is returned when your search result contains more than one page of results. This value is passed into your next search call in the `cursor` field.
    """  # noqa

    total: int
    next_cursor: Optional[str] = None


class SearchUsersQuery(pydantic.BaseModel):
    """
    Fields:
      - operator: The action to perform on the operands. The accepted value are:

      `AND` – all the operand values provided must match.

      `OR` – the operator will return any matches to at least one of the operand values you supply.
      - operands: An array of operand objects that contains all of the filters and values to apply to your search search query.
    """  # noqa

    operator: SearchUsersQueryOperator
    operands: List[Dict[str, Any]]


class TOTP(pydantic.BaseModel):
    """
    Fields:
      - totp_id: The unique ID for a TOTP instance.
      - verified: The verified boolean denotes whether or not this send method, e.g. phone number, email address, etc., has been successfully authenticated by the User.
    """  # noqa

    totp_id: str
    verified: bool


class WebAuthnRegistration(pydantic.BaseModel):
    """
    Fields:
      - webauthn_registration_id: The unique ID for the WebAuthn registration.
      - domain: The `domain` on which a WebAuthn registration was started. This will be the domain of your app.
      - user_agent: The user agent of the User.
      - verified: The verified boolean denotes whether or not this send method, e.g. phone number, email address, etc., has been successfully authenticated by the User.
      - authenticator_type: The `authenticator_type` string displays the requested authenticator type of the WebAuthn device. The two valid types are "platform" and "cross-platform". If no value is present, the WebAuthn device was created without an authenticator type preference.
    """  # noqa

    webauthn_registration_id: str
    domain: str
    user_agent: str
    verified: bool
    authenticator_type: str


class User(pydantic.BaseModel):
    """
    Fields:
      - user_id: The unique ID of the affected User.
      - emails: An array of email objects for the User.
      - status: The status of the User. The possible values are `pending` and `active`.
      - phone_numbers: An array of phone number objects linked to the User.
      - webauthn_registrations: An array that contains a list of all WebAuthn registrations for a given User in the Stytch API.
      - providers: An array of OAuth `provider` objects linked to the User.
      - totps: An array containing a list of all TOTP instances for a given User in the Stytch API.
      - crypto_wallets: An array contains a list of all crypto wallets for a given User in the Stytch API.
      - biometric_registrations: An array that contains a list of all biometric registrations for a given User in the Stytch API.
      - name: The name of the User. Each field in the `name` object is optional.
      - created_at: The timestamp of the User's creation. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - password: The password object is returned for users with a password.
      - trusted_metadata: The `trusted_metadata` field contains an arbitrary JSON object of application-specific data. See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
      - untrusted_metadata: The `untrusted_metadata` field contains an arbitrary JSON object of application-specific data. Untrusted metadata can be edited by end users directly via the SDK, and **cannot be used to store critical information.** See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
    """  # noqa

    user_id: str
    emails: List[Email]
    status: str
    phone_numbers: List[PhoneNumber]
    webauthn_registrations: List[WebAuthnRegistration]
    providers: List[OAuthProvider]
    totps: List[TOTP]
    crypto_wallets: List[CryptoWallet]
    biometric_registrations: List[BiometricRegistration]
    name: Optional[Name] = None
    created_at: Optional[datetime.datetime] = None
    password: Optional[Password] = None
    trusted_metadata: Optional[Dict[str, Any]] = None
    untrusted_metadata: Optional[Dict[str, Any]] = None


class CreateResponse(ResponseBase):
    """Response type for `Users.create`.
    Fields:
      - user_id: The unique ID of the affected User.
      - email_id: The unique ID of a specific email address.
      - status: The status of the User. The possible values are `pending` and `active`.
      - phone_id: The unique ID for the phone number.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
    """  # noqa

    user_id: str
    email_id: str
    status: str
    phone_id: str
    user: User


class DeleteBiometricRegistrationResponse(ResponseBase):
    """Response type for `Users.delete_biometric_registration`.
    Fields:
      - user_id: The unique ID of the affected User.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
    """  # noqa

    user_id: str
    user: User


class DeleteCryptoWalletResponse(ResponseBase):
    """Response type for `Users.delete_crypto_wallet`.
    Fields:
      - user_id: The unique ID of the affected User.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
    """  # noqa

    user_id: str
    user: User


class DeleteEmailResponse(ResponseBase):
    """Response type for `Users.delete_email`.
    Fields:
      - user_id: The unique ID of the affected User.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
    """  # noqa

    user_id: str
    user: User


class DeleteOAuthRegistrationResponse(ResponseBase):
    """Response type for `Users.delete_oauth_registration`.
    Fields:
      - user_id: The unique ID of the affected User.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
    """  # noqa

    user_id: str
    user: User


class DeletePasswordResponse(ResponseBase):
    """Response type for `Users.delete_password`.
    Fields:
      - user_id: The unique ID of the affected User.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
    """  # noqa

    user_id: str
    user: User


class DeletePhoneNumberResponse(ResponseBase):
    """Response type for `Users.delete_phone_number`.
    Fields:
      - user_id: The unique ID of the affected User.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
    """  # noqa

    user_id: str
    user: User


class DeleteResponse(ResponseBase):
    """Response type for `Users.delete`.
    Fields:
      - user_id: The unique ID of the deleted User.
    """  # noqa

    user_id: str


class DeleteTOTPResponse(ResponseBase):
    """Response type for `Users.delete_totp`.
    Fields:
      - user_id: The unique ID of the affected User.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
    """  # noqa

    user_id: str
    user: User


class DeleteWebAuthnRegistrationResponse(ResponseBase):
    """Response type for `Users.delete_webauthn_registration`.
    Fields:
      - user_id: The unique ID of the affected User.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
    """  # noqa

    user_id: str
    user: User


class GetResponse(ResponseBase):
    """Response type for `Users.get`.
    Fields:
      - user_id: The unique ID of the returned User.
      - emails: An array of email objects for the User.
      - status: The status of the User. The possible values are `pending` and `active`.
      - phone_numbers: An array of phone number objects linked to the User.
      - webauthn_registrations: An array that contains a list of all WebAuthn registrations for a given User in the Stytch API.
      - providers: An array of OAuth `provider` objects linked to the User.
      - totps: An array containing a list of all TOTP instances for a given User in the Stytch API.
      - crypto_wallets: An array contains a list of all crypto wallets for a given User in the Stytch API.
      - biometric_registrations: An array that contains a list of all biometric registrations for a given User in the Stytch API.
      - name: The name of the User. Each field in the `name` object is optional.
      - created_at: The timestamp of the User's creation. Values conform to the RFC 3339 standard and are expressed in UTC, e.g. `2021-12-29T12:33:09Z`.
      - password: The password object is returned for users with a password.
      - trusted_metadata: The `trusted_metadata` field contains an arbitrary JSON object of application-specific data. See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
      - untrusted_metadata: The `untrusted_metadata` field contains an arbitrary JSON object of application-specific data. Untrusted metadata can be edited by end users directly via the SDK, and **cannot be used to store critical information.** See the [Metadata](https://stytch.com/docs/api/metadata) reference for complete field behavior details.
    """  # noqa

    user_id: str
    emails: List[Email]
    status: str
    phone_numbers: List[PhoneNumber]
    webauthn_registrations: List[WebAuthnRegistration]
    providers: List[OAuthProvider]
    totps: List[TOTP]
    crypto_wallets: List[CryptoWallet]
    biometric_registrations: List[BiometricRegistration]
    name: Optional[Name] = None
    created_at: Optional[datetime.datetime] = None
    password: Optional[Password] = None
    trusted_metadata: Optional[Dict[str, Any]] = None
    untrusted_metadata: Optional[Dict[str, Any]] = None


class SearchResponse(ResponseBase):
    """Response type for `Users.search`.
    Fields:
      - results: An array of results that match your search query.
      - results_metadata: The search `results_metadata` object contains metadata relevant to your specific query like total and `next_cursor`.
    """  # noqa

    results: List[User]
    results_metadata: ResultsMetadata


class UpdateResponse(ResponseBase):
    """Response type for `Users.update`.
    Fields:
      - user_id: The unique ID of the updated User.
      - emails: An array of email objects for the User.
      - phone_numbers: An array of phone number objects linked to the User.
      - crypto_wallets: An array contains a list of all crypto wallets for a given User in the Stytch API.
      - user: The `user` object affected by this API call. See the [Get user endpoint](https://stytch.com/docs/api/get-user) for complete response field details.
    """  # noqa

    user_id: str
    emails: List[Email]
    phone_numbers: List[PhoneNumber]
    crypto_wallets: List[CryptoWallet]
    user: User
