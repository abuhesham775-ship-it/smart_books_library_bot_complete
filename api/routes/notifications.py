from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from api.deps import get_current_user, get_current_user_id, is_admin
from db.session import get_db
from schemas.notification import NotificationCreate, NotificationRead, NotificationUpdate
from services.notifications import service


router = APIRouter()


@router.get('/', response_model=list[NotificationRead])
async def list_items(session: AsyncSession = Depends(get_db), limit: int = Query(default=100, ge=1, le=1000), offset: int = Query(default=0, ge=0)):
    return await service.list(session, limit=limit, offset=offset)


@router.get('/{item_id}', response_model=NotificationRead)
async def get_item(item_id: int, session: AsyncSession = Depends(get_db)):
    item = await service.get(session, item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    return item


@router.post('/', response_model=NotificationRead, status_code=201)
async def create_item(payload: NotificationCreate, session: AsyncSession = Depends(get_db), user_id: int = Depends(get_current_user_id)):

    return await service.create(session, payload)


@router.put('/{item_id}', response_model=NotificationRead)
async def update_item(item_id: int, payload: NotificationUpdate, session: AsyncSession = Depends(get_db), user_id: int = Depends(get_current_user_id)):

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

@router.get('/user/{user_id}', response_model=list[NotificationRead])
async def user_notifications(user_id: int, session: AsyncSession = Depends(get_db)):
    return await service.list(session)

