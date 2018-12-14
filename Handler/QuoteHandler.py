from Abstract import QuoteHandlerAbstract
from flask import jsonify
from Model import Quote


class QuoteHandler(QuoteHandlerAbstract):
    def __init__(self):
        self.logCollector = "Log Collector"

    @classmethod
    def getQuotes(self):
        quote1 = Quote()
        quote1.id = 1
        quote1.name = "Quote 1"

        quote2 = Quote()
        quote2.id = 2
        quote2.name = "Quote 2"

        quotes = [quote1, quote2]

        payload = {
            "payload": {
                "quote": {
                    "quote": quotes
                }
            }
        }
        return jsonify(payload)

    @classmethod
    def getQuoteById(self, id):
        quote = Quote()
        quote.id = id
        quote.name = "Quote 1"

        payload = {
            "payload": {
                "quote": {
                    "quote": [
                        quote
                    ]
                }
            }
        }
        return jsonify(payload)
