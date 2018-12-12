import sys

sys.path.append('.')

from flask import Flask, request
from Service import QuoteService
from Handler import QuoteHandler

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return 'Post request'
    else:
        service = QuoteService(QuoteHandler())
        return service.getQuoteById(10)
