opensearch
==========

opensearch is a python library for talking to opensearch servers.
Both v1.0 and v1.1 interactions are supported.  You can find out more 
about opensearch at [opensearch.org](http://opensearch.org).

Usage
-----

Here's the basic idea:

```python
from opensearch import Client

client = Client(description_url)
results = client.search('zx81')

for result in results:
    print result.title, result.link
```

If you have a template with some non-standard query parameters like `key` in
this template:

```xml
   <Url type="application/atom+xml" template="http://example.org/search?q={searchTerms}&amp;start={startIndex?}&amp;count={resultSize?}&amp;key={key}"/>
```

you can send the parameter like so:

```python
results = client.search('zx81', key="abc123")
```

If the template happens to use a namespace prefix, as in this real example 
from the OCLC Worldcat API, which uses `wcapi:wskey`:

```xml
<Url type="application/atom+xml" xmlns:wcapi="http://www.worldcat.org/devnet/wiki/SearchAPIDetails" template="http://worldcat.org/webservices/catalog/search/worldcat/opensearch?q={searchTerms}&amp;start={startIndex?}&amp;count={resultSize?}&amp;format=atom&amp;wskey={wcapi:wskey}&amp;cformat={wcapi:cformat?}"/>
```

You can supply `wcapi:wskey` using the underscore notation:

```python
results = client.search('zx81', wcapi__wskey="abc123")
```

Debugging
---------

If you run into trouble and would like to see what URLs are being accessed
behind the scenes, turn on logging and set the log level to DEBUG:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

To Do
-----

- handle v1.1 that want a POST instead of a GET
- figure out if the latest feedparser can be used as a dependency
- validate required parameters

License
-------

The opensearch code itself has been released under the 
[GPL](http://www.opensource.org/licenses/gpl-license.php).

One exception is that the distro bundles Mark Pilgrim's Universal Feed 
Parser, which is licensed separately under the MIT license. See 
opensearch/osfeedparser.py for details on Mark's license.

Author
------

Ed Summers [ehs@pobox.com](mailto:ehs@pobox.com)
