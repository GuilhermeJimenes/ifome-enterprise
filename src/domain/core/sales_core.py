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
        else:
            print(deliveryman_id)
            print(delivery_id)

    def update_deliveryman(self, deliveryman_id):
        if deliveryman_id:
            return self.deliveryman_storage.update(deliveryman_id)
        else:
            print(deliveryman_id)

    def send_delivery(self, delivery_id):
        if delivery_id:
            self.sales_message_broker.notify_deliveryman(delivery_id)
        else:
            print(delivery_id)

    def sales(self):
        delivery_id = self.get_delivery_id()
        deliveryman_id = self.get_deliveryman_id()
        self.update_delivery(deliveryman_id, delivery_id)
        self.update_deliveryman(deliveryman_id)
        self.send_delivery(delivery_id)
        return delivery_id
