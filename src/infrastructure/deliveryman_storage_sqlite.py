from src.domain.constants import STORAGE_SQLITE_PATH
from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.service.sqlite import SQLite


class DeliverymanStorageSQLite(SQLite, DeliverymanStorage):
    def __init__(self):
        super(DeliverymanStorageSQLite, self).__init__(STORAGE_SQLITE_PATH)

    def get_available(self):
        get_all_query = "SELECT deliveryman_id FROM deliverymans WHERE available = true ORDER BY RAND() LIMIT 1"

        if deliverymans := self.execute_query_one(get_all_query):
            return deliverymans
        else:
            raise NotFoundFail('Deliveryman not found')
