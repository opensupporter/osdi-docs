#### Target

|Name          	      |Type                 |Description
|-----------          |-----------          |--------------
|target.title	        |string               |The title or position of the target. (ex: "Senator" or "CEO")
|target.organization	|string	              |The organization the target belongs to. (ex: "U.S. Senate" or "Acme Corporation")
|target.given_name	  |string               |The first or given name of the target. (ex: "John")
|target.family_name	  |string               |The last or family name of the target. (ex: "Smith")
|target.ocdid	        |string               |The Open Civic Data Division ID for this target's political geography, if applicable. See [here](http://docs.opencivicdata.org/en/latest/proposals/0002.html) for more documentation. (ex: "ocd-division/country:us/state:ny/cd:18", which corresponds to New York's 18th Congressional District)
|postal_addresses     |[Postal Addresses[]](#postal-addresses)  |Postal address[es] of the target
|email_addresses	    |[Email Addresses[]](#email-addresses)    |Email address[es] of the target
|phone_numbers	      |[Phone Numbers[]](#phone-numbers)        |Phone number[s] of the target

{% include addresses.md %}