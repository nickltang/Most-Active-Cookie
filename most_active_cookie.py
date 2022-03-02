import argparse
import csv

"""
Command: ./most_active_cookie cookie_log.csv -d 2018-12-09

Functions:
- Take CLI arguments for CSV file and date (DONE)
- Parse CSV file into dictionary (DONE)
- Cookies already sorted (DONE) -> is sorting necessary?
- Format timestamp (DONE)
- Retrieve most active cookies from list
- 
"""

program_description = 'This program processes a cookie log file and returns the most active cookie(s) for a specific date.'
infile_help = 'Cookies File to Input - Format: CSV'
date_help = 'Date of Cookie(s) - Format: YYYY-MM-DD'


# Parse CSV into dictionary
def parse_csv_cookies(infile):
    with open(infile) as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        cookies_dict = {rows[0] : format_timestamp(rows[1]) for rows in csv_reader}
    return cookies_dict

# Separate dates from times in CSV timestamps
def format_timestamp(timestamp):
    iso_date = (str(timestamp)).split('T')[0]
    return iso_date

# Search for most active cookie(s) in time frame
def find_cookie(cookies):
    print('Search for most active cookie')
    # Specify by date
    # Count occurrences of each cookie on date
    # Get max occurrences of cookies


def main():
    parser = argparse.ArgumentParser(description = program_description)
    parser.add_argument('infile', help = infile_help)
    parser.add_argument('-d', required = True, help = date_help)

    # Convert parsed arguments into dictionary
    args = vars(parser.parse_args())    

    parsed_cookies = parse_csv_cookies(args['infile'])
    find_cookie(parsed_cookies)

    
if __name__ == '__main__':
    main()