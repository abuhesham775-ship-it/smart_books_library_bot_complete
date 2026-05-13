from db.models.notification import Notification
from schemas.notification import NotificationCreate, NotificationRead, NotificationUpdate
from services.common import CRUDService

service = CRUDService[Notification, NotificationCreate, NotificationUpdate](Notification)
