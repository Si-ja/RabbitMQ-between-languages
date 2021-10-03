using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using ProducerService;

namespace LocalApplicationNET
{
    class Program
    {
        static void Main(string[] args)
        {
            while(true)
            {
                int applicationChosenInt = 0;
                List<float> parametersChosen = new();
                string requestorChosen = ".NET";
                Guid idChosen = Guid.NewGuid();

                string operatedEnvironment = "localhost";

                var applications = new Applications();
                applications.StateAllApplicationOptions();
                bool conditionChosenBool = false;
                while (!conditionChosenBool)
                {
                    Console.Write("Enter Your Option of Choice: ");
                    string applicationChosen = Console.ReadLine();
                    bool applicationChosenIntCheck = Int32.TryParse(applicationChosen, out applicationChosenInt);
                    if (applicationChosenIntCheck)
                    {
                        bool keyCheck = applications.CheckIfKeyExistsInAvailableApplications(value: applicationChosenInt);
                        if (keyCheck)
                        {
                            conditionChosenBool = keyCheck;
                        }
                    }
                }

                int neededParameters = applications.StateAllNeededParameters(key: applicationChosenInt);
                {
                    for (int i = 0; i < neededParameters; i++)
                    {
                        bool parameterChosenBool = false;
                        while (!parameterChosenBool)
                        {
                            Console.Write("Chose a parameter to use: ");
                            string parameterChosen = Console.ReadLine();
                            float newParameter;
                            bool parameterChosenFloatCheck = float.TryParse(parameterChosen, out newParameter);
                            if (parameterChosenFloatCheck)
                            {
                                parametersChosen.Add(newParameter);
                                parameterChosenBool = true;
                            }
                        }
                    }
                }

                Message message = new();
                message.Id = idChosen;
                message.Platform = requestorChosen;
                message.Application = applications.FindApplicationNameUsingIdReference(applicationChosenInt);
                message.Parameters = parametersChosen;

                string jsonMessage = JsonConvert.SerializeObject(message);

                Console.WriteLine($"Your unique ID is: {message.Id}");
                Producer.SendMessage(environmnet: operatedEnvironment, message: jsonMessage);
                Console.WriteLine();
            }
            
        }
    }
}
