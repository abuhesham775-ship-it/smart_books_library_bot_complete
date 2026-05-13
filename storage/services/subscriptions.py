from db.models.subscription import Subscription
from schemas.subscription import SubscriptionCreate, SubscriptionRead, SubscriptionUpdate
from services.common import CRUDService

service = CRUDService[Subscription, SubscriptionCreate, SubscriptionUpdate](Subscription)
