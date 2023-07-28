from src.domain.interfaces.deliveries_interface import DeliveriesStorage


class DeliveryCore:
    def __init__(self, deliveries_storage: DeliveriesStorage):
        self.deliveries_storage = deliveries_storage

    def get_deliveries(self):
        return self.deliveries_storage.get_all()

    def get_all(self):
        return self.get_deliveries()

