from unittest import TestCase
from opensearch import Results, Query

class ResultsTests(TestCase):

    def test_result(self):
        query = Query("http://www.koders.com/?s={searchTerms}&amp;p={startPage}&amp;output=rss&c={count}&amp;i={startIndex}")
        query.searchTerms = "python"
        results = Results(query)
        self.assertEqual(True, (results.totalResults > 0))
        self.assertEqual(results.startIndex, 1)
        self.assertEqual(results.itemsPerPage, 25)
        self.assertEqual(True, len(results.items) > 0)

    def test_iterator_with_index(self):
        query = Query("http://www.koders.com/?s={searchTerms}&amp;p={startPage}&amp;output=rss&c={count}&amp;i={startIndex}")
        query.searchTerms = "python"
        results = Results(query)
        count = 0 
        for i in results:
            count += 1
            if count > 75: 
                break
        self.assertEqual(True, count > 75)


    def test_iterator_with_page(self):
        query = Query("http://www.koders.com/?s={searchTerms}&amp;p={startPage}&amp;output=rss")
        query.searchTerms = "python"
        results = Results(query)
        count = 0 
        for i in results:
            count += 1
            if count > 75: 
                break
        self.assertEqual(True, count > 75)

