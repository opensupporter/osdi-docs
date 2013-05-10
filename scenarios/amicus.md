# Scenarios
## Amicus

The basic flow of an Amicus/vendor use-case is:

1.  Import a target universe of people
1.  Match Amicus user's and user's friends facebook information to a national file
1.  Using a script with set answers (multiple or single choice) amicus users reach out (mostly call) people on the target universe
1.  We post back the asker/answerer and answers to vendor

It's possible that creating a target universe and interacting with it *on* a vendor is out-of-scope but is perhaps worth thinking about.

We also now support donations, so we'd use that API as well.

An ideal flow might look like:

1.  On amicus user signup, do a MATCH person and save relationship to real-world person on vendor
1.  Create a target universe using a query (POST /universes/ {query: {state: 'PA'}})
1.  Interact with that target universe completely through APIs (match person to universe)
1.  create script on vendor with answers
1.  using API send user's matched person and person from target universe back to vendor.

As far as match is concerned, one important thing to us is the ability to post multiple locations as a possible match.
