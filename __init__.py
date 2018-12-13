import sys

sys.path.append('.')

from flask import Flask, request
from Service import QuoteService
from Handler import QuoteHandler
from Model import MyJsonEncoder

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
