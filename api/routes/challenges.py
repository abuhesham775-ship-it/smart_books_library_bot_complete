from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from api.deps import get_current_user, get_current_user_id, is_admin
from db.session import get_db
from schemas.challenge import ChallengeCreate, ChallengeParticipationCreate, ChallengeParticipationRead, ChallengeRead, ChallengeUpdate
from services.challenges import service


router = APIRouter()


@router.get('/', response_model=list[ChallengeRead])
async def list_items(session: AsyncSession = Depends(get_db), limit: int = Query(default=100, ge=1, le=1000), offset: int = Query(default=0, ge=0)):
    return await service.list(session, limit=limit, offset=offset)


@router.get('/{item_id}', response_model=ChallengeRead)
async def get_item(item_id: int, session: AsyncSession = Depends(get_db)):
    item = await service.get(session, item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    return item


@router.post('/', response_model=ChallengeRead, status_code=201)
async def create_item(payload: ChallengeCreate, session: AsyncSession = Depends(get_db), user_id: int = Depends(get_current_user_id)):

    return await service.create(session, payload)


@router.put('/{item_id}', response_model=ChallengeRead)
async def update_item(item_id: int, payload: ChallengeUpdate, session: AsyncSession = Depends(get_db), user_id: int = Depends(get_current_user_id)):

    item = await service.get(session, item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    return await service.update(session, item, payload)


@router.delete('/{item_id}')
async def delete_item(item_id: int, session: AsyncSession = Depends(get_db), user_id: int = Depends(get_current_user_id)):

    item = await service.get(session, item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    await service.delete(session, item)
    return {'status': 'deleted'}

@router.get('/active/', response_model=list[ChallengeRead])
async def active(session: AsyncSession = Depends(get_db)):
    return await service.active(session)


@router.post('/{challenge_id}/join', response_model=ChallengeParticipationRead)
async def join(challenge_id: int, user_id: int, session: AsyncSession = Depends(get_db)):
    return await service.join(session, challenge_id, user_id)


@router.post('/participations/{participation_id}/claim', response_model=ChallengeParticipationRead)
async def claim(participation_id: int, session: AsyncSession = Depends(get_db)):
    participation = await session.get(__import__('db.models.challenge', fromlist=['ChallengeParticipation']).ChallengeParticipation, participation_id)
    if not participation:
        raise HTTPException(status_code=404, detail='Participation not found')
    return await service.claim(session, participation)

