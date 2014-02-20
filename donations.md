# Donation
## Model

| Name          | Type      | Description
|-----------    |-----------|--------------
|identifiers    |Identifier[] |The OSDI identifiers of this donation
|system			|string		|The donation system. Example: ActBlue
|recipient		|string		|The recipient of the donation. Example: Obama for America
|donor			|Person		|Donor data collected at the time of donation (inline)
|donor_resource|Person|Person resource related to the donation
|employment		|hash		|Employment information
|employment.employer|string	|The name of the employer
|employment.occupation|string	|The occupation of the donor
|employment.postal_address|Address	|The postal address of the employer
|donation_date  |date     	|Date of the donation
|amount			|number		|Amount of total donation (after any credits) in specified currency
|amount_credited|number		|Amount credited back to donor in specified currency
|credited_date	|number		|Date of the credit
|currency		|string		|ISO 4217 designation of currency. Example: USD, JPY
|payment		|hash		|A hash of payment details
|payment.method	|enum		|A flexible enumeration of "Credit Card", "Check", "Cash", "Electronic Funds Transfer"
|payment.reference_number	|string		|A check number, transaction ID, or some other information referencing the payment
|payment.authorization_stored	|boolean	|Indicates if payment information has been stored for future automatic payments
|recurrence		|hash		|A hash detailing the donation's part in a recurrence of other donations
|recurrence.recurring|boolean	|Indicates if the donation is part of a recurring donation series
|recurrence.correlation_key|string	|A common key shared by all recurrences of the donation
|recurrence.instance|string	|A sequence number or some other id unique to this instance of the recurrence. Examples: 5, JAN-2014
|voided			|boolean	|Indicates if the donation has been voided
|voided_date	|date		|Date of the void
|url			|string		|URL at which the donation was taken
|sources			|string[]		|Sources associated with the donation
|attributions	|string[]		|Attributions associated with the donation

## POST Scenario (Donor and Donor Resource)
In this scenario, a donation is being created by posting the data to an OSDI server. The client includes transaction data about the donor, along with current donor data from its own system. Between the donation date and the current date, the donor moved and this is reflected in the differing postal addresses.


	POST /api/donations
	{
		"system": "ActBlue",
		"donation_date": "2014-04-21T15:24:13",
		"amount": 25,
		"currency": "USD",
		"recipient": "Candidate for America",
		"payment": {
			"method": "Credit Card",
			"reference_number": "BGV123"
		},
		"voided": false,
		"url": "https://secure.candidateforamerica.com/donate",
		"sources": [ "p2p-email" ],
		"attributions": [ "johnnyboy12" ],
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
		"employment": {
			"employer": "Big Corp.",
			"occupation": "Tester",
			"postal_address": {
				"address_type": "Home",
				"address_lines": [ "1 Corporate Way" ],
				"locality": "Washington",
				"region": "DC",
				"postal_code": "20002"
			}
		},
		"recurrence": {
			"recurring": true,
			"instance": "1",
			"correlation_key": "AB123456"
		}
	}


## POST Scenario (Donor Resource Only)
In this scenario, a donation is being created by posting the data to an OSDI server. The client does not include transaction data about the donor.


	POST /api/donations
	{
		"system": "ActBlue",
		"donation_date": "2014-04-21T15:24:13",
		"amount": 25,
		"currency": "USD",
		"recipient": "Candidate for America",
		"payment": {
			"method": "Credit Card",
			"reference_number": "BGV123"
		},
		"voided": false,
		"url": "https://secure.candidateforamerica.com/donate",
		"sources": [ "p2p-email" ],
		"attributions": [ "johnnyboy12" ],
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
		"employment": {
			"employer": "Big Corp.",
			"occupation": "Tester",
			"postal_address": {
				"address_type": "Home",
				"address_lines": [ "1 Corporate Way" ],
				"locality": "Washington",
				"region": "DC",
				"postal_code": "20002"
			}
		},
		"recurrence": {
			"recurring": true,
			"instance": "1",
			"correlation_key": "AB123456"
		}
	}



## POST Scenario (Donor and Donor Resource Identifier)
In this scenario, a donation is being created by posting the data to an OSDI server. The client includes transaction data about the donor and also the identifier for the donor resource.


	POST /api/donations
	{
		"system": "ActBlue",
		"donation_date": "2014-04-21T15:24:13",
		"amount": 25,
		"currency": "USD",
		"recipient": "Candidate for America",
		"payment": {
			"method": "Credit Card",
			"reference_number": "BGV123"
		},
		"voided": false,
		"url": "https://secure.candidateforamerica.com/donate",
		"sources": [ "p2p-email" ],
		"attributions": [ "johnnyboy12" ],
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
			"identifiers": ["osdimember:1"]
		},
		"employment": {
			"employer": "Big Corp.",
			"occupation": "Tester",
			"postal_address": {
				"address_type": "Home",
				"address_lines": [ "1 Corporate Way" ],
				"locality": "Washington",
				"region": "DC",
				"postal_code": "20002"
			}
		},
		"recurrence": {
			"recurring": true,
			"instance": "1",
			"correlation_key": "AB123456"
		}
	}



## POST Scenario (Donor Resource Identifier)
In this scenario, a donation is being created by posting the data to an OSDI server. The client includes just the donor resource identifier for linking to an existing person.


	POST /api/donations
	{
		"system": "ActBlue",
		"donation_date": "2014-04-21T15:24:13",
		"amount": 25,
		"currency": "USD",
		"recipient": "Candidate for America",
		"payment": {
			"method": "Credit Card",
			"reference_number": "BGV123"
		},
		"voided": false,
		"url": "https://secure.candidateforamerica.com/donate",
		"sources": [ "p2p-email" ],
		"attributions": [ "johnnyboy12" ],
		"donor_resource": {
			"identifiers": ["osdimember:1"]
		},
		"employment": {
			"employer": "Big Corp.",
			"occupation": "Tester",
			"postal_address": {
				"address_type": "Home",
				"address_lines": [ "1 Corporate Way" ],
				"locality": "Washington",
				"region": "DC",
				"postal_code": "20002"
			}
		},
		"recurrence": {
			"recurring": true,
			"instance": "1",
			"correlation_key": "AB123456"
		}
	}