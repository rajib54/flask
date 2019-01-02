import os
import sys

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

from Handler import QuoteHandler


def test_get_quotes():
    result = {"payload": {"quote": {"quote": [{"id": 1, "name": "Quote 1"}, {"id": 2, "name": "Quote 2"}]}}}

    quotehandler = QuoteHandler()
    expectedresult = quotehandler.getquotes()

    assert result == expectedresult
