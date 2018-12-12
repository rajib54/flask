from Abstract import QuoteHandlerAbstract
from flask import jsonify
from Model import Quote


class QuoteHandler(QuoteHandlerAbstract):
    def __init__(self):
        self.logCollector = "Log Collector"

    @classmethod
    def getQuoteById(self, id):
        quote = Quote()
        quote.id = id
        quote.name = "Name 1"

        payload = {
            "payload": {
                "quote": {
                    "quote": [
                        {
                            "id": quote.id,
                            "name": quote.name
                        }
                    ]
                }
            }
        }
        return jsonify(payload)
