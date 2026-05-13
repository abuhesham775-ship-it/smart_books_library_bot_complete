from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def clamp(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(maximum, value))


def paginate(items: list[Any], page: int = 1, page_size: int = 10):
    page = max(1, page)
    page_size = max(1, page_size)
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end], len(items)


def normalize_query(value: str) -> str:
    return ' '.join(value.strip().lower().split())
