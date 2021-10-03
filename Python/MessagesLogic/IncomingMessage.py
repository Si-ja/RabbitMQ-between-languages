import json


class IncomingMessage:

    def __init__(self, message):
        self.message = message
        self.message_json = {"Id": None,
                             "Platform": None,
                             "Parameters": None,
                             "Application": None}
        self.message_compatible = False

        self.expected_id = "Id"
        self.expected_platform = "Platform"
        self.expected_parameters = "Parameters"
        self.expected_application = "Application"

        self.actual_id = None
        self.actual_platform = None
        self.actual_parameters = None
        self.actual_application = None

        self.available_platforms = ["Python", ".NET", "Java"]
        self.available_applications = ["Square area", "Rectangle area", "Prime values"]
        self.available_parameters = {"Square area": 1, "Rectangle area": 2, "Prime values": 1}

        self.__assess_message()

    def __assess_message(self):
        try:
            self.message_json = json.loads(self.message)
        except:
            print(f"Issue occurred, while converting string to json.")
            return

        try:
            self.actual_id = self.message_json[self.expected_id]
            self.actual_platform = self.message_json[self.expected_platform]
            self.actual_parameters = self.message_json[self.expected_parameters]
            self.actual_application = self.message_json[self.expected_application]

            if self.actual_platform not in self.available_platforms:
                print(f"The indicated platform is not supported currently")
                return
            if self.actual_application not in self.available_applications:
                print(f"The indicated application is not present with the application")
                return
            if len(self.actual_parameters) != self.available_parameters[self.actual_application]:
                print(f"The amount of indicated parameters is inconsistent with the current application")
                return

            print("The message got successfully processed")

        except:
            print(f"Issue occurred while parsing data from the incoming message.")
            return
