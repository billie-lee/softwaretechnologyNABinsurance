import unittest
from crash_analysis import Crash_Analysis

# Create a Crash_Analysis object
data = Crash_Analysis()
data.read_data("testdata/crashData.csv")

class TestCrashAnalysis(unittest.TestCase):
    """Class for unit testing get_location_analysis function of the Crash_Analysis module"""
    # test get_period function with valid inputs
    # got predicted number of results from sql queries of the database

    # 6.1 Test return type. 
    def test_location_analysis_return_type(self):
        self.assertIs(type(data.get_location_analysis("2013-07-01", "2013-07-02", "ALPINE")), list)
    
    # 6.2 Test return type contains accident_types
    def test_location_analysis_return_accident_types(self):
        self.assertEqual(data.get_location_analysis("2013-07-01", "2013-07-02", "ALPINE")[0], [
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

    # 6.3 Test return type contains number of accidents
    def test_location_analysis_return_number_of_accidents(self):
        self.assertEqual(data.get_location_analysis("2013-07-13", "2013-07-20", "ALPINE")[1], [1, 0, 1, 0, 0, 0, 0, 0, 0])
        self.assertEqual(data.get_location_analysis("2013-07-13", "2013-07-20", "MELBOURNE")[1], [4, 0, 7, 0, 1, 0, 1, 0, 1])
        self.assertEqual(data.get_location_analysis("2013-07-13", "2013-07-20", "BAYSIDE")[1], [1, 0, 3, 0, 1, 1, 0, 0, 0])

    # 6.4 Test correct number of accidents 
    def test_location_analysis_correct_number_of_accidents(self):
        self.assertEqual(sum(data.get_location_analysis("2013-07-13", "2013-07-20", "ALPINE")[1]), 2)
        self.assertEqual(sum(data.get_location_analysis("2013-07-13", "2013-07-20", "MELBOURNE")[1]), 14)
        self.assertEqual(sum(data.get_location_analysis("2013-07-13", "2013-07-20", "BAYSIDE")[1]), 6)

    # 6.5 Test empty location passed in the function 
    def test_location_analysis_empty_location(self):
        self.assertEqual(sum(data.get_location_analysis("2013-07-13", "2013-07-20", "")[1]), 284) 

    # 6.6 Test invalid location passed in the function 
    def test_location_analysis_invalid_location(self):
        self.assertEqual(sum(data.get_location_analysis("2013-07-13", "2013-07-20", "JAJA")[1]), 0) 
        self.assertEqual(sum(data.get_location_analysis("2013-07-13", "2013-07-20", "INVALID")[1]), 0) 
        self.assertEqual(sum(data.get_location_analysis("2013-07-13", "2013-07-20", "NAB")[1]), 0) 

unittest.main()