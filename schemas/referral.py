from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ReferralCodeBase(BaseModel):
    user_id: int
    code: str
    total_uses: int = 0


class ReferralCodeCreate(ReferralCodeBase):
    pass


class ReferralCodeRead(ReferralCodeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ReferralEventBase(BaseModel):
    referrer_id: int
    referred_id: int
    points_awarded: int = 0
    is_completed: bool = False


class ReferralEventCreate(ReferralEventBase):
    pass


class ReferralEventRead(ReferralEventBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
