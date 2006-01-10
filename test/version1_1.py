from unittest import TestCase
from opensearch import Description, Client

class Version1_1Tests(TestCase):

    atom_v1_1 = 'http://hublog.hubmed.org/opensearchdescription.xml'
    rss_v1_1 = 'http://a9.com/-/opensearch/public/osd'
    rss2_v1_1 = 'http://www.hhpl.on.ca/GreatLakes/GLImages/Opensearch/GreatLakesImages.xml'

    def test_description(self):
        desc = Description(self.atom_v1_1)

        # format won't be populated in v1.1
        self.assertTrue(desc.format == None)

        # check that urls are populated correctly
        self.assertTrue(len(desc.urls) == 2)

        # examine first url
        url1 = desc.urls[0]
        self.assertTrue(url1.template == 'http://hublog.hubmed.org/cgi-bin/mt/mt-search.cgi?IncludeBlogs=2&search={searchTerms}&Template=opensearch')
        self.assertTrue(url1.type == 'application/atom+xml')
       
        # examine 2nd url
        url2 = desc.urls[1]
        self.assertTrue(url2.template == 'http://hublog.hubmed.org/cgi-bin/mt/mt-search.cgi?IncludeBlogs=2&search={searchTerms}')
        self.assertTrue(url2.type == 'text/html')
   
        # test url fetching mechanism
        url = desc.get_url_by_type('application/atom+xml')
        self.assertTrue(url.type == 'application/atom+xml')
        url = desc.get_url_by_type('application/rss+xml')
        self.assertTrue(url == None)

    def test_atom_query(self):
        client = Client(self.atom_v1_1)
        results = client.search('perl')
        self.assertTrue(results.totalResults > 0)

    def test_rss_query(self):
        client = Client(self.rss_v1_1)
        results = client.search('perl')
        self.assertTrue(results.totalResults > 0)

    def test_missing_results(self):
        client = Client(self.rss2_v1_1)
        results = client.search('lewis')
        self.assertTrue(results.totalResults > 0)

