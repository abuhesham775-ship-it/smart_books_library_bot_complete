from __future__ import annotations

from pathlib import Path

BASE_STORAGE = Path('storage_data')
BASE_STORAGE.mkdir(exist_ok=True)


def ensure_dir(name: str) -> Path:
    path = BASE_STORAGE / name
    path.mkdir(parents=True, exist_ok=True)
    return path
