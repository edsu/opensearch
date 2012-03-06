import re
import urllib
import urlparse

class Query:
    """Represents an opensearch query. Used internally by the Client to 
    construct an opensearch url to request. Really this class is just a 
    helper for substituting values into the macros in a format. 

    format = 'http://beta.indeed.com/opensearch?q={searchTerms}&start={startIndex}&limit={count}'
    q = Query(format)
    q.searchTerms('zx81')
    q.startIndex = 1
    q.count = 25
    print q.to_url()
    """

    standard_macros = ['searchTerms','count','startIndex','startPage', 
        'language', 'outputEncoding', 'inputEncoding']

    def __init__(self, format):
        """Create a query object by passing it the url format obtained
        from the opensearch Description.
        """
        self.format = format
        self.url_parts = urlparse.urlparse(format)
        qsl = urlparse.parse_qsl(self.url_parts[4])
        self.params = []

        for key, value in qsl:
            self.params.append(Param(key, value))

    def url(self):
        # build new query string list substituting any macros
        # TODO: make sure required params are filled in
        qsl = []
        for param in self.params:
            if param.macro and hasattr(self, param.macro):
                qsl.append((param.name, getattr(self, param.macro)))
            elif not param.macro:
                qsl.append((param.name, param.value))

        # create new url using the query string list
        url_parts = list(self.url_parts)
        url_parts[4] = urllib.urlencode(qsl)
        return urlparse.urlunparse(tuple(url_parts))

    def has_macro(self, macro_name):
        for param in self.params:
            if param.macro == macro_name:
                return True
        return False

class Param:

    def __init__(self, name, value):
        self.name = name
        self.value = value 

        # this ugly regex is looking to capture 'macro' in '{macro}',  
        # '{prefix:macro}' and '{macro?}' ... sorry
        match = re.match('^{((.+):)?(.+?)(\?)?}$', value)

        if match:
            self.prefix = match.group(2)
            if self.prefix:
                self.macro = self.prefix + "__" + match.group(3)
            else:
                self.macro = match.group(3)
            self.optional = match.group(4) == "?"
        else:
            self.prefix = None
            self.macro = None
            self.optional = False

    def __repr__(self):
        return "param(name=%s, prefix=%s, macro=%s, optional=%s value=%s" % (self.name, self.prefix, self.macro, self.optional, self.value)

