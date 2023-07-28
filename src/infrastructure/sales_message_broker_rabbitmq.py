from src.domain.constants import BUY_QUEUE, DELIVERY_QUEUE
from src.domain.interfaces.sales_interface import SalesMessageBroker
from src.infrastructure.service.rabbitmq import RabbitMQ


class SalesMessageBrokerRabbitMQ(RabbitMQ, SalesMessageBroker):
    buy_queue = BUY_QUEUE
    delivery_queue = DELIVERY_QUEUE

    def notify_deliveryman(self, message):
        self.new_queue(self.delivery_queue)
        self.publish(self.delivery_queue, message)

    def consume_buy(self, result_queue):
        self.consume(self.buy_queue, result_queue)
