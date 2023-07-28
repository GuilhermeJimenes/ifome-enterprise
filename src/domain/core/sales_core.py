from src.domain.interfaces.sales_interface import SalesMessageBroker


class SalesCore:
    def __init__(self, sales_message_broker: SalesMessageBroker):
        self.sales_message_broker = sales_message_broker

    def consume_buy(self):
        self.sales_message_broker.consume_buy()
        self.sales_message_broker.connection_close()
