import pika
from MessagesLogic.configurations_support import *


class Producer:
    def __init__(self, message, json_queue="Python", settings_path=r"messagingSettings.json"):
        self.json_RabbitMQ = "RabbitMQ"
        self.json_queues_pointer = "Queues"
        self.json_queue = json_queue + "_Response"

        self.message = message
        self.settings_path = settings_path
        self.prod_state = find_environment_var()
        self.settings_data = read_json_file(self.settings_path)
        self.rabbit_connection_param = self.settings_data[self.json_RabbitMQ][self.prod_state]
        self.used_queue = self.settings_data[self.json_queues_pointer][self.json_queue]

        self.__open_connection()
        self.channel.queue_declare(queue=self.used_queue)
        self.send_message()
        self.__close_connection()

    def __open_connection(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.rabbit_connection_param))
        self.channel = self.connection.channel()

    def send_message(self):
        self.channel.basic_publish(exchange="",
                                   routing_key=self.used_queue,
                                   body=self.message,
                                   properties=pika.BasicProperties(delivery_mode=2))  # Makes messages persistent

    def __close_connection(self):
        self.channel.close()
