from Abstract import QuoteHandlerAbstract
from flask import jsonify


class QuoteHandler(QuoteHandlerAbstract):
    def __init__(self):
        self.logCollector = "Log Collector"

    @classmethod
    def getQuoteById(self, id):
        payload = {
            "payload": {
                "quote": {
                    "quote": [
                        {
                            "id": id,
                            "Name": "Name 1"
                        }
                    ]
                }
            }
        }
        return jsonify(payload)
