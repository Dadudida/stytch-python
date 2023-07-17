# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

import pydantic

from stytch.b2b.models.organizations import Member, Organization


class Membership(pydantic.BaseModel):
    """
    Fields:
      - type: Either `active_member`, `pending_member`, `invited_member`, or `eligible_to_join_by_email_domain`
      - details: An object containing additional metadata about the membership, if available.
      - member: The [Member object](https://stytch.com/docs/b2b/api/member-object) if one already exists, or null if one does not.
    """  # noqa

    type: str
    details: Optional[Dict[str, Any]] = None
    member: Optional[Member] = None


class DiscoveredOrganization(pydantic.BaseModel):
    """
    Fields:
      - member_authenticated: Indicates whether or not the discovery magic link initiated session is valid for the organization's allowed auth method settings.
      If not, the member needs to perform additional authentication before logging in - such as password or SSO auth.
      - organization: The [Organization object](https://stytch.com/docs/b2b/api/organization-object).
      - membership: Information about the membership.
    """  # noqa

    member_authenticated: bool
    organization: Optional[Organization] = None
    membership: Optional[Membership] = None
