# Most Active Cookie
Write a command line program along with appropriate tests (very important step) in your preferred language to process the log file and return the most active cookie for a specified day.  

Given a cookie log file in the following format:
cookie,timestamp<br/>
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00 <br/>
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00 <br/>
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00 <br/>
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00 <br/>
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00 <br/>
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00 <br/>
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00 <br/>
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00 <br/>
Write a command line program in your preferred language to process the log file and return the most active
cookie for specified day. The example below shows how we&#39;ll execute your program.

Command:
$ ./most_active_cookie cookie_log.csv -d 2018-12-09

Output:
AtY0laUfhglK3lC7
We define the most active cookie as one seen in the log the most times during a given day.

Assumptions:
* If multiple cookies meet that criteria, please return all of them on separate lines.
$ ./most_active_cookie cookie_log.csv -d 2018-12-08
SAZuXPGUrfbcn5UA
4sMM2LxV07bPJzwf
fbcn5UAVanZf6UtG

* You're only allowed to use additional libraries for testing, logging and cli-parsing. There are libraries for most languages which make this too easy (e.g pandas) and we’d like you to show off you coding skills.
* You can assume -d parameter takes date in UTC time zone.
* You have enough memory to store the contents of the whole file.
* Cookies in the log file are sorted by timestamp (most recent occurrence is first line of the file).
