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

# workaround for older pythons that don't 
# understand classifiers 

if sys.version_info < (2, 3):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

setup( 
    name             = 'opensearch',
    version          = '0.7',
    url              = 'http://pypi.python.org/pypi/opensearch/',
    author           = 'Ed Summers',
    author_email     = 'ehs@pobox.com',
    license          = 'http://www.opensource.org/licenses/gpl-license.php',
    packages         = find_packages(),
    description      = "Interact with opensearch services",
    classifiers      = filter( None, classifiers.split("\n") ),
)

