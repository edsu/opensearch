from description import Description
from query import Query
from results import Results

class Client:

    def __init__(self, url, page_size=25):
        self.description = Description(url)
        self.page_size = 25

    def search(self, search_terms):
        # get a query object
        query = Query(self.description.url)

        # set up initial values
        query.search_terms = search_terms
        query.count = 25
        query.start_index = 1

        # run the results
        results = Results(query)
        results.run()
        return results

        





