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
        self.assertEqual(data.fetch_location(), ['ALPINE', 'ARARAT', 'BALLARAT', 'BANYULE', 'BASS COAST', 
        'BAW BAW', 'BAYSIDE', 'BENALLA', 'BENDIGO', 'BOROONDARA', 'BRIMBANK', 'BULOKE', 'CAMPASPE', 
        'CARDINIA', 'CASEY', 'CENTRAL GOLDFIELDS', 'COLAC OTWAY', 'CORANGAMITE', 'DANDENONG', 'DAREBIN', 
        'EAST GIPPSLAND', 'FALLS CREEK', 'FRANKSTON', 'FRENCH ISLAND', 'GANNAWARRA', 'GEELONG', 
        'GLEN EIRA', 'GLENELG', 'GOLDEN PLAINS', 'HEPBURN', 'HINDMARSH', 'HOBSONS BAY', 'HORSHAM', 
        'HUME', 'INDIGO', 'KINGSTON', 'KNOX', 'LAKE MOUNTAIN', 'LATROBE', 'LODDON', 'MACEDON RANGES', 
        'MANNINGHAM', 'MANSFIELD', 'MARIBYRNONG', 'MAROONDAH', 'MELBOURNE', 'MELTON', 'MILDURA', 
        'MITCHELL', 'MOIRA', 'MONASH', 'MOONEE VALLEY', 'MOORABOOL', 'MORELAND', 'MORNINGTON PENINSULA', 
        'MOUNT ALEXANDER', 'MOUNT BAW BAW', 'MOUNT BULLER', 'MOUNT BULLER ALPINE RESOR', 'MOUNT HOTHAM', 
        'MOUNT STIRLING', 'MOYNE', 'MURRINDINDI', 'NILLUMBIK', 'NORTHERN GRAMPIANS', 'PORT PHILLIP', 
        'PYRENEES', 'QUEENSCLIFFE', 'SHEPPARTON', 'SOUTH GIPPSLAND', 'SOUTHERN GRAMPIANS', 'STONNINGTON', 
        'STRATHBOGIE', 'SURF COAST', 'SWAN HILL', 'TOWONG', 'WANGARATTA', 'WARRNAMBOOL', 'WELLINGTON', 
        'WEST WIMMERA', 'WHITEHORSE', 'WHITTLESEA', 'WODONGA', 'WYNDHAM', 'YARRA', 'YARRA RANGES', 
        'YARRIAMBIACK'])

            
unittest.main()