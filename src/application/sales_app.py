from src.domain.constants import MESSAGE_BROKER_TYPE, STORAGE_TYPE
from src.domain.core.sales_core import SalesCore
from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.domain.interfaces.deliveries_interface import DeliveriesStorage
from src.domain.interfaces.sales_interface import SalesMessageBroker
from src.exceptions.custom_exceptions import RabbitMQError, NotFoundFail
from src.infrastructure.deliveryman_storage_mysql import DeliverymanStorageMySQL
from src.infrastructure.deliveryman_storage_sqlite import DeliverymanStorageSQLite
from src.infrastructure.deliveries_storage_mysql import DeliveriesStorageMySQL
from src.infrastructure.deliveries_storage_sqlite import DeliveriesStorageSQLite
from src.infrastructure.sales_message_broker_rabbitmq import SalesMessageBrokerRabbitMQ


class SalesApp:
    def __init__(self):
        if STORAGE_TYPE == "mysql":
            self.deliveryman_storage: DeliverymanStorage = DeliverymanStorageMySQL()
            self.deliveries_storage: DeliveriesStorage = DeliveriesStorageMySQL()
        elif STORAGE_TYPE == "sqlite":
            self.deliveryman_storage: DeliverymanStorage = DeliverymanStorageSQLite()
            self.deliveries_storage: DeliveriesStorage = DeliveriesStorageSQLite()
        else:
            raise ValueError("Invalid storage, valid types: sqlite, mysql")

        if MESSAGE_BROKER_TYPE == "rabbitmq":
            self.sales_message_broker: SalesMessageBroker = SalesMessageBrokerRabbitMQ()
        else:
            raise ValueError("Invalid message broker, valid types: rabbitmq")

    def sales(self):
        try:
            sales_core = SalesCore(self.deliveryman_storage, self.deliveries_storage, self.sales_message_broker)
            response = sales_core.sales()
            self.sales_message_broker.consume_success()
            return response
        except NotFoundFail as error:
            print(error)
            return 'error'
        except KeyboardInterrupt as error:
            print(error)
            return 'error'
        except RabbitMQError as error:
            print(error)
            self.sales_message_broker.close_connection()
            return 'error'
