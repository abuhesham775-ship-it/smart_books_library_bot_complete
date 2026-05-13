from db.models.review import Review
from schemas.review import ReviewCreate, ReviewRead, ReviewUpdate
from services.common import CRUDService

service = CRUDService[Review, ReviewCreate, ReviewUpdate](Review)
