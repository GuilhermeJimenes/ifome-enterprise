import pika
from pika.exceptions import AMQPConnectionError, AMQPError

from src.domain.constants import HOST_MSG_BROKER
from src.exceptions.custom_exceptions import RabbitMQError


class RabbitMQ:
    def __init__(self):
        self.host = HOST_MSG_BROKER
        self._connection, self._channel = self.connection(self.host)

    def connection(self, host):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host))
            channel = connection.channel()
            return connection, channel
        except AMQPConnectionError as error:
            print(error)
            raise RabbitMQError("Erro ao conectar ao RabbitMQ.") from error

    def channel(self, connection):
        try:
            if not self._channel:
                return connection.channel()
        except AMQPConnectionError as error:
            print(error)
            raise RabbitMQError("Erro ao conectar ao RabbitMQ.") from error

    def new_queue(self, queue_name):
        print(f'nova fila: {queue_name}')
        try:
            self._channel.queue_declare(queue=queue_name)
        except AMQPError as error:
            print(error)
            raise RabbitMQError("Erro ao criar a fila no RabbitMQ.") from error

    def publish(self, queue_name, message):
        try:
            self._channel.basic_publish(exchange='', routing_key=queue_name, body=message)
            print("Mensagem enviada.")
        except AMQPError as error:
            print(error)
            raise RabbitMQError("Erro ao publicar a mensagem no RabbitMQ.") from error

    def consume(self, queue_name, result_queue):
        def callback(ch, method, properties, body, result_queue):
            result_queue.put(body.decode())
            ch.basic_ack(delivery_tag=method.delivery_tag)

        self._channel.basic_consume(
            queue=queue_name, on_message_callback=lambda ch, method, properties, body: callback(
                ch, method, properties, body, result_queue
            )
        )

        try:
            self._channel.start_consuming()
        except KeyboardInterrupt:
            self._channel.stop_consuming()

    def connection_close(self):
        try:
            if self._connection:
                self._connection.close()
                self._connection = None
        except Exception as error:
            print(error)
            raise RabbitMQError("Erro ao fechar conexao com RabbitMQ.") from error
