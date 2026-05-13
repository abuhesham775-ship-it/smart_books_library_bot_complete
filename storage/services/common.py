from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import delete, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

ModelT = TypeVar('ModelT', bound=DeclarativeBase)
CreateT = TypeVar('CreateT', bound=BaseModel)
UpdateT = TypeVar('UpdateT', bound=BaseModel)


class CRUDService(Generic[ModelT, CreateT, UpdateT]):
    def __init__(self, model: type[ModelT]):
        self.model = model

    async def list(self, session: AsyncSession, limit: int = 100, offset: int = 0):
        stmt = select(self.model).limit(limit).offset(offset)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def count(self, session: AsyncSession) -> int:
        stmt = select(func.count()).select_from(self.model)
        result = await session.execute(stmt)
        return int(result.scalar_one())

    async def get(self, session: AsyncSession, item_id: int):
        return await session.get(self.model, item_id)

    async def create(self, session: AsyncSession, obj_in: CreateT):
        obj = self.model(**obj_in.model_dump())
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def update(self, session: AsyncSession, db_obj: ModelT, obj_in: UpdateT):
        data = obj_in.model_dump(exclude_unset=True)
        for field, value in data.items():
            setattr(db_obj, field, value)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def delete(self, session: AsyncSession, db_obj: ModelT):
        await session.delete(db_obj)
        await session.commit()
        return True
