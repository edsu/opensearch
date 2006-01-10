#!/usr/bin/env python2.4

from unittest import TestSuite, TextTestRunner, makeSuite
from test.description import DescriptionTests
from test.query import QueryTests
from test.results import ResultsTests
from test.client import ClientTests
from test.version1_1 import Version1_1Tests

suite = TestSuite()
suite.addTest(makeSuite(DescriptionTests, 'test'))
suite.addTest(makeSuite(QueryTests, 'test'))
suite.addTest(makeSuite(ClientTests, 'test'))
suite.addTest(makeSuite(ResultsTests, 'test'))
suite.addTest(makeSuite(Version1_1Tests, 'test'))
runner = TextTestRunner(verbosity=3)
runner.run(suite)

