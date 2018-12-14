import os
import sys

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

from Handler import QuoteHandler
from Model import Quote


def test_get_quotes():
    result = {"payload": {"quote": {"quote": [{"id": 1, "name": "Quote 1"}, {"id": 1, "name": "Quote 1"}]}}}

    quotehandler = QuoteHandler()
    expectedresult = quotehandler.getQuotes()

    assert result == expectedresult
