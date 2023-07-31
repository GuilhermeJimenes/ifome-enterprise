from src.domain.interfaces.deliveries_interface import DeliveriesStorage
from src.domain.models.delivery_model import DeliveryModel
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.config.config_storage import ConfigStorage
from src.infrastructure.service.mysql import MySQL


class DeliveriesStorageMySQL(MySQL, DeliveriesStorage):
    def __init__(self):
        super(DeliveriesStorageMySQL, self).__init__(ConfigStorage)
        self.create_table()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS deliveries ("
            "delivery_id VARCHAR(255) PRIMARY KEY,"
            "client_id VARCHAR(255) NOT NULL,"
            "food_name VARCHAR(255) NOT NULL,"
            "address VARCHAR(255) NOT NULL,"
            "deliveryman_id VARCHAR(255) DEFAULT '',"
            "status VARCHAR(255) DEFAULT ''"
            ")"
        )

        self.execute_query_one(create_table_query)
        self.commit()

    def get_all(self):
        get_available_query = "SELECT * FROM deliveries"

        if deliveries := self.execute_query_many(get_available_query):
            return [DeliveryModel(*delivery) for delivery in deliveries]
        else:
            raise NotFoundFail('Delivery not found')

    def update(self, deliveryman_id, delivery_id):
        update_query = "UPDATE deliveries SET deliveryman_id = %s, status = 'accepted' WHERE delivery_id = %s;"
        update_params = (deliveryman_id, delivery_id)

        self.execute_query_one(update_query, update_params)
        self.commit()
        self.connection_close()
