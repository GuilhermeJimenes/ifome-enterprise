from src.domain.interfaces.deliveries_interface import DeliveriesStorage
from src.infrastructure.config.config_storage import ConfigStorage
from src.infrastructure.service.mysql import MySQL


class DeliveriesStorageMySQL(MySQL, DeliveriesStorage):
    def __init__(self):
        super(DeliveriesStorageMySQL, self).__init__(ConfigStorage)

    def update(self, deliveryman_id, delivery_id):
        update_query = "UPDATE deliveries SET deliveryman_id = %s WHERE delivery_id = %s"
        update_params = (deliveryman_id, delivery_id)

        self.execute_query_one(update_query, update_params)
        self.commit()
        self.connection_close()
