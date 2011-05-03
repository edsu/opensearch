import sys
from distutils.core import setup
from setuptools import find_packages

classifiers = """\
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: GNU General Public License (GPL)
Programming Language :: Python
Topic :: Text Processing :: General
"""

setup( 
    name             = 'opensearch',
    version          = '0.9',
    url              = 'http://github.com/edsu/opensearch',
    author           = 'Ed Summers',
    author_email     = 'ehs@pobox.com',
    license          = 'http://www.opensource.org/licenses/gpl-license.php',
    packages         = find_packages(exclude=['test']),
    description      = "Interact with opensearch services",
    classifiers      = filter( None, classifiers.split("\n") ),
    tests_require    = ["nose>=0.10.4"],
    test_suite       = 'nose.collector',
)

