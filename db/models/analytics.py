from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import Base, TimestampMixin


class AnalyticsEvent(Base, TimestampMixin):
    __tablename__ = 'analytics_events'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int | None] = mapped_column(ForeignKey('users.id', ondelete='SET NULL'), nullable=True, index=True)
    event_name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    payload: Mapped[str | None] = mapped_column(Text, nullable=True)

    user = relationship('User', back_populates='analytics')
