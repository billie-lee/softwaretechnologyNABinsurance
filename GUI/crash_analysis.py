"""
Module crash_analysis
    
    This module contains the class Crash_Analysis that is used for reading the 
    Victoria State Accident Data Set into sqlite3.
    It contains functions used for analysis of the data.
    
"""

class Crash_Analysis:
    """Crash_Analysis is for the storage of Victoria State Accident Data Set into sqlite3.
    It contains functions used for analysis of the data."""
    
    def __init__(self) -> None:
        pass

    def iterate_per_accident_type(self, accident_list):

        accident_types = [
            'Collision with a fixed object', 
            'Collision with some other object', 
            'Collision with vehicle', 
            'Fall from or in moving vehicle', 
            'No collision and no object struck', 
            'Other accident', 
            'Struck Pedestrian', 
            'Struck animal', 
            'Vehicle overturned (no collision)'
        ]

        # accidents_per_type contains the number of accidents for each accident type.
        accidents_per_type = []
        for accident in accident_types:
            # accidents is a count of number of accidents found for the hour
            accidents = 0
            for row in accident_list:
                # ACCIDENT_TYPE is at index 7
                type = str(row[7])
                # convert both strings to lowercase for a case insensitive match
                if type.lower() == accident.lower():
                    accidents += 1
            accidents_per_type.append(accidents)
        
        array = [accident_types, accidents_per_type]

        return array

# Method for period search
# Tested = working
    def get_period(self, start_date, end_date):
        """Method searches database table Crash_Data for all information from within a specified period
        Returns a list of all data"""
        import sqlite3
        con =sqlite3.connect("Database/accidents.db")
        cur = con.cursor()
        sql = "SELECT * FROM Crash_Data where ACCIDENT_DATE BETWEEN ? AND ? ORDER by ACCIDENT_DATE ASC;"
        values= (str(start_date), str(end_date))
        # SQL query and a tuple of values are provided to the execute() method. 
        # The ? is replaced with the variable in the tuple in order of occurence.
        cur.execute(sql, values)
        results = cur.fetchall()
        con.close()
        return results

# Method for time analysis
# Tested = working
    def get_time_analysis(self, start_date, end_date):
        """get_time_analysis method returns the number of accidents for each hour of the day (00:00 - 23:00) for a
        specified period"""

        accident_list = self.get_period(start_date, end_date)
        hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

        # accidents_per_hour contains the number of accidents each hour over a 24 hour period.
        accidents_per_hour = []
        for hour in hours:
            # accidents is a count of number of accidents found for the hour
            accidents = 0
            for row in accident_list:
                # index 5 is the time, the slice takes the first two digits. eg 18.30.00 -> 18 
                time = str(row[5][0:2])
                if time == hour:
                    accidents += 1
            accidents_per_hour.append(accidents)

        array = [hours, accidents_per_hour]
        return array


# Method for Alcohol Analysis
# tested = working
    def get_alcohol_analysis(self, start_date, end_date, start_date2, end_date2):
        """Method searches database table Crash_Data for all information from within a specified period
         that is alcohol related. Returns the number of accidents for each accident type"""
         
        import sqlite3
        con =sqlite3.connect("Database/accidents.db")
        cur = con.cursor()
        sql = """
            SELECT * FROM Crash_Data where ACCIDENT_DATE BETWEEN ? AND ?
            AND ALCOHOL_RELATED = ? 
            ORDER by ACCIDENT_TYPE ASC;
        """
        values = (str(start_date), str(end_date), "Yes")
        # SQL query and a tuple of values are provided to the execute() method. 
        # The ? is replaced with the variable in the tuple in order of occurence.
        cur.execute(sql, values)
        accident_list = cur.fetchall()
        con.close()
                
        array = self.iterate_per_accident_type(accident_list)

        con =sqlite3.connect("Database/accidents.db")
        cur = con.cursor()
        sql = """
            SELECT * FROM Crash_Data where ACCIDENT_DATE BETWEEN ? AND ?
            AND ALCOHOL_RELATED = ? 
            ORDER by ACCIDENT_TYPE ASC;
        """
        values = (str(start_date2), str(end_date2), "Yes")
        # SQL query and a tuple of values are provided to the execute() method. 
        # The ? is replaced with the variable in the tuple in order of occurence.
        cur.execute(sql, values)
        accident_list = cur.fetchall()
        con.close()

        array2 = self.iterate_per_accident_type(accident_list)

        result = [array, array2]
        
        return result

