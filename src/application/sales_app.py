from src.api.http.http_response import HttpResponse
from src.domain.constants import MESSAGE_BROKER_TYPE
from src.domain.core.sales_core import SalesCore
from src.domain.interfaces.sales_interface import SalesMessageBroker
from src.exceptions.custom_exceptions import RabbitMQError
from src.infrastructure.sales_message_broker_rabbitmq import SalesMessageBrokerRabbitMQ


class SalesApp:
    def __init__(self):
        if MESSAGE_BROKER_TYPE == "rabbitmq":
            self.sales_message_broker: SalesMessageBroker = SalesMessageBrokerRabbitMQ()
        else:
            raise ValueError("Invalid message broker, valid types: rabbitmq")

    def consume_buy(self):
        try:
            sales_core = SalesCore(self.sales_message_broker)
            response = sales_core.consume_buy()
            return HttpResponse.success('Sale started successfully!', response)
        except RabbitMQError as error:
            return HttpResponse.internal_error(message=str(error))
