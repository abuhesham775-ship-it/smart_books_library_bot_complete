from db.models.referral import ReferralCode, ReferralEvent
from schemas.referral import ReferralCodeCreate, ReferralCodeRead, ReferralEventCreate, ReferralEventRead
from services.common import CRUDService

code_service = CRUDService[ReferralCode, ReferralCodeCreate, ReferralCodeRead](ReferralCode)
event_service = CRUDService[ReferralEvent, ReferralEventCreate, ReferralEventRead](ReferralEvent)
