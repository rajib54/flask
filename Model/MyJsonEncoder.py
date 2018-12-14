from flask.json import JSONEncoder


class MyJsonEncoder(JSONEncoder):
    def default(self, obj):
        data = {}
        for key, value in obj.__dict__.items():
            data[key] = value
        return data
