import unittest
from crash_analysis import Crash_Analysis

# Create a Crash_Analysis object
data = Crash_Analysis()
data.read_data("testdata/crashData.csv")

class TestCrashAnalysis(unittest.TestCase):
    """Class for unit testing get_period and load_data functions of the Crash_Analysis module"""

    # test get_period function with valid inputs
    # got predicted number of results from sql queries of the database

    # 2.1 Testing valid date inputs.
    def test_get_period_valid(self):
        self.assertEqual(len(data.get_period("2013-07-01", "2013-07-02")), 78)
        self.assertEqual(len(data.get_period("2016-12-16", "2017-12-16")), 12381)
        self.assertEqual(len(data.get_period("2014-08-16", "2015-12-01")), 18507)
        self.assertEqual(len(data.get_period("2019-02-22", "2019-04-26")), 379)

    # 2.2 Testing dates not within recorded data range.
    def test_get_period_outside(self):
        self.assertEqual(len(data.get_period("2012-07-01", "2012-07-02")), 0)
        self.assertEqual(len(data.get_period("2011-12-16", "2011-12-16")), 0)
        self.assertEqual(len(data.get_period("2022-08-16", "2022-12-01")), 0)
        self.assertEqual(len(data.get_period("2021-02-22", "2021-04-26")), 0)

    # 2.3 Test with empty start and end dates
    def test_get_period_empty(self):
        self.assertEqual(len(data.get_period("", "")), 0)
    
    # 2.4 Test with empty start date but valid end dates
    def test_get_period_start(self):
        self.assertEqual(len(data.get_period("", "2013-07-02")), 78)
        self.assertEqual(len(data.get_period("", "2014-07-02")), 14102)
        self.assertEqual(len(data.get_period("", "2013-08-02")), 1183)

    # 2.5 Test with empty end but valid start date.
    def test_get_period_end(self):
        self.assertEqual(len(data.get_period("2013-07-02", "")), 0)
        self.assertEqual(len(data.get_period("2014-07-02", "")), 0)
        self.assertEqual(len(data.get_period("2013-08-02", "")), 0)

    # 2.6 Test if integer is passed into the start and end date fields.
    # SQL treats the number as the first digit of the year, so 2 would be 2000 (thats why 2,3 returns all data entries)
    def test_get_period_int(self):
        self.assertEqual(len(data.get_period(34, 56)), 0)
        self.assertEqual(len(data.get_period(3456, 23424)), 0)
        self.assertEqual(len(data.get_period(2, 7)), 74908)
        self.assertEqual(len(data.get_period(2, 3)), 74908)

    # 2.7 Test if float is passed into the start and end date fields.
    # SQL treats the number as the first digit of the year, so 2 would be 2000 (thats why 1.23, 9.999 returns all data entries)
    def test_get_period_float(self):
        self.assertEqual(len(data.get_period(23.4, 45.3)), 0)
        self.assertEqual(len(data.get_period(0.007, 3.4)), 74908)
        self.assertEqual(len(data.get_period(1.23, 9.999)), 74908)


unittest.main()