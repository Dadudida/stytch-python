# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

import enum
from typing import Optional

from stytch.b2b.models.organizations import Member, Organization
from stytch.b2b.models.sessions import MemberSession
from stytch.core.response_base import ResponseBase


class ResetStartRequestLocale(enum.Enum):
    EN = "en"
    ES = "es"
    PTBR = "pt-br"


class ResetResponse(ResponseBase):
    """Response type for `Email.reset`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member_email_id: Globally unique UUID that identifies a member's email
      - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object).
      - session_token: A secret token for a given Stytch Session.
      - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - member_session: The [Session object](https://stytch.com/docs/b2b/api/session-object).
    """  # noqa

    member_id: str
    member_email_id: str
    organization_id: str
    member: Member
    session_token: str
    session_jwt: str
    organization: Organization
    member_session: Optional[MemberSession] = None


class ResetStartResponse(ResponseBase):
    """Response type for `Email.reset_start`.
    Fields:
      - member_id: Globally unique UUID that identifies a specific Member.
      - member_email_id: Globally unique UUID that identifies a member's email
    """  # noqa

    member_id: str
    member_email_id: str
