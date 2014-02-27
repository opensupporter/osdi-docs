# Resource Relations and Inline Writes

When writing data to a server, plain JSON should be used with related resources posted inline and following a naming convention. The server is responsible for disambiguation and the creation of related resources when appropriate.

Related resources should follow the naming convention of "instance_resource." For example, donor_resource, creator_resource, attendee_resource, etc. This convention allows inline-transaction data to use the same name without the "_resource" suffix where appropriate. A donor, for example, may have both a donor_resource field, and a donor field, with the donor field representing transactional data and the donor_resource field relating to a person resource that is updated independently of the donation. 

## Example #1: Posting a Donation with donor and donor_resource data

In this scenario, a donation is being created by posting the data to an OSDI server. The client includes transaction data about the donor, along with current donor data from its own system. Between the donation date and the current date, the donor moved and this is reflected in the differing postal addresses.

	POST /api/donations

	{
		"system": "ActBlue",
		"recipient" : "Obama for America",
		"donor": {
			"given_name": "Sample",
			"family_name": "Donor",
			"email_addresses": "[ { "address": "sample_donor@opensupporter.org" } ]",
			"postal_addresses": [
				{
					"address_type": "Home",
					"address_lines": [ "123 Main St. NW", "APT 4" ],
					"locality": "Washington",
					"region": "DC",
					"postal_code": "20010"
				}
			]
		},
		"donor_resource": {
			"identifiers": ["osdimember:1"],
			"given_name": "Sample",
			"family_name": "Donor",
			"email_addresses": "[ { "address": "sample_donor@opensupporter.org" } ]",
			"postal_addresses": [
				{
					"address_type": "Home",
					"address_lines": [ "456 Main St. NW" ],
					"locality": "Washington",
					"region": "DC",
					"postal_code": "20010"
				}
			],
			"phone_numbers": [ { "number": "12025555555", "number_type": "Mobile" } ]
		},
	    "donation_date" : "2013-11-19T08:37:48-0600",
	    "amount" : 50.00,
	    "currency" : "USD",
		// Other fields omitted
	}

Result:

	201 Created : "http://opensupporter.org/api/v1/donations/1"

	GET /api/v1/donations/1

	{
		"identifiers": ["osdimember:1"],
		"system": "ActBlue",
		"recipient" : "Obama for America",
		"donor": {
			"given_name": "Sample",
			"family_name": "Donor",
			"email_addresses": "[ { "address": "sample_donor@opensupporter.org" } ]",
			"postal_addresses": [
				{
					"address_type": "Home",
					"address_lines": [ "123 Main St. NW", "APT 4" ],
					"locality": "Washington",
					"region": "DC",
					"postal_code": "20010"
				}
			]
		}
	    "donation_date" : "2013-11-19T08:37:48-0600",
	    "amount" : 50.00,
	    "currency" : "USD",
		// Other fields omitted

		"_links" : {
			"self" : "http://opensupporter.org/api/v1/donations/1",
			"donor_resource" : "http://opensupporter.org/api/v1/people/1"
		}
	}


Also, the person's donation links has been updated:

	GET /api/v1/people/1/donations

	{
	    "_links": {
	        "self": "http://osdi.trilogyinteractive.com/api/v1/people/1/donations",
	        "donations": [
	            "href": "http://osdi.trilogyinteractive.com/api/v1/donations/1"
	        ]
	    }
	}


## Example #2: Posting a resource with multiple resource references

In place of full inline resources, a client may send just the identifiers, instructing the server to use the existing related resources.

	POST /api/events

	{
		"summary": "Sample Event",
		"creator_resource": {
			"identifiers": ["osdimember:1"]
		},
		"organizer_resource": {
			"identifiers": ["osdimember:2"]		
		}
		// Other fields omitted
	}

Result:

	201 Created : "http://opensupporter.org/api/v1/events/1"

	GET /api/v1/events/1

	{
		"identifiers": ["osdimember:1"],
		"summary": "Sample Event",
		// Other fields omitted

		"_links" : {
			"self" : "http://opensupporter.org/api/v1/events/1",
			"creator_resource" : "http://opensupporter.org/api/v1/people/1",
			"organizer_resource" : "http://opensupporter.org/api/v1/people/2"
		}
	}