class SalesMessageBroker:
    def change_status(self, message):
        raise NotImplementedError()

    def consume_buy(self):
        raise NotImplementedError()

    def connection_close(self):
        raise NotImplementedError()
