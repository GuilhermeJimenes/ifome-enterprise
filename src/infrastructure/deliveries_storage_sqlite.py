from src.domain.constants import STORAGE_SQLITE_PATH
from src.domain.interfaces.deliveries_interface import DeliveriesStorage
from src.infrastructure.service.sqlite import SQLite


class DeliveriesStorageSQLite(SQLite, DeliveriesStorage):
    def __init__(self):
        super(DeliveriesStorageSQLite, self).__init__(STORAGE_SQLITE_PATH)

    def update(self, deliveryman_id, delivery_id):
        update_quey = "UPDATE deliveries SET deliveryman_id = %s WHERE delivery_id = %s"
        update_params = (deliveryman_id, delivery_id)

        self.execute_query_one(update_quey, update_params)
        self.commit()
