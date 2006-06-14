from opensearch import osfeedparser

class Results(object):

    def __init__(self,query):
        self._fetch(query)
        self._iter = 0

    def __iter__(self):
        self._iter = 0
        return self

    def __len__(self):
      return self.totalResults

    def next(self):

        # just keep going like the energizer bunny
        while True:

            # return any item we haven't returned
            if self._iter < len(self.items):
                self._iter += 1
                return self.items[self._iter-1]
          
            # if there appears to be more to fetch
            if \
                self.totalResults != 0 \
                and self.totalResults > self.startIndex + self.itemsPerPage - 1:

                # get the next query
                next_query = self._get_next_query()

                # if we got one executed it and go back to the beginning
                if next_query:
                    self._fetch(next_query)
                    # very important to reset this counter 
                    # or else the return will fail
                    self._iter = 0

            else:
                raise StopIteration


    def _fetch(self, query):
        feed  = osfeedparser.opensearch_parse(query.url())
        self.feed = feed

        # general channel stuff
        channel = feed['feed']
        self.title = _pick(channel,'title')
        self.link = _pick(channel,'link')
        self.description = _pick(channel,'description')
        self.language = _pick(channel,'language')
        self.copyright = _pick(channel,'copyright')

        # get back opensearch specific values
        self.totalResults = int(_pick(channel,'opensearch_totalresults',0))
        self.startIndex = int(_pick(channel,'opensearch_startindex',1)) 
        self.itemsPerPage = int(_pick(channel,'opensearch_itemsperpage',0))

        # alias items from the feed to our results object
        self.items = feed['items']

        # set default values if necessary
        if self.startIndex == 0:
            self.startIndex = 1
        if self.itemsPerPage == 0 and len(self.items) > 0:
            self.itemsPerPage = len(self.items)

        # store away query for calculating next results
        # if necessary
        self.last_query = query


    def _get_next_query(self):
        # update our query to get the next set of records
        query = self.last_query

        # use start page if the query supports it
        if query.has_macro('startPage'):
            # if the query already defined the startPage 
            # we just need to increment it
            if hasattr(query, 'startPage'):
                query.startPage += 1
            # to issue the first query startPage might not have
            # been specified, so set it to 2
            else:
                query.startPage = 2
            return query

        # otherwise the query should support startIndex
        elif query.has_macro('startIndex'):
            # if startIndex was used before we just add the 
            # items per page to it to get the next set
            if hasattr(query, 'startIndex'):
                query.startIndex += self.itemsPerPage
            # to issue the first query the startIndex may have
            # been left blank in that case we assume it to be
            # the item just after the last one on this page
            else:
                query.startIndex = self.itemsPerPage + 1
            return query

        # doesn't look like there is another stage to this query
        return None


# helper for pulling values out of a dictionary if they're there
def _pick(d,key,default=None):
    if d.has_key(key):
        # don't want to return '' if they want an int
        if type(default) == int and d[key] == '':
            return 0
        return d[key]
    return default
