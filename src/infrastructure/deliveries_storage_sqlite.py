from src.domain.constants import STORAGE_SQLITE_PATH
from src.domain.interfaces.deliveries_interface import DeliveriesStorage
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.service.sqlite import SQLite


class DeliveriesStorageSQLite(SQLite, DeliveriesStorage):
    def __init__(self):
        super(DeliveriesStorageSQLite, self).__init__(STORAGE_SQLITE_PATH)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS deliveries ("
            "delivery_id TEXT PRIMARY KEY,"
            "client_id TEXT,"
            "food_name TEXT NOT NULL,"
            "address TEXT NOT NULL,"
            "deliveryman_id TEXT DEFAULT '',"
            "status TEXT DEFAULT ''"
            ")"
        )

        self.execute_query_one(create_table_query)

    def get_all(self):
        get_available_query = "SELECT * FROM deliveries"

        if deliverymans := self.execute_query_many(get_available_query):
            return deliverymans
        else:
            raise NotFoundFail('Delivery not found')

    def update(self, deliveryman_id, delivery_id):
        update_query = "UPDATE deliveries SET deliveryman_id = %s, status = 'accepted' WHERE delivery_id = %s;"
        update_params = (deliveryman_id, delivery_id)

        self.execute_query_one(update_query, update_params)
        self.commit()
