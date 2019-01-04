from app.Abstract import QuoteHandlerAbstract
from app.Model import Quote


class QuoteHandler(QuoteHandlerAbstract):
    def __init__(self):
        self.logCollector = "Log Collector"

    @classmethod
    def getquotes(self):
        quotes = []

        for i in range(1, 3):
            quote = Quote()
            quote.id = i
            quote.name = "Quote " + str(i)
            quotes.append(quote.toarray())

        payload = {
            "payload": {
                "quote": {
                    "quote": quotes
                }
            }
        }
        return payload

    @classmethod
    def getquotebyid(self, id):
        quote = Quote()
        quote.id = int(id)
        quote.name = "Quote " + id

        payload = {
            "payload": {
                "quote": {
                    "quote": [
                        quote.toarray()
                    ]
                }
            }
        }
        return payload
