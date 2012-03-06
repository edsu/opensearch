from description import Description
from query import Query
from results import Results

class Client:

    """This is the class you'll probably want to be using. You simply
    pass the constructor the url for the service description file and
    issue a search and get back results as an iterable Results object.

    The kinda neat thing about a Results object is that it will seamlessly
    handle fetching more results from the opensearch server when it can...
    so you just need to iterate and can let the paging be taken care of 
    for you.

    >>> from opensearch import Client
    >>> client = Client(description_url)
    >>> results = client.search("computer")
    >>> print results.totalResults
    >>> for result in results:
            print result.title

    If you have additional paramters to pass in the template just use
    their name. So for example if the template was 

        http://example.org/search?q={searchTerms}&key={key}

    you could supply key with:

    >>> results = client.search("computer", key="abc123")

    Additionally if you want to use prefixed parameter names you'll need to use
    the double underscore syntax. So for a template like:

        http://example.org/search?q={searchTerms}&key={ex:key}

    you could supply ex:key with:

    >>> results = client.search("computer", ex__key="abc123")
    """

    def __init__(self, url, agent="python-opensearch <https://github.com/edsu/opensearch>"):
        self.agent = agent
        self.description = Description(url, self.agent)

    def search(self, search_terms, page_size=25, **kwargs):
        """Perform a search and get back a results object
        """
        url = self.description.get_best_template()
        query = Query(url)

        # set up initial values
        query.searchTerms = search_terms
        query.count = page_size

        # add any additional parameters to the query
        for name, value in kwargs.items():
            setattr(query, name, value)

        # run the results
        return Results(query, agent=self.agent)

