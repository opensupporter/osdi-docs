# Scenarios
## Outreach campaign with survey questions

The basic flow of an outreach campaign:

1.  Import a target universe of people (mass export probably, see notes though)
1.  Match user's and user's friends' facebook information to a data file using the MATCH api (see notes)
1.  Using a script with set answers (multiple or single choice), users reach out people on the target universe. Various techniques may be used to reach out (email, call, direct mail, etc)
1.  Post back asker/answerer and answers to vendor.  If script includes donations then use donation API


### Notes

* As far as match is concerned, one important thing to us is the ability to post multiple locations as a possible match.
* It's possible that creating a target universe and interacting with it *on* a vendor is out-of-scope but is perhaps worth thinking about.
