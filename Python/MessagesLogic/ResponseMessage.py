import json


class ResponseMessage:

    def __init__(self, answer, id):
        self.answer = answer
        self.id = id
        self.message = json.dumps({"Id": id, "Answer": answer})
