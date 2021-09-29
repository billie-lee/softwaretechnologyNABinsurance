import matplotlib.pyplot as plt
import sqlite3

def fetchData():
    connection = sqlite3.connect("Database/accidents.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM CRASH_DATA")

    data = cursor.fetchall()

    cursor.close()

    return data

def fetchLocation():
    connection = sqlite3.connect("Database/accidents.db")

    cursor = connection.cursor()

    cursor.execute("SELECT DISTINCT LGA_NAME FROM CRASH_DATA")

    data = cursor.fetchall()

    cursor.close()

    locations = []
    for location in data:
        if location[0] != ' ':
            locations.append(location[0])

    return locations
