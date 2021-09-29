import unittest
from crash_analysis import Crash_Analysis

# Create a Crash_Analysis object
data = Crash_Analysis()


class TestCrashAnalysis(unittest.TestCase):
    """Class for unit testing fetch_location function of the Crash_Analysis module"""

    # 7.1 Test the return type is a list
    def test_fetch_location_type(self):
        self.assertIs(type(data.fetch_location()), list)


    # 7.2 Test the number of locations returned == 87
    def test_time_analysis_total(self):
        self.assertEqual(len(data.fetch_location()), 87)


    # 7.3 Test the locations returned equal the locations stored in the database.
    def test_time_analysis_number(self):
        self.assertEqual(data.fetch_location(), [
            'MELBOURNE', 'WHITEHORSE', 'BRIMBANK', 'MITCHELL', 'BAW BAW', 'BAYSIDE', 'BOROONDARA', 
            'BANYULE', 'HUME', 'WHITTLESEA', 'GEELONG', 'HOBSONS BAY', 'NILLUMBIK', 'PORT PHILLIP', 
            'DAREBIN', 'YARRA', 'LATROBE', 'MOONEE VALLEY', 'KNOX', 'CASEY', 'BENDIGO', 'FRANKSTON', 
            'EAST GIPPSLAND', 'KINGSTON', 'MAROONDAH', 'BALLARAT', 'CAMPASPE', 'SHEPPARTON', 'MILDURA', 
            'DANDENONG', 'MONASH', 'GOLDEN PLAINS', 'MORNINGTON PENINSULA', 'WYNDHAM', 'CORANGAMITE', 
            'BASS COAST', 'MURRINDINDI', 'STONNINGTON', 'MORELAND', 'MOORABOOL', 'YARRA RANGES', 'MARIBYRNONG', 
            'STRATHBOGIE', 'CARDINIA', 'TOWONG', 'WANGARATTA', 'MELTON', 'SURF COAST', 'SOUTH GIPPSLAND', 
            'HEPBURN', 'SOUTHERN GRAMPIANS', 'GLEN EIRA', 'BENALLA', 'MOYNE', 'COLAC OTWAY', 
            'MACEDON RANGES', 'MOIRA', 'WELLINGTON', 'WEST WIMMERA', 'MANSFIELD', 'LODDON', 'WODONGA', 
            'INDIGO', 'HORSHAM', 'MANNINGHAM', 'NORTHERN GRAMPIANS', 'PYRENEES', 'ALPINE', 'BULOKE', 
            'GANNAWARRA', 'ARARAT', 'WARRNAMBOOL', 'GLENELG', 'SWAN HILL', 'HINDMARSH', 'FALLS CREEK', 
            'MOUNT ALEXANDER', 'CENTRAL GOLDFIELDS', 'MOUNT BULLER', 'MOUNT HOTHAM', 'YARRIAMBIACK', 
            'LAKE MOUNTAIN', 'MOUNT BAW BAW', 'QUEENSCLIFFE', 'MOUNT BULLER ALPINE RESOR', 
            'FRENCH ISLAND', 'MOUNT STIRLING'])

            
unittest.main()