from unittest import TestCase
from opensearch import Description

class DescriptionTests(TestCase):

    # just grab the description once for all these tests
    url = 'http://www.koders.com/search/KodersSourceCodeSearchDescription.xml'
    desc = Description(url)

    def test_url(self):
        self.assertTrue(self.desc.url ==
            'http://www.koders.com/?s={searchTerms}&p={startPage}&output=rss' )

    def test_format(self):
        self.assertTrue(self.desc.format == 'http://a9.com/-/spec/opensearchrss/1.0/')

    def test_shortname(self):
        self.assertTrue(self.desc.shortname == 'Koders')

    def test_longname(self):
        self.assertTrue(self.desc.longname == 'Koders Source Code Search')

    def test_description(self):
        self.assertTrue(self.desc.description == 'Search open source code on Koders.com. Supports languages such as java, c, c++, c#, php, perl, python, and many others.')

    def test_tags(self):
        self.assertTrue(self.desc.tags == ['koders', 'source', 'code', 
            'open-source', 'programming', 'software'])

    def test_image(self):
        self.assertTrue(self.desc.image ==
            'http://www.koders.com/images/koders_icon64x64.gif')

    def test_samplesearch(self):
        self.assertTrue(self.desc.samplesearch == 'calculator')

    def test_developer(self):
        self.assertTrue(self.desc.developer == 'Koders Inc.')

    def test_contact(self):
        self.assertTrue(self.desc.contact == 'webmaster@koders.com')

    def test_attribution(self):
        self.assertTrue(self.desc.attribution == 
            '&copy; 2005, Koders Inc., All Rights Reserved.')

    def test_syndicationright(self):
        self.assertTrue(self.desc.syndicationright == 'open')

    def test_adultcontent(self):
        self.assertTrue(self.desc.adultcontent == False)


