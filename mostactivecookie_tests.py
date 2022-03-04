import unittest
import mostactivecookie

class TestActiveCookies(unittest.TestCase):
    infile = 'coookie_log.csv'
    testdate = '2018-12-08'

    def test_validdate(self):
        cookiefilter = mostactivecookie.CookieFilter({'infile' : self.infile, 'd' : '9999-99-99'})

        self.assertEqual(cookiefilter.cookies_bydate, 'FOO')

    def test_validfilepath(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_filtercookiesbydate(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_mostactivecookies(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()