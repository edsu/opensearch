import sys
from distutils.core import setup

classifiers = """\
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: BSD License
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
    version          = '0.3',
    url              = 'http://www.textualize.com/opensearch',
    download_url     = 'http://www.textualize.com/archive/opensearch/latest.tar.gz',
    author           = 'Ed Summers',
    author_email     = 'ehs@pobox.com',
    license          = 'http://www.opensource.org/licenses/artistic-license.php',
    packages         = [ 'opensearch' ],
    description      = "Interact with opensearch services",
    classifiers      = filter( None, classifiers.split("\n") ),
)

