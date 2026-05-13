from aiogram import Router

from bot.handlers.admin import router as admin_router
from bot.handlers.books.details import router as books_details_router
from bot.handlers.books.search import router as books_search_router
from bot.handlers.books.send import router as books_send_router
from bot.handlers.books.upload import router as books_upload_router
from bot.handlers.challenges.claim import router as challenge_claim_router
from bot.handlers.challenges.join import router as challenge_join_router
from bot.handlers.challenges.list import router as challenge_list_router
from bot.handlers.help import router as help_router
from bot.handlers.notifications import router as notifications_router
from bot.handlers.others import router as others_router
from bot.handlers.referral import router as referral_router
from bot.handlers.start import router as start_router
from bot.handlers.users.achievements import router as achievements_router
from bot.handlers.users.points import router as user_points_router
from bot.handlers.users.profile import router as user_profile_router
from bot.handlers.users.subscriptions import router as user_subscriptions_router

router = Router()
for child in [
    start_router, help_router, books_search_router, books_details_router, books_send_router,
    books_upload_router, user_profile_router, user_points_router, achievements_router,
    user_subscriptions_router, challenge_list_router, challenge_join_router, challenge_claim_router,
    notifications_router, referral_router, admin_router, others_router,
]:
    router.include_router(child)
