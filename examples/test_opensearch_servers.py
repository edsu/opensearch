#!/usr/bin/env python

# this python script walks all the opensearch servers
# and tries to exercise them, and report any errors
#
# Rob Sanderson <azaroth@liv.ac.uk>

from opensearch import Client
import socket, urllib2
socket.setdefaulttimeout(10)

# OS list of open OS targets
mainc = Client('http://a9.com/-/opensearch/public/osd')
mainres = mainc.search('') # fetch all

for site in mainres:
    print "Trying: %s" % site.link
    try:
        c = Client(site.link)
    except socket.timeout:
        print " ... timed out"
        continue
    except urllib2.URLError:
        print " ... timed out"
        continue
    except:
        print " ... ERROR: couldn't create Client"
        continue
    q =  c.description.samplesearch
    if not q:
        q = "cat"
    res = c.search(q)
    try:
        item = res.next()
        print " TITLE: %s" % item.title
    except StopIteration:
        print " ... No Matches"
    except:
        print " ... ERROR: something wrong in iterator"
