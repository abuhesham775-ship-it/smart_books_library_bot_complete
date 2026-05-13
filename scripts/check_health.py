from __future__ import annotations

import asyncio

from api.main import app


async def main():
    print(app.title)


if __name__ == '__main__':
    asyncio.run(main())
