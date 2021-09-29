from crash_analysis import *

data = Crash_Analysis()

# -----------test for get_keyword(self, start_date, end_date, keyword)
# results = data.get_keyword("2014-07-01", "2014-07-01", "Rear end")
# print(len(results))

# results = data.get_keyword("2014-07-01", "2014-07-01", "Ped hit")
# print(len(results))

# results = data.get_keyword("2014-07-01", "2014-07-01", "struck")
# print(len(results))


# def fetch_location(self): # pragma: no cover
#     import sqlite3
#     connection = sqlite3.connect("Database/accidents.db")

#     cursor = connection.cursor()

#     cursor.execute("SELECT DISTINCT LGA_NAME FROM CRASH_DATA")

#     data = cursor.fetchall()

#     cursor.close()

#     # get locations out of the tuple and into an array
#     locations = []
#     for location in data:
#         if location[0] != ' ':
#             locations.append(location[0])

#     # clean the location by removing all non alphabetical characters.
#     clean_location = []
#     for i in locations:
#         words = i.split()
#         suburb = ""
#         for word in words:
#             for c in word:
#                 if c.isalpha():
#                     suburb += c
#             suburb += " "
#         clean_location.append(suburb.strip())

#     return clean_location


data = Crash_Analysis()
locations = data.fetch_location()
print(locations)
print(len(locations))