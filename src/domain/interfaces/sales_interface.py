class SalesMessageBroker:
    def change_status(self, message):
        raise NotImplementedError()

    def consume_buy(self, result_queue):
        raise NotImplementedError()

    def connection_close(self):
        raise NotImplementedError()
