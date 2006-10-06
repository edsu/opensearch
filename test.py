#!/usr/bin/env python2.4

from unittest import TestSuite, TextTestRunner, makeSuite
from test.description import DescriptionTests
from test.query import QueryTests
from test.results import ResultsTests
from test.client import ClientTests

suite = TestSuite()
suite.addTest(makeSuite(DescriptionTests, 'test'))
suite.addTest(makeSuite(QueryTests, 'test'))
suite.addTest(makeSuite(ClientTests, 'test'))
suite.addTest(makeSuite(ResultsTests, 'test'))
runner = TextTestRunner(verbosity=3)
runner.run(suite)

