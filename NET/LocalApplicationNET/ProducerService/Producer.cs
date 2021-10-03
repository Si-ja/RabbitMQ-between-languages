using System.Text;
using System;
using RabbitMQ.Client;

namespace ProducerService
{
    public class Producer
    {
        public static void SendMessage(string environmnet, string message)
        {
            var factory = new ConnectionFactory() { HostName = environmnet };
            string usedQueue = "Python_Request";
            using (var connection = factory.CreateConnection())
            {
                using (var channel = connection.CreateModel())
                {
                    channel.QueueDeclare(queue: usedQueue,
                                         durable: false,
                                         exclusive: false,
                                         autoDelete: false,
                                         arguments: null);
                    var body = Encoding.UTF8.GetBytes(message);

                    channel.BasicPublish(exchange: "",
                                         routingKey: usedQueue,
                                         basicProperties: null,
                                         body: body);
                    Console.WriteLine("Message Sent", message);
                }
            }
        }
    }
}
