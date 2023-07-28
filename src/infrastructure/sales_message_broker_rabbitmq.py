from src.domain.constants import BUY_QUEUE
from src.domain.interfaces.sales_interface import SalesMessageBroker
from src.infrastructure.service.rabbitmq import RabbitMQ


class SalesMessageBrokerRabbitMQ(RabbitMQ, SalesMessageBroker):
    queue_name = BUY_QUEUE

    def change_status(self, message):
        self.new_queue(self.queue_name)
        self.publish(self.queue_name, message)

    def consume_buy(self):
        self.new_queue(self.queue_name)
        self.consume(self.queue_name)
