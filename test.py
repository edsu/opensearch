#!/usr/bin/env python2.4

from unittest import TestSuite, TextTestRunner, makeSuite
from test.description import DescriptionTests

suite = TestSuite()
suite.addTest(makeSuite(DescriptionTests, 'test'))
runner = TextTestRunner(verbosity=2)
runner.run(suite)


