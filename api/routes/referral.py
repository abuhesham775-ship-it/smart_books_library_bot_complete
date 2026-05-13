from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from api.deps import get_current_user, get_current_user_id, is_admin
from db.session import get_db
from schemas.referral import ReferralCodeCreate, ReferralCodeRead, ReferralEventCreate, ReferralEventRead
from services.referral import code_service, event_service

router = APIRouter()


@router.get('/codes/', response_model=list[ReferralCodeRead])
async def list_codes(session: AsyncSession = Depends(get_db)):
    return await code_service.list(session)


@router.post('/codes/', response_model=ReferralCodeRead, status_code=201)
async def create_code(payload: ReferralCodeCreate, session: AsyncSession = Depends(get_db)):
    return await code_service.create(session, payload)


@router.get('/events/', response_model=list[ReferralEventRead])
async def list_events(session: AsyncSession = Depends(get_db)):
    return await event_service.list(session)


@router.post('/events/', response_model=ReferralEventRead)
async def create_event(payload: ReferralEventCreate, session: AsyncSession = Depends(get_db)):
    return await event_service.create(session, payload)
