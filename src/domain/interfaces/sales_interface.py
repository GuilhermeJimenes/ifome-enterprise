class SalesMessageBroker:
    def notify_deliveryman(self, message):
        raise NotImplementedError()

    def consume_buy(self):
        raise NotImplementedError()

    def consume_success(self):
        raise NotImplementedError()

    def close_connection(self):
        raise NotImplementedError()
