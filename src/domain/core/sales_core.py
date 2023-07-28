import queue
import threading

from src.domain.interfaces.deliveryman_interface import DeliverymanStorage
from src.domain.interfaces.deliveries_interface import DeliveriesStorage
from src.domain.interfaces.sales_interface import SalesMessageBroker


class SalesCore:
    def __init__(self, deliveryman_storage: DeliverymanStorage, deliveries_storage: DeliveriesStorage, sales_message_broker: SalesMessageBroker):
        self.deliveryman_storage = deliveryman_storage
        self.deliveries_storage = deliveries_storage
        self.sales_message_broker = sales_message_broker

    def get_delivery_id(self):
        result_queue = queue.Queue()
        thread = threading.Thread(target=self.sales_message_broker.consume_buy, args=(result_queue,))
        thread.daemon = True
        thread.start()

        try:
            return result_queue.get(timeout=5)
        except queue.Empty:
            print("Looking for sales.")

    def get_deliveryman_id(self):
        return self.deliveryman_storage.get_available()[0]

    def update_delivery(self, deliveryman_id, delivery_id):
        if deliveryman_id and delivery_id:
            self.deliveries_storage.update(deliveryman_id, delivery_id)

    def update_deliveryman(self):
        pass
        # definir entregador como ocupado

    def sales(self):
        delivery_id = self.get_delivery_id()
        deliveryman_id = self.get_deliveryman_id()
        self.update_delivery(deliveryman_id, delivery_id)
        return delivery_id
