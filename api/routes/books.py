from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from api.deps import get_current_user, get_current_user_id, is_admin
from db.session import get_db
from schemas.book import BookCreate, BookRead, BookUpdate
from services.books import service
from schemas.category import CategoryRead
from services.categories import service as category_service


router = APIRouter()


@router.get('/', response_model=list[BookRead])
async def list_items(session: AsyncSession = Depends(get_db), limit: int = Query(default=100, ge=1, le=1000), offset: int = Query(default=0, ge=0)):
    return await service.list(session, limit=limit, offset=offset)


@router.get('/{item_id}', response_model=BookRead)
async def get_item(item_id: int, session: AsyncSession = Depends(get_db)):
    item = await service.get(session, item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    return item


@router.post('/', response_model=BookRead, status_code=201)
async def create_item(payload: BookCreate, session: AsyncSession = Depends(get_db), user_id: int = Depends(get_current_user_id)):

    return await service.create(session, payload)


@router.put('/{item_id}', response_model=BookRead)
async def update_item(item_id: int, payload: BookUpdate, session: AsyncSession = Depends(get_db), user_id: int = Depends(get_current_user_id)):

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

@router.get('/search/', response_model=list[BookRead])
async def search_books(q: str, session: AsyncSession = Depends(get_db)):
    return await service.search(session, q)


@router.get('/category/{category_id}', response_model=list[BookRead])
async def books_by_category(category_id: int, session: AsyncSession = Depends(get_db)):
    return await service.list_by_category(session, category_id)


@router.post('/{book_id}/view', response_model=BookRead)
async def view_book(book_id: int, session: AsyncSession = Depends(get_db)):
    item = await service.get(session, book_id)
    if not item:
        raise HTTPException(status_code=404, detail='Book not found')
    return await service.increment_views(session, item)


@router.post('/{book_id}/download', response_model=BookRead)
async def download_book(book_id: int, session: AsyncSession = Depends(get_db)):
    item = await service.get(session, book_id)
    if not item:
        raise HTTPException(status_code=404, detail='Book not found')
    return await service.increment_downloads(session, item)


@router.get('/categories/', response_model=list[CategoryRead])
async def list_categories(session: AsyncSession = Depends(get_db)):
    return await category_service.list(session)

