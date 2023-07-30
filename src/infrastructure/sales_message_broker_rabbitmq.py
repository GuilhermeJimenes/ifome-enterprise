from src.domain.constants import BUY_QUEUE, DELIVERY_QUEUE
from src.domain.interfaces.sales_interface import SalesMessageBroker
from src.infrastructure.service.rabbitmq import RabbitMQ


class SalesMessageBrokerRabbitMQ(RabbitMQ, SalesMessageBroker):
    def publish_deliveryman(self, message):
        self.new_queue(DELIVERY_QUEUE)
        self.publish(DELIVERY_QUEUE, message)

    def consume_buy(self):
        return self.start_consuming(BUY_QUEUE)
