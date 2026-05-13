from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from api.deps import get_current_user, get_current_user_id, is_admin
from db.session import get_db
from schemas.social import SocialCommentCreate, SocialCommentRead, SocialPostCreate, SocialPostRead
from services.social import comment_service, post_service

router = APIRouter()


@router.get('/posts/', response_model=list[SocialPostRead])
async def list_posts(session: AsyncSession = Depends(get_db)):
    return await post_service.list(session)


@router.get('/posts/{post_id}', response_model=SocialPostRead)
async def get_post(post_id: int, session: AsyncSession = Depends(get_db)):
    post = await post_service.get(session, post_id)
    if not post:
        raise HTTPException(status_code=404, detail='Item not found')
    return post


@router.post('/posts/', response_model=SocialPostRead, status_code=201)
async def create_post(payload: SocialPostCreate, session: AsyncSession = Depends(get_db)):
    return await post_service.create(session, payload)


@router.post('/comments/', response_model=SocialCommentRead)
async def create_comment(payload: SocialCommentCreate, session: AsyncSession = Depends(get_db)):
    return await comment_service.create(session, payload)
