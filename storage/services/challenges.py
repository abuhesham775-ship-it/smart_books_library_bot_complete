from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.challenge import Challenge, ChallengeParticipation
from schemas.challenge import ChallengeCreate, ChallengeParticipationCreate, ChallengeParticipationRead, ChallengeRead, ChallengeUpdate
from services.common import CRUDService


class ChallengeService(CRUDService[Challenge, ChallengeCreate, ChallengeUpdate]):
    async def active(self, session: AsyncSession):
        stmt = select(Challenge).where(Challenge.is_active.is_(True))
        result = await session.execute(stmt)
        return result.scalars().all()

    async def join(self, session: AsyncSession, challenge_id: int, user_id: int):
        stmt = select(ChallengeParticipation).where(
            ChallengeParticipation.challenge_id == challenge_id,
            ChallengeParticipation.user_id == user_id,
        )
        result = await session.execute(stmt)
        participation = result.scalar_one_or_none()
        if participation:
            return participation
        participation = ChallengeParticipation(challenge_id=challenge_id, user_id=user_id)
        session.add(participation)
        await session.commit()
        await session.refresh(participation)
        return participation

    async def claim(self, session: AsyncSession, participation: ChallengeParticipation):
        challenge = await session.get(Challenge, participation.challenge_id)
        if not challenge:
            return participation
        participation.is_completed = True
        await session.commit()
        await session.refresh(participation)
        return participation


service = ChallengeService(Challenge)
