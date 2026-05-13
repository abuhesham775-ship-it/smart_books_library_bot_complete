from __future__ import annotations

from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    telegram_id: Mapped[int | None] = mapped_column(Integer, unique=True, index=True, nullable=True)
    username: Mapped[str | None] = mapped_column(String(100), index=True, nullable=True)
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    points: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_premium: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    referral_code: Mapped[str | None] = mapped_column(String(50), unique=True, index=True, nullable=True)

    point_transactions = relationship('PointTransaction', back_populates='user', cascade='all, delete-orphan')
    reviews = relationship('Review', back_populates='user', cascade='all, delete-orphan')
    subscriptions = relationship('Subscription', back_populates='user', cascade='all, delete-orphan')
    referral_codes = relationship('ReferralCode', back_populates='user', cascade='all, delete-orphan')
    analytics = relationship('AnalyticsEvent', back_populates='user', cascade='all, delete-orphan')
    challenge_participations = relationship('ChallengeParticipation', back_populates='user', cascade='all, delete-orphan')
    notifications = relationship('Notification', back_populates='user', cascade='all, delete-orphan')
    social_posts = relationship('SocialPost', back_populates='user', cascade='all, delete-orphan')