# Method for Location Analysis
# tested = working
    def get_location_analysis(self, start_date, end_date, location):       
        """Method searches the database for a specified period and location.
        Returns the number of accidents for each accident type for the specified location and period."""

        import sqlite3
        con =sqlite3.connect("Database/accidents.db")
        cur = con.cursor()
        sql = """
            SELECT * FROM Crash_Data where ACCIDENT_DATE BETWEEN ? AND ? 
            AND LGA_NAME LIKE ? 
            ORDER by ACCIDENT_TYPE ASC;
        """
        # To allow for a case insensitive location search returning any location that contains the query,
        # the % has been place at the beginning and end of the like query. 
        values = (str(start_date), str(end_date), f"%{str(location)}%")
        # SQL query and a tuple of values are provided to the execute() method. 
        # The ? is replaced with the variable in the tuple in order of occurence.
        cur.execute(sql, values)
        accident_list = cur.fetchall()
        con.close()

        array = self.iterate_per_accident_type(accident_list)      
        
        return array

# Method for period/keyword search
# Tested = working
    def get_keyword(self, start_date, end_date, keyword):
        """Method searches database table Crash_Data for all information from within a specified period containing
        an accident type of the specified keyword. Returns a list of data."""
        import sqlite3
        con =sqlite3.connect("Database/accidents.db")
        cur = con.cursor()
        sql = """
            SELECT * FROM Crash_Data 
            where ACCIDENT_DATE BETWEEN ? AND ? 
            AND (ACCIDENT_TYPE like ? OR DCA_CODE like ?) 
            ORDER by ACCIDENT_DATE ASC;
        """
        # Becuase the sql query like requires %keyword%, the keyword is converted to str, then % are placed, to allow
        # the search to match any accident type or definition for classifying accident.
        values= (str(start_date), str(end_date), f"%{str(keyword)}%", f"%{str(keyword)}%")
        # SQL query and a tuple of values are provided to the execute() method.
        # The ? is replaced with the variable in the tuple in order of occurence.
        cur.execute(sql, values)
        results = cur.fetchall()
        con.close()
        return results

