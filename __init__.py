import sys

sys.path.append('.')

from flask import Flask, request
from src.Service import QuoteService
from src.Handler import QuoteHandler
from src.Model import MyJsonEncoder

app = Flask(__name__)
app.json_encoder = MyJsonEncoder


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return 'Post request'
    else:
        return 'GET request'


@app.route('/quote/<id>')
def quotebyid(id):
    service = QuoteService(QuoteHandler())
    return service.getQuoteById(id)


@app.route('/quotes')
def quotes():
    service = QuoteService(QuoteHandler())
    return service.getQuotes()
