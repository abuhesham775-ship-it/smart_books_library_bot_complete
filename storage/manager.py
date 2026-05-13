from __future__ import annotations

from pathlib import Path

from storage.files import ensure_dir


class StorageManager:
    def __init__(self, root: str = 'storage_data'):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def books_dir(self) -> Path:
        return ensure_dir('books')
