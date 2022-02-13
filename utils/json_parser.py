import json


class JsonParser():

    @staticmethod
    def parse_configuration():
        with open("sorce/configuration.json") as f:
            data = f.read()
            data = json.loads(data)
            return data

    @staticmethod
    def parse_constatns():
        with open('sorce/constants.json') as f:
            data = f.read()
            data = json.loads(data)
            return data