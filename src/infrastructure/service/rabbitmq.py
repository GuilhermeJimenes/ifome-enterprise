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

    def consume(self, queue_name):
        def callback(ch, method, properties, body):
            print(f" [x] Mensagem recebida: {body.decode('utf-8')}")

        try:
            self._channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
            print(' [*] Aguardando mensagens. Pressione CTRL+C para sair.')
            self._channel.start_consuming()
        except AMQPError as error:
            print(error)
            raise RabbitMQError("Erro ao consumir mensagens do RabbitMQ.") from error

    def connection_close(self):
        try:
            if self._connection:
                self._connection.close()
                self._connection = None
        except Exception as error:
            print(error)
            raise RabbitMQError("Erro ao fechar conexao com RabbitMQ.") from error
