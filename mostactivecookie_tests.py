import unittest
import mostactivecookie

class TestActiveCookies(unittest.TestCase):
    infile = './cookie_log.csv'
    testdate = '2018-12-08'
    cookielog_fortestdate = {}

    # Test correct cookies_bydate values for a dummy date.
    def test_dummydate(self):
        cookiefilter = mostactivecookie.CookieFilter({'infile' : self.infile, 'd' : '9999-99-99'})
        cookiefilter.parse_csv_bydate()
        self.assertEqual(cookiefilter.cookies_bydate, {})


    # Test correct cookies_bydate values for given date, 2018-12-08
    def test_filtercookiesbydate(self):
        cookiefilter = mostactivecookie.CookieFilter({'infile' : self.infile, 'd' : '2018-12-08'})
        cookiefilter.parse_csv_bydate()
        self.assertEqual(cookiefilter.cookies_bydate, {'SAZuXPGUrfbcn5UA': '2018-12-08', '4sMM2LxV07bPJzwf': '2018-12-08', 'fbcn5UAVanZf6UtG': '2018-12-08', 'DUPuVLGUrflcn7UB': '2018-12-08'})
    
    
    # Test correct mostactive_cookies values for given date, 2018-12-08
    def test_mostactivecookies(self):
        cookiefilter = mostactivecookie.CookieFilter({'infile' : self.infile, 'd' : '2018-12-08'})
        cookiefilter.parse_csv_bydate()
        cookiefilter.find_maxcookie()
        self.assertEqual(cookiefilter.mostactive_cookies, ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG'])

if __name__ == '__main__':
    unittest.main()