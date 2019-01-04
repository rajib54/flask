from app.Abstract import QuoteHandlerAbstract
from app.Model import Quote
from app import db


class QuoteHandler(QuoteHandlerAbstract):
    def __init__(self):
        self.logCollector = "Log Collector"

    @classmethod
    def getquotes(self):
        quotes = []

        data = db.engine.execute("select * from quote")
        for row in data:
            quote = Quote()
            quote.id = row[0]
            quote.name = row[1]
            quote.description = row[2]
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
        data = db.engine.execute("select * from quote where id = " +id)
        for row in data:
            quote.id = row[0]
            quote.name = row[1]
            quote.description = row[2]

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
