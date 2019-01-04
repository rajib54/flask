import sys
sys.path.append('.')

from flask import Flask, request, jsonify
from Service import QuoteService
from Handler import QuoteHandler

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return 'Post request'
    else:
        return 'GET request'


@app.route('/quote/<id>')
def quotebyid(id):
    service = QuoteService(QuoteHandler())
    return jsonify(service.getquotebyid(id))


@app.route('/quotes')
def quotes():
    service = QuoteService(QuoteHandler())
    return jsonify(service.getquotes())