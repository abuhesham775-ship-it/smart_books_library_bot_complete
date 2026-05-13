from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ChallengeBase(BaseModel):
    title: str
    description: str | None = None
    reward_points: int = 0
    is_active: bool = True
    target_value: int = 1


class ChallengeCreate(ChallengeBase):
    pass


class ChallengeUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    reward_points: int | None = None
    is_active: bool | None = None
    target_value: int | None = None


class ChallengeRead(ChallengeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ChallengeParticipationBase(BaseModel):
    challenge_id: int
    user_id: int
    progress: int = 0
    is_completed: bool = False


class ChallengeParticipationCreate(ChallengeParticipationBase):
    pass


class ChallengeParticipationRead(ChallengeParticipationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
