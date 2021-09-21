import matplotlib.pyplot as plt
import sqlite3

def fetchData():
    connection = sqlite3.connect("Database/accidents.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM CRASH_DATA LIMIT 1,10")

    DATA = cursor.fetchall()

    return DATA