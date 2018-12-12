from flask.json import JSONEncoder


class Quote(JSONEncoder):
    id = None
    name = None

    def default(self, obj):
        return JSONEncoder.default(self, obj)
