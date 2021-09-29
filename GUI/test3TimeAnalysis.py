import unittest
from crash_analysis import Crash_Analysis

# Create a Crash_Analysis object
data = Crash_Analysis()


class TestCrashAnalysis(unittest.TestCase):
    """Class for unit testing get_period function of the Crash_Analysis module"""

    # test get_period function with valid inputs
    # got predicted number of results from sql queries of the database

    # 3.1 Test valid input dates returns 24 values. 
    def test_time_analysis_values(self):
        self.assertEqual(len(data.get_time_analysis("2013-07-01", "2013-07-02")), 24)
        self.assertEqual(len(data.get_time_analysis("2016-12-16", "2017-12-16")), 24)
        self.assertEqual(len(data.get_time_analysis("2014-08-16", "2015-12-01")), 24)
        self.assertEqual(len(data.get_time_analysis("2019-02-22", "2019-04-26")), 24)

    # 3.2 Test the total number of accidents returned for the time analysis function.
    def test_time_analysis_total(self):
        self.assertEqual(sum(data.get_time_analysis("2013-07-01", "2013-07-01")), 41)
        self.assertEqual(sum(data.get_time_analysis("2014-07-01", "2014-07-01")), 23)
        self.assertEqual(sum(data.get_time_analysis("2014-08-16", "2015-12-01")), 18507)
        self.assertEqual(sum(data.get_time_analysis("2019-02-22", "2019-04-26")), 379)


    # 3.3 Test the total number of accidents returned for the time analysis function.
    def test_time_analysis_total(self):
        self.assertEqual(data.get_time_analysis("2013-07-01", "2013-07-01"), [0, 0, 1, 0, 1, 1, 2, 1, 2, 2, 1, 0, 1, 1, 1, 4, 5, 6, 5, 4, 0, 2, 1, 0])
        self.assertEqual(data.get_time_analysis("2014-07-01", "2014-07-01"), [0, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 2, 2, 1, 1, 2, 5, 3, 2, 1, 0, 0, 0])
        self.assertEqual(data.get_time_analysis("2019-02-22", "2019-04-26"), [3, 3, 4, 2, 2, 4, 13, 27, 36, 19, 23, 25, 25, 19, 17, 24, 32, 30, 25, 13, 9, 10, 5, 9])

unittest.main()