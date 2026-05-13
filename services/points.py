from db.models.point import PointTransaction
from schemas.point import PointTransactionCreate, PointTransactionRead
from services.common import CRUDService

service = CRUDService[PointTransaction, PointTransactionCreate, PointTransactionRead](PointTransaction)
