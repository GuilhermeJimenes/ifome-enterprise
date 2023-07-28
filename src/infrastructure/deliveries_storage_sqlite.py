from src.domain.constants import STORAGE_SQLITE_PATH
from src.domain.interfaces.deliveries_interface import DeliveriesStorage
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.service.sqlite import SQLite


class DeliveriesStorageSQLite(SQLite, DeliveriesStorage):
    def __init__(self):
        super(DeliveriesStorageSQLite, self).__init__(STORAGE_SQLITE_PATH)

    def get_all(self):
        get_available_query = "SELECT * FROM deliveries"

        if deliverymans := self.execute_query_many(get_available_query):
            return deliverymans
        else:
            raise NotFoundFail('Delivery not found')

    def update(self, deliveryman_id, delivery_id):
        update_quey = "UPDATE deliveries SET deliveryman_id = %s, status = 'accepted' WHERE delivery_id = %s;"
        update_params = (deliveryman_id, delivery_id)

        self.execute_query_one(update_quey, update_params)
        self.commit()
