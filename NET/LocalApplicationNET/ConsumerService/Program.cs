using System;

namespace ConsumerService
{
    class Program
    {
        static void Main(string[] args)
        {
            Consumer.ReceiveMessages(environmnet: "localhost");
        }
    }
}
