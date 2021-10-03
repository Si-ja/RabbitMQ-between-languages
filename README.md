# RabbitMQ Between Languages

If you ever wanted to allow for communication between language but didn't know how to create and use an API, then
this might be something that you are looking for. 

RabbitMQ is a message broker, but by using some clever tactics, it is possible to allow your users use
a .NET application you have created, but have all the complex calculations run on the side that is manage
by say Python. This could be applicable for such cases where you wouldn't want to rewrite an already existing application, 
or want to use an approach that is much friendlier to some tasks you are looking to use it for, like Machine Learning.

This project is as a simple example of such implementation. Everything runs in consoles, there are no
databases, and RabbitMQ is run with the docker, using the basic parameters (i.e. no configurations, so even the
default user is `guest` with password `guest`).

## How to use it

Start either your own RabbitMQ instance (basic one, running on localhost) or the one prepared in the `docker-compose` 
file. On the Python side, run the Consumer class. On the .NET side, run the ConsumerService, by starting the `Program`
class. Now you will have 2 consumers that are waiting for information to appear in the RabbitMQ.

Finally, start on the .NET side the LocalApplicationNET `Program` class. It will give you several options on what
you can do (look further for a visual example). Chose appropriate options and enter information asked. After you will enter data as an input to the 
program (which will either ask to calculate the area of a square, rectangle, or find a sequence of prime values) the
program will send a message to Rabbit. Consumer on the Python side will consume the message, process it, and will return
into a queue dedicated to your application (in this case .NET). Consumer on the .NET side will consume the message and
display it in its own console window. In the future, the plans were to add also the Java application, just to see how
this is easily working when the major set up is already in place.

## The Good, the bad and the ugly

On the positives - you have a communication between applications that should work. The bad part - it is based on 
messages consumption through a queue. This means that it is quite hard to implement this in real time and maybe quite
messy. The ugly truth is that such applications might work if you send all of the processed data to a database and later
make your users check whether their messages got processed successfully. The message broker is not an alternative to 
an API, but a different technology, so it also has a bit of a different logic getting implemented and used, but eitherway, 
you can make some cool things with it.

## Example of this being used in practice:

![](https://github.com/Si-ja/RabbitMQ-between-languages/blob/main/Visuals/RabbitMQQueues.png "RabbitMQ Queues")
![](https://github.com/Si-ja/RabbitMQ-between-languages/blob/main/Visuals/Python_Consumer.png "Python Consumer")
![](https://github.com/Si-ja/RabbitMQ-between-languages/blob/main/Visuals/NET_Consumer.png ".NET Consumer")
![](https://github.com/Si-ja/RabbitMQ-between-languages/blob/main/Visuals/NET_application.png ".NET Application")