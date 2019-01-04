from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.Service import QuoteService
from app.Handler import QuoteHandler


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
