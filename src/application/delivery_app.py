from src.api.http.http_response import HttpResponse
from src.domain.constants import STORAGE_TYPE
from src.domain.core.delivery_core import DeliveryCore
from src.domain.interfaces.deliveries_interface import DeliveriesStorage
from src.exceptions.custom_exceptions import NotFoundFail
from src.infrastructure.deliveries_storage_mysql import DeliveriesStorageMySQL
from src.infrastructure.deliveries_storage_sqlite import DeliveriesStorageSQLite


class DeliveryApp:
    def __init__(self):
        if STORAGE_TYPE == "mysql":
            self.deliveries_storage: DeliveriesStorage = DeliveriesStorageMySQL()
        elif STORAGE_TYPE == "sqlite":
            self.deliveries_storage: DeliveriesStorage = DeliveriesStorageSQLite()
        else:
            raise ValueError("Invalid storage, valid types: sqlite, mysql")

    def get_all(self):
        try:
            delivery_core = DeliveryCore(self.deliveries_storage)
            response = [delivery.__dict__ for delivery in delivery_core.get_all()]
            return HttpResponse.success('Delivery successfully found!', response)
        except NotFoundFail as error:
            return HttpResponse.internal_error(message=str(error))
