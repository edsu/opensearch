from opensearch import Client
from unittest import TestCase

class ClientTests(TestCase):

    url = 'http://www.koders.com/search/KodersSourceCodeSearchDescription.xml'

    def test_query(self):
        pass
        #client = Client(ClientTests.url)
        #results = client.search("computer")