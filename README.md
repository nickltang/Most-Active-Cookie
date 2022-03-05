# Most Active Cookie
## Description
This repository contains a CLI program, `mostactivecookie.py`, that finds and returns the most active cookie(s) in a cookie log csv file, `cookie_log.csv`, for a given date.<br/><br/>

It also contains a testing file, `mostactivecookie_tests.py`, that uses Python's unittest library to test for a specific date, 2018-12-08.  
To test the accuracy of our CLI program in filtering out less active cookies, some cookies for 2018-12-08 are repeated in the given cookie log, `cookie_log.csv`.

## Instructions To Run
Python 3 must be installed in order to run these files.<br/>

**CLI Program:**
* This program takes the CSV filepath and the user's desired date (YYYY-MM-DD format) as arguments
* To run this program, enter `python3 mostactivecookie.py cookie_log.csv -d YYYY-MM-DD` for a given date.
* Example: `python3 mostactivecookie.py cookie_log.csv -d 2018-12-08`<br/>

**Test Program:**
* To run this program, enter `python3 mostactivecookie_tests.py`

## Assignment Description
Write a command line program along with appropriate tests (very important step) in your preferred language to process the log file and return the most active cookie for a specified day.<br/>

**Cookie log file (cookie_log.csv) format:** <br/>
cookie,timestamp <br/>
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00 <br/>
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00 <br/>
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00 <br/>
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00 <br/>
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00 <br/>
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00 <br/>
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00 <br/>
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00 <br/>

**Test Command:**
`$ ./most_active_cookie cookie_log.csv -d 2018-12-09`

**Output:**
AtY0laUfhglK3lC7<br/>

We define the most active cookie as one seen in the log the most times during a given day.<br/>

**Assumptions:**
* If multiple cookies meet that criteria, please return all of them on separate lines.<br/>
$ ./most_active_cookie cookie_log.csv -d 2018-12-08<br/>
  SAZuXPGUrfbcn5UA<br/>
  4sMM2LxV07bPJzwf<br/>
  fbcn5UAVanZf6UtG<br/>
* You're only allowed to use additional libraries for testing, logging and cli-parsing. There are libraries for most languages which make this too easy (e.g pandas) and we’d like you to show off you coding skills.
* You can assume -d parameter takes date in UTC time zone.
* You have enough memory to store the contents of the whole file.
* Cookies in the log file are sorted by timestamp (most recent occurrence is first line of the file).