# Method to read csv file into sqlite3 database
# tested = working
    def read_data(self, csv_file):
        """Method reads the specified CSV file into a sqlite database by the name of accidents.db"""

        import csv, sqlite3, datetime
        # Establish a connection with sqlite3 and create a database file or connect to one that exists with the same name.

        con =sqlite3.connect("Database/accidents.db")
        cur = con.cursor()

        # Drop previous tables from the database if they exist.
        cur.execute("DROP TABLE IF EXISTS Crash_Data;")
        # Create the Crash_Data table to store the data from the CSV file.
        cur.execute(
            """
            CREATE TABLE Crash_Data (
            OBJECTID integer primary key,
            ACCIDENT_NO varchar,
            ABS_CODE varchar,
            ACCIDENT_STATUS varchar,
            ACCIDENT_DATE varchar,
            ACCIDENT_TIME varchar,
            ALCOHOLTIME varchar,
            ACCIDENT_TYPE varchar,
            DAY_OF_WEEK varchar,
            DCA_CODE varchar, 
            HIT_RUN_FLAG varchar, 
            LIGHT_CONDITION varchar, 
            POLICE_ATTEND varchar, 
            ROAD_GEOMETRY varchar, 
            SEVERITY varchar, 
            SPEED_ZONE varchar, 
            RUN_OFFROAD varchar, 
            NODE_ID varchar, 
            LONGITUDE varchar, 
            LATITUDE varchar, 
            NODE_TYPE varchar, 
            LGA_NAME varchar, 
            REGION_NAME varchar, 
            VICGRID_X varchar, 
            VICGRID_Y varchar, 
            TOTAL_PERSONS varchar, 
            INJ_OR_FATAL varchar, 
            FATALITY varchar, 
            SERIOUSINJURY varchar, 
            OTHERINJURY varchar, 
            NONINJURED varchar, 
            MALES varchar, 
            FEMALES varchar, 
            BICYCLIST varchar, 
            PASSENGER varchar, 
            DRIVER varchar, 
            PEDESTRIAN varchar, 
            PILLION varchar, 
            MOTORIST varchar, 
            UNKNOWN varchar, 
            PED_CYCLIST_5_12 varchar, 
            PED_CYCLIST_13_18 varchar, 
            OLD_PEDESTRIAN varchar, 
            OLD_DRIVER varchar, 
            YOUNG_DRIVER varchar, 
            ALCOHOL_RELATED varchar, 
            UNLICENCSED varchar, 
            NO_OF_VEHICLES varchar, 
            HEAVYVEHICLE varchar, 
            PASSENGERVEHICLE varchar, 
            MOTORCYCLE varchar, 
            PUBLICVEHICLE varchar, 
            DEG_URBAN_NAME varchar, 
            DEG_URBAN_ALL varchar, 
            LGA_NAME_ALL varchar, 
            REGION_NAME_ALL varchar, 
            SRNS varchar, 
            SRNS_ALL varchar, 
            RMA varchar, 
            RMA_ALL varchar, 
            DIVIDED varchar, 
            DIVIDED_ALL varchar, 
            STAT_DIV_NAME varchar
        );"""
        )

        # open the specified CSV file
        file = open(csv_file, 'r')
        # read the data into a dictionary with column headings as keys for each value in a row. 
        crash_data = csv.DictReader(file)
        # List comprehension that loops through crash_data creating a tuple containing the values for each key in a row for every row in the csv file. 
        # row['ACCIDENT_DATE'] is converted from dd-mm-yyyy format to yyyy-mm-dd for storage in the sqlite database.
        data = [(row['OBJECTID'], row['ACCIDENT_NO'], row['ABS_CODE'], row['ACCIDENT_STATUS'], 
        datetime.datetime.strptime(row['ACCIDENT_DATE'], "%d/%m/%Y").strftime("%Y-%m-%d"), 
        row['ACCIDENT_TIME'], row['ALCOHOLTIME'], row['ACCIDENT_TYPE'], row['DAY_OF_WEEK'], row['DCA_CODE'], row['HIT_RUN_FLAG'], 
        row['LIGHT_CONDITION'], row['POLICE_ATTEND'], row['ROAD_GEOMETRY'], row['SEVERITY'], row['SPEED_ZONE'], row['RUN_OFFROAD'], 
        row['NODE_ID'], row['LONGITUDE'], row['LATITUDE'], row['NODE_TYPE'], row['LGA_NAME'], row['REGION_NAME'], 
        row['VICGRID_X'], row['VICGRID_Y'], row['TOTAL_PERSONS'], row['INJ_OR_FATAL'], row['FATALITY'], row['SERIOUSINJURY'], 
        row['OTHERINJURY'], row['NONINJURED'], row['MALES'], row['FEMALES'], row['BICYCLIST'], row['PASSENGER'], row['DRIVER'], 
        row['PEDESTRIAN'], row['PILLION'], row['MOTORIST'], row['UNKNOWN'], row['PED_CYCLIST_5_12'], row['PED_CYCLIST_13_18'], 
        row['OLD_PEDESTRIAN'], row['OLD_DRIVER'], row['YOUNG_DRIVER'], row['ALCOHOL_RELATED'], row['UNLICENCSED'], 
        row['NO_OF_VEHICLES'], row['HEAVYVEHICLE'], row['PASSENGERVEHICLE'], row['MOTORCYCLE'], row['PUBLICVEHICLE'], 
        row['DEG_URBAN_NAME'], row['DEG_URBAN_ALL'], row['LGA_NAME_ALL'], row['REGION_NAME_ALL'], row['SRNS'], row['SRNS_ALL'], 
        row['RMA'], row['RMA_ALL'], row['DIVIDED'], row['DIVIDED_ALL'], row['STAT_DIV_NAME']) for row in crash_data]

        # data contains a tuple of values for every row of data from the csv file.
        # The executemany inserts values for each of the specified fields for each row of data in the variable "data"
        cur.executemany(
            """Insert into Crash_Data (OBJECTID, ACCIDENT_NO, ABS_CODE, ACCIDENT_STATUS, ACCIDENT_DATE, ACCIDENT_TIME, 
            ALCOHOLTIME, ACCIDENT_TYPE, DAY_OF_WEEK, DCA_CODE, HIT_RUN_FLAG, LIGHT_CONDITION, POLICE_ATTEND, ROAD_GEOMETRY, 
            SEVERITY, SPEED_ZONE, RUN_OFFROAD, NODE_ID, LONGITUDE, LATITUDE, NODE_TYPE, LGA_NAME, REGION_NAME, VICGRID_X, 
            VICGRID_Y, TOTAL_PERSONS, INJ_OR_FATAL, FATALITY, SERIOUSINJURY, OTHERINJURY, NONINJURED, MALES, FEMALES, BICYCLIST, 
            PASSENGER, DRIVER, PEDESTRIAN, PILLION, MOTORIST, UNKNOWN, PED_CYCLIST_5_12, PED_CYCLIST_13_18, OLD_PEDESTRIAN, 
            OLD_DRIVER, YOUNG_DRIVER, ALCOHOL_RELATED, UNLICENCSED, NO_OF_VEHICLES, HEAVYVEHICLE, PASSENGERVEHICLE, MOTORCYCLE, 
            PUBLICVEHICLE, DEG_URBAN_NAME, DEG_URBAN_ALL, LGA_NAME_ALL, REGION_NAME_ALL, SRNS, SRNS_ALL, RMA, RMA_ALL, DIVIDED, 
            DIVIDED_ALL, STAT_DIV_NAME) 
            values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", data
        )

        # close csv file, commit the sql queries, and close the connection to sqlite3.
        file.close()
        con.commit()
        con.close()

    def load_data(self):
        import sqlite3
        connection = sqlite3.connect("Database/accidents.db")

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM CRASH_DATA LIMIT 1,100")

        data = cursor.fetchall()

        cursor.close()

        connection.close()

        return data

    def fetch_location(self):
        import sqlite3
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


