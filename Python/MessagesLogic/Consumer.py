import pika
from MessagesLogic.configurations_support import *
from MessagesLogic.IncomingMessage import IncomingMessage
from MessagesLogic.ResponseMessage import ResponseMessage
from MessagesLogic.Producer import Producer
from Brainiac.brainiac_caller import ask_a_question


class Consumer:
    def __init__(self, json_queue="Python", settings_path=r"messagingSettings.json"):
        self.json_RabbitMQ = "RabbitMQ"
        self.json_queues_pointer = "Queues"
        self.json_queue = json_queue + "_Request"

        self.settings_path = settings_path
        self.prod_state = find_environment_var()
        self.settings_data = read_json_file(self.settings_path)
        self.rabbit_connection_param = self.settings_data[self.json_RabbitMQ][self.prod_state]
        self.used_queue = self.settings_data[self.json_queues_pointer][self.json_queue]

        self.__open_connection()
        self.channel.queue_declare(queue=self.used_queue)
        self.channel.basic_qos(prefetch_count=1)
        self.receive_message()
        self.__close_connection()

    def __open_connection(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.rabbit_connection_param))
        self.channel = self.connection.channel()

    @staticmethod
    def callback(ch, method, properites, body):
        incomingMessage = IncomingMessage(body.decode())
        answer = ask_a_question(issue=incomingMessage.actual_application,
                                parameters=incomingMessage.actual_parameters)
        responseMessage = ResponseMessage(id=incomingMessage.actual_id,
                                          answer=answer)
        if incomingMessage.actual_id is not None and incomingMessage.actual_platform is not None:
            producer = Producer(message=responseMessage.message,
                                json_queue=incomingMessage.actual_platform)
        else:
            print("One of the key message components is missing.")
        ch.basic_ack(delivery_tag=method.delivery_tag)


    def receive_message(self):
        self.channel.basic_consume(queue=self.used_queue,
                                   on_message_callback=Consumer.callback)
        self.channel.start_consuming()

    def __close_connection(self):
        self.channel.queue_delete(self.used_queue)
        self.channel.close()


if __name__ == "__main__":
    consumer = Consumer()