import unittest
from crash_analysis import Crash_Analysis

# Create a Crash_Analysis object
data = Crash_Analysis()


class TestCrashAnalysis(unittest.TestCase):
    """Class for unit testing get_keyword function of the Crash_Analysis module"""

    # test get_period function with valid inputs
    # got predicted number of results from sql queries of the database

    # 4.1 Test a valid keyword result. 
    def test_keyword_analysis_results(self):
        self.assertEqual(len(data.get_keyword("2014-07-01", "2014-07-01", "Rear end")), 3)
        self.assertEqual(len(data.get_keyword("2014-07-01", "2014-07-01", "Ped hit")), 4)
        self.assertEqual(len(data.get_keyword("2014-07-01", "2014-07-01", "struck")), 5)

    # 4.2 Test an invalid keyword.
    def test_keyword_analysis_invalid(self):
        self.assertEqual(len(data.get_keyword("2014-07-01", "2014-07-01", "Cheese Burgers")), 0)
        self.assertEqual(len(data.get_keyword("2014-07-01", "2014-07-01", 9000)), 0)
        self.assertEqual(len(data.get_keyword("2014-07-01", "2014-07-01", 56.74)), 0)

    # 4.3 Test an empty keyword.
    def test_keyword_analysis_empty(self):
        self.assertEqual(len(data.get_keyword("2013-07-01", "2013-07-01", "")), 41)
        self.assertEqual(len(data.get_keyword("2016-12-16", "2017-12-16", "")), 12381)
        self.assertEqual(len(data.get_keyword("2014-07-01", "2014-07-01", "")), 23)

unittest.main()