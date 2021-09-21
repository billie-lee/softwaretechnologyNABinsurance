import matplotlib.pyplot as plt
import sqlite3

def fetchData():
    connection = sqlite3.connect("Database/accidents.db")

    cursor = connection.cursor()

    cursor.execute("SELECT OBJECTID, ACCIDENT_NO, ABS_CODE, ACCIDENT_STATUS, ACCIDENT_DATE, ACCIDENT_TIME, ALCOHOLTIME, ACCIDENT_TYPE, DAY_OF_WEEK, DCA_CODE FROM CRASH_DATA")

    DATA = cursor.fetchall()

    return DATA
