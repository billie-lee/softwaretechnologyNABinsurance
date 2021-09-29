import unittest
from crash_analysis import Crash_Analysis

# Create a Crash_Analysis object
data = Crash_Analysis()
data.read_data("testdata/crashData.csv")

class TestCrashAnalysis(unittest.TestCase):
    """Class for unit testing get_alcohol_analysis function of the Crash_Analysis module"""
    # test get_period function with valid inputs
    # got predicted number of results from sql queries of the database

    # 5.1 Test return type. 
    def test_alcohol_analysis_return_type(self):
        self.assertIs(type(data.get_alcohol_analysis("2013-07-01", "2013-07-02", "2013-08-10", "2013-08-30")), list)

    # 5.2 Test return contains list. 
    def test_alcohol_analysis_return_contain_list_index_0(self):
        self.assertIs(type(data.get_alcohol_analysis("2013-07-01", "2013-07-02", "2013-08-10", "2013-08-30")[0]), list)
    
    # 5.3 Test return contains list. 
    def test_alcohol_analysis_return_contain_list_index_1(self):
        self.assertIs(type(data.get_alcohol_analysis("2013-07-01", "2013-07-02", "2013-08-10", "2013-08-30")[1]), list)
    
    # 5.4 Test return type contains accident_types
    def test_alcohol_analysis_return_accident_types(self):
        self.assertEqual(data.get_alcohol_analysis("2013-07-01", "2013-07-02", "2013-08-10", "2013-08-30")[0][0], [
            'Collision with a fixed object', 
            'Collision with some other object', 
            'Collision with vehicle', 
            'Fall from or in moving vehicle', 
            'No collision and no object struck', 
            'Other accident', 
            'Struck Pedestrian', 
            'Struck animal', 
            'Vehicle overturned (no collision)'
        ])
        self.assertEqual(data.get_alcohol_analysis("2013-07-01", "2013-07-02", "2013-08-10", "2013-08-30")[1][0], [
            'Collision with a fixed object', 
            'Collision with some other object', 
            'Collision with vehicle', 
            'Fall from or in moving vehicle', 
            'No collision and no object struck', 
            'Other accident', 
            'Struck Pedestrian', 
            'Struck animal', 
            'Vehicle overturned (no collision)'
        ])

    # 5.5 Test return type contains number of accidents
    def test_alcohol_analysis_return_number_of_accidents(self):
        self.assertEqual(data.get_alcohol_analysis("2013-07-01", "2013-07-02", "2013-08-10", "2013-08-30")[0][1], [1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(data.get_alcohol_analysis("2013-07-13", "2013-07-15", "2013-08-10", "2013-08-30")[0][1], [4, 0, 1, 0, 0, 0, 0, 0, 0])
        self.assertEqual(data.get_alcohol_analysis("2013-07-17", "2013-07-19", "2013-08-10", "2013-08-30")[0][1], [1, 0, 2, 0, 1, 0, 0, 0, 0])
        self.assertEqual(data.get_alcohol_analysis("2013-07-01", "2013-07-02", "2013-08-10", "2013-08-12")[1][1], [3, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(data.get_alcohol_analysis("2013-07-13", "2013-07-15", "2013-08-15", "2013-08-20")[1][1], [5, 0, 1, 0, 1, 0, 0, 0, 2])
        self.assertEqual(data.get_alcohol_analysis("2013-07-17", "2013-07-19", "2013-08-22", "2013-08-30")[1][1], [6, 0, 4, 0, 1, 0, 1, 0, 0])

    # 5.6 Test correct number of accidents 
    def test_alcohol_analysis_correct_number_of_accidents(self):
        self.assertEqual(sum(data.get_alcohol_analysis("2013-07-01", "2013-07-02", "2013-08-10", "2013-08-30")[0][1]), 1)
        self.assertEqual(sum(data.get_alcohol_analysis("2013-07-13", "2013-07-15", "2013-08-10", "2013-08-30")[0][1]), 5)
        self.assertEqual(sum(data.get_alcohol_analysis("2013-07-17", "2013-07-19", "2013-08-10", "2013-08-30")[0][1]), 4)
        self.assertEqual(sum(data.get_alcohol_analysis("2013-07-01", "2013-07-02", "2013-08-10", "2013-08-12")[1][1]), 3)
        self.assertEqual(sum(data.get_alcohol_analysis("2013-07-13", "2013-07-15", "2013-08-15", "2013-08-20")[1][1]), 9)
        self.assertEqual(sum(data.get_alcohol_analysis("2013-07-17", "2013-07-19", "2013-08-22", "2013-08-30")[1][1]), 12)

unittest.main()