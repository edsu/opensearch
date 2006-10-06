from unittest import TestCase
from opensearch import Description

class DescriptionTests(TestCase):

    # just grab the description once for all these tests
    url = 'http://www.koders.com/search/KodersSourceCodeSearchDescription.xml'
    desc = Description(url)

    def test_url(self):
        self.assertEqual(self.desc.url,
            'http://www.koders.com/?s={searchTerms}&p={startPage}&output=rss' )

    def test_format(self):
        self.assertEqual(self.desc.format, 
            'http://a9.com/-/spec/opensearchrss/1.0/')

    def test_shortname(self):
        self.assertEqual(self.desc.shortname, 'Koders')

    def test_longname(self):
        self.assertEqual(self.desc.longname, 'Koders Source Code Search')

    def test_description(self):
        self.assertEqual(self.desc.description, 'Search open source code on Koders.com. Supports languages such as java, c, c++, c#, php, perl, python, and many others.')

    def test_tags(self):
        self.assertEqual(self.desc.tags, ['koders', 'source', 'code', 
            'open-source', 'programming', 'software'])

    def test_image(self):
        self.assertEqual(self.desc.image,
            'http://www.koders.com/images/koders_icon64x64.gif')

    def test_samplesearch(self):
        self.assertEqual(self.desc.samplesearch, 'calculator')

    def test_developer(self):
        self.assertEqual(self.desc.developer, 'Koders Inc.')

    def test_contact(self):
        self.assertEqual(self.desc.contact, 'webmaster@koders.com')

    def test_attribution(self):
        self.assertEqual(self.desc.attribution,
            '&copy; 2005, Koders Inc., All Rights Reserved.')

    def test_syndicationright(self):
        self.assertEqual(self.desc.syndicationright, 'open')

    def test_adultcontent(self):
        self.assertEqual(self.desc.adultcontent, False)


