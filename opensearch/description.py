from urllib2 import urlopen
from xml.dom.minidom import parse

class Description:
    """A class for representing OpenSearch Description files.
    """

    def __init__(self, url=""):
        """The constructor which may pass an optional url to load from.

        d = Description("http://www.example.com/description")
        """
        if url: 
            self.load(url)


    def load(self, url):
        """For loading up a description object from a url. Normally
        you'll probably just want to pass a URL into the constructor.
        """
        self.dom = parse(urlopen(url))
        self.url = self._get_element_text('Url')
        self.format = self._get_element_text('Format')
        self.shortname = self._get_element_text('ShortName')
        self.longname = self._get_element_text('LongName')
        self.description = self._get_element_text('Description')
        self.image = self._get_element_text('Image')
        self.samplesearch = self._get_element_text('SampleSearch')
        self.developer = self._get_element_text('Developer')
        self.contact = self._get_element_text('Contact')
        self.attribution = self._get_element_text('Attribution')
        self.syndicationright = self._get_element_text('SyndicationRight')
        self.tags = self._get_element_text('Tags').split(" ")
        if self._get_element_text('AdultContent') == 'true':
            self.adultcontent = True
        else:
            self.adultcontent = False

    # these are internal methods for querying xml

    def _get_element_text(self, tag):
        elements = self._get_elements(tag)
        if not elements:
            return ''
        return self._get_text(elements[0].childNodes)

    def _get_elements(self, tag):
        return self.dom.getElementsByTagName(tag)
 
    def _get_text(self, nodes):
        text = ''
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                text += node.data
        return text

