using System;
using System.Text;
using RabbitMQ.Client;

namespace ProducerService
{
    class Program
    {
        static void Main(string[] args)
        {
            Producer.SendMessage(environmnet: "localhost", message: "Hello, World");
        }
    }
}
