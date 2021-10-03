using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LocalApplicationNET
{
    class Applications
    {
        private Dictionary<int, string> availableApplications = new();
        private Dictionary<int, int> requiredApplicationBindedParameters = new();
        
        public Applications()
        {
            availableApplications.Add(key: 1, value: "Square area");
            availableApplications.Add(key: 2, value: "Rectangle area");
            availableApplications.Add(key: 3, value: "Prime values");

            requiredApplicationBindedParameters.Add(key: 1, value: 1);
            requiredApplicationBindedParameters.Add(key: 2, value: 2);
            requiredApplicationBindedParameters.Add(key: 3, value: 1);
        }

        public void StateAllApplicationOptions()
        {
            Console.WriteLine("================================================================");
            foreach (var keyValuePair in availableApplications)
            {
                Console.WriteLine($"Select {keyValuePair.Key} to use the service: {keyValuePair.Value}");
            }
            Console.WriteLine("================================================================");
        }

        public string FindApplicationNameUsingIdReference(int key)
        {
            string applicationName = string.Empty;
            availableApplications.TryGetValue(key, out applicationName);
            return applicationName;
        }

        public bool CheckIfKeyExistsInAvailableApplications(int value)
        {
            foreach (var keyValuePair in availableApplications)
            {
                if (value == keyValuePair.Key)
                {
                    return true;
                }
            }
            return false;
        }

        public int StateAllNeededParameters(int key)
        {
            int requiredParametersAmount;
            requiredApplicationBindedParameters.TryGetValue(key, out requiredParametersAmount);

            Console.WriteLine("================================================================");
            Console.WriteLine($"You need to pass in {requiredParametersAmount} parameters.");
            Console.WriteLine("================================================================");

            return requiredParametersAmount;
        }
    }
}
