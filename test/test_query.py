from unittest import TestCase
from opensearch import Query, Param

class QueryTests(TestCase):

    template = "http://www.koders.com/?s={searchTerms}&p={startPage}&output=rss&c={count}&i={startIndex}"

    def test_searchTerms(self):
        q = Query(QueryTests.template)
        q.searchTerms = 'zx81'
        self.assertEqual(q.url(), 'http://www.koders.com/?s=zx81&output=rss')

    def test_count(self):
        q = Query(QueryTests.template)
        q.count = 25
        self.assertEqual(q.url(), 'http://www.koders.com/?output=rss&c=25')

    def test_startPage(self):
        q = Query(QueryTests.template)
        q.startPage = 5
        self.assertEqual(q.url(), 'http://www.koders.com/?p=5&output=rss')

    def test_startIndex(self):
        q = Query(QueryTests.template)
        q.startIndex = 5
        self.assertEqual(q.url(), 'http://www.koders.com/?output=rss&i=5')

    def test_multiple(self):
        q = Query(QueryTests.template)
        q.searchTerms = 'zx81'
        q.startIndex = 15
        q.count = 15
        self.assertEqual(q.url(), 
            'http://www.koders.com/?s=zx81&output=rss&c=15&i=15')

    def test_extra_param(self):
        template = "http://www.koders.com/?s={searchTerms}&p={startPage}&output=rss&c={count}&i={startIndex}&key={key}"
        q = Query(template)
        self.assertTrue(q.has_macro('key'))
        q.searchTerms = 'zx81'
        q.key = 'abc123'
        self.assertEqual(q.url(), 'http://www.koders.com/?s=zx81&output=rss&key=abc123')

    def test_prefix(self):
        template = "http://worldcat.org/webservices/catalog/search/worldcat/opensearch?q={searchTerms}&start={startIndex?}&count={resultSize?}&format=atom&wskey={wcapi:wskey}&cformat={wcapi:cformat?}"
        q = Query(template)
        self.assertTrue(q.has_macro('searchTerms'))
        self.assertTrue(q.has_macro('wcapi__wskey'))
        q.searchTerms = "computer"
        q.wcapi__wskey = "abc123"
        self.assertEqual(q.url(), 'http://worldcat.org/webservices/catalog/search/worldcat/opensearch?q=computer&format=atom&wskey=abc123')

    def test_param(self):
        p = Param("foo", "bar")
        self.assertEqual(p.name, "foo")
        self.assertEqual(p.value, "bar")
        self.assertEqual(p.macro, None)
        self.assertEqual(p.optional, False)

    def test_macro(self):
        p = Param("foo", "{bar}")
        self.assertEqual(p.name, "foo")
        self.assertEqual(p.value, "{bar}")
        self.assertEqual(p.macro, "bar")
        self.assertEqual(p.optional, False)

    def test_prefix_macro(self):
        p = Param("foo", "{bar:baz}")
        self.assertEqual(p.name, "foo")
        self.assertEqual(p.value, "{bar:baz}")
        self.assertEqual(p.macro, "bar__baz")
        self.assertEqual(p.optional, False)

