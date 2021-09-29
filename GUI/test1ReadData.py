
# ----Get number of rows of data = 74908 for loaded database, 0 for unloaded.
# select count() from Crash_Data;

# -----old test function
# def get_rows():

#     import sqlite3
#     con =sqlite3.connect("Database/accidents.db")
#     cur = con.cursor()
#     sql = "SELECT * FROM Crash_Data;"
#     cur.execute(sql)
#     results = cur.fetchall()
#     con.close()
#     return len(results)

# rows = get_rows()
# print(rows)


import unittest
from crash_analysis import Crash_Analysis

# Create a Crash_Analysis object
data = Crash_Analysis()


class TestCrashAnalysis(unittest.TestCase):
    """Class for unit testing read_data function of the Crash_Analysis module"""

    # test get_period function with valid inputs
    # got predicted number of results from sql queries of the database

    # 1.1 Testing a valid file for read_data
    def test_read_data_read(self):
        self.assertEqual(data.read_data("testdata/crashData.csv"), "The file was loaded successfully")

    
    # 1.2 Testing a valid file load_data
    def test_read_data_load(self):
        data.read_data("testdata/crashData.csv")
        self.assertEqual(len(data.load_data()), 74908)

    # 1.3 Testing an empty file read_data
    def test_read_data_readempty(self):
        self.assertEqual(data.read_data("testdata/empty.csv"), "The file was loaded successfully")

    # 1.4 Testing an empty file load_data
    def test_read_data_loadempty(self):
        data.read_data("testdata/empty.csv")
        self.assertEqual(len(data.load_data()), 0)


    # 1.5 Testing an incorrect file name or path.
    def test_read_data_path(self):
        self.assertEqual(data.read_data("not a real path"), "The file could not be found, please select another")


unittest.main()