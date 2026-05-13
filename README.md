# Smart Books Library Bot

مشروع مكتبة رقمية ذكية عبر FastAPI + Aiogram + SQLAlchemy + Redis.

## التشغيل المحلي

1. انسخ `.env.example` إلى `.env`
2. عدّل القيم الأساسية
3. ثبّت المتطلبات:

```bash
pip install -r requirements.txt
```

4. شغّل الـ API:

```bash
uvicorn api.main:app --reload
```

5. شغّل البوت:

```bash
python -m bot.main
```

## Docker

```bash
docker compose up --build
```

## ملاحظات

- الإعداد الافتراضي يستخدم SQLite محليًا حتى يعمل المشروع فورًا بدون تعقيدات.
- عند وضع `DATABASE_URL` إلى PostgreSQL سيعمل بنفس الواجهات.
- الجداول تُنشأ تلقائيًا عند تشغيل الـ API لأول مرة.
