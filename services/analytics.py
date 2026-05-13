from db.models.analytics import AnalyticsEvent
from schemas.analytics import AnalyticsEventCreate, AnalyticsEventRead
from services.common import CRUDService

service = CRUDService[AnalyticsEvent, AnalyticsEventCreate, AnalyticsEventRead](AnalyticsEvent)
