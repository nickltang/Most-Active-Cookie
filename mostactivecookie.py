import argparse
import csv

class CookieFilter:
    def __init__(self, args):
        self.infile = args['infile']
        self.date = args['d']

    cookie_count = {}
    cookies_bydate = {}
    mostactive_cookies = []


    # Parse cookies from CSV into dictionary if date matches
    def parse_csv_bydate(self):
        with open(self.infile) as csv_file:
            csv_reader = csv.reader(csv_file)
            # Remove CSV header row
            header = next(csv_reader)
            
            for rows in csv_reader:
                rowdate_formatted = self.format_timestamp(rows[1])

                if(rowdate_formatted == self.date):
                    self.cookies_bydate.update({rows[0] : rowdate_formatted})

                    # Update cookie_count dictionary with number of occurrences for given date
                    if(rows[0] in self.cookie_count):
                        self.cookie_count[rows[0]] = self.cookie_count.get(rows[0]) + 1
                    else:
                        self.cookie_count.update({rows[0] : 1})

    # Separate dates from times in CSV timestamps
    def format_timestamp(self, timestamp):
        iso_date = (str(timestamp)).split('T')[0]
        return iso_date

    # Search for most active cookie(s) in time frame
    def find_maxcookie(self):
        max_count = max(self.cookie_count.values())

        for key,value in self.cookie_count.items():
            if value == max_count:
                print(key)
                self.mostactive_cookies.append(key)
    

def main():
    program_description = 'This program processes a cookie log file and returns the most active cookie(s) for a specific date.'
    infile_help = 'Cookies File to Input - Format: CSV'
    date_help = 'Date of Cookie(s) - Format: YYYY-MM-DD'

    parser = argparse.ArgumentParser(description = program_description)
    parser.add_argument('infile', help = infile_help)
    parser.add_argument('-d', required = True, help = date_help)
    args = vars(parser.parse_args())

    mostactivecookies = CookieFilter(args)
    mostactivecookies.parse_csv_bydate()
    mostactivecookies.find_maxcookie()

    
if __name__ == '__main__':
    main()