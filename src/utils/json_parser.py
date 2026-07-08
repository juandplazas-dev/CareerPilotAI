import json


class JSONParser:

    @staticmethod
    def parse(text: str):

        return json.loads(text)