from opensearch import Client
from unittest import TestCase

class ClientTests(TestCase):

    url = 'http://www.koders.com/search/KodersSourceCodeSearchDescription.xml'

    def test_query(self):
        client = Client(ClientTests.url)
        self.assertEqual(client.agent, 'python-opensearch <https://github.com/edsu/opensearch>')
        results = client.search("computer")
        assert(results.totalResults > 0)
