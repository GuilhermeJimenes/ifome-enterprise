from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.config.config_storage import ConfigStorage
from src.infrastructure.service.mysql import MySQL


class DeliverymanStorageMySQL(MySQL, DeliverymanStorage):
    def __init__(self):
        super(DeliverymanStorageMySQL, self).__init__(ConfigStorage)

    def get_available(self):
        get_all_query = "SELECT deliveryman_id FROM deliverymans WHERE available = true ORDER BY RAND() LIMIT 1"

        if deliverymans := self.execute_query_one(get_all_query):
            return deliverymans
        else:
            raise NotFoundFail('Deliveryman not found')
