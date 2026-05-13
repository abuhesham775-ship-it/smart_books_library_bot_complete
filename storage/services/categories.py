from db.models.category import Category
from schemas.category import CategoryCreate, CategoryRead, CategoryUpdate
from services.common import CRUDService

service = CRUDService[Category, CategoryCreate, CategoryUpdate](Category)
