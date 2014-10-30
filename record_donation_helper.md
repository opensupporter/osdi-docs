---
layout: default
title: "Record Donation Helper"
---

# Record Donation Helper

The Record Donation Helper provides a simple method for adding a new donation and a new person to a system at the same time. 

The Record Donation Helper URL can be determined from the fundraising page under the "record_donations_helper" link relation.  The system's default donation record helper should be found on the API Entry Point (AEP)

The response to a Record Donation Helper is the full representation of the donation, with a link to the person resource created and an optional embedded person resource.

Some initial implementations may only support helpers, direct RESTful access may not be supporter.  In those cases,_links may be omitted in responses.

# Parameters

The Record Donation Helper takes the following parameters

| Name          | Type      | Description
|-----------    |-----------|--------------
|donor      |Person |The donor for this donation
|donation	|Donation	|The donation

# Related Resources

* [Donation](donations.md)
* [Person](people.md)

# Scenarios

## Scenario: Use the helper to create a donation and person

### Request

```javascript
// POST /api/v1/donations/record_donations_helper

{
	"amount" : 500.00,
	"origin_system" : "ActBlue",
	"recipients": [
		{
			"display_name" : "Tom for President",
			"legal_name" : "Campaign To Elect Tom",
			"amount" : 500.00
		}
	],
	"donor" : {
		"family_name" : "Smith",
		"given_name" : "John",
		"postal_addresses" : [ {
			"address_lines": [ "123 Main St. NW" ],
			"locality" : "Washington",
			"region" : "DC" 
			"postal_code" : "20009" 
		} ],
		"email_addresses" : [ { "address" : "jsmith@opensupporter.org" } ]
	}
} 

```

### Response

```javascript
200 OK

Content-Type: application/hal+json

{
	"identifiers": [
		"free_fundraisers:2",
		"osdi_system:38ec0365-f996-42a0-b26a-dbed24cf927f"
	],
	"origin_system": "FreeFundraisers.com",
	"created_at": "2014-03-27T17:58:45Z",
	"modified_at": "2014-03-27T17:58:45Z",
	"currency": "USD",
	"total_amount": 3.00,
	"recipients": [
		{
			"name": "Campaign To Elect Tom",
			"amount": 3.00
		}
	],
	"payment": {
		"method": "Credit Card",
		"reference_number": "38ec0365-f996-42a0-b26a-dbed24cf927f",
		"authorization_stored": false
	},
	"_links": {
	"self": {
		"href": "/api/v1/donations/38ec0365-f996-42a0-b26a-dbed24cf927f"
	},
	"osdi:person": {
		"href": "/api/v1/people/17be9a36-bb9a-4f68-94a8-40523b9dab27"
	}
}

```

