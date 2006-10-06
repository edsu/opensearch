from unittest import TestCase
from opensearch import Query

class QueryTests(TestCase):

    template = "http://www.koders.com/?s={searchTerms}&amp;p={startPage}&amp;output=rss&c={count}&amp;i={startIndex}"

    def test_searchTerms(self):
        q = Query(QueryTests.template)
        q.searchTerms = 'zx81'
        self.assertEqual(q.url(), 'http://www.koders.com/?s=zx81&output=rss')

    def test_count(self):
        q = Query(QueryTests.template)
        q.count = 25
        self.assertEqual(q.url(), 'http://www.koders.com/?c=25&output=rss')

    def test_startPage(self):
        q = Query(QueryTests.template)
        q.startPage = 5
        self.assertEqual(q.url(), 'http://www.koders.com/?p=5&output=rss')

    def test_startIndex(self):
        q = Query(QueryTests.template)
        q.startIndex = 5
        self.assertEqual(q.url(), 'http://www.koders.com/?i=5&output=rss')

    def test_multiple(self):
        q = Query(QueryTests.template)
        q.searchTerms = 'zx81'
        q.startIndex = 15
        q.count = 15
        self.assertEqual(q.url(), 
            'http://www.koders.com/?i=15&s=zx81&c=15&output=rss')

