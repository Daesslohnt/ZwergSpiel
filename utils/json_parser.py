import json


class JsonParser():

    @staticmethod
    def parse():
        with open("sorce/configuration.json") as f:
            data = f.read()
            data = json.loads(data)
            return data