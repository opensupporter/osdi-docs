---
layout: default
title: "Donations"
---

# Donation

This page defines the Donation resource.

## Fields

| Name          | Type      | Description
|-----------    |-----------|--------------
|identifiers    |Identifier[] |An array of OSDI Identifiers for identifying this donation
|created_date	|datetime	| The date and time the resource was created on the local system.
|modified_date	|datetime	| The date and time the resource was modified on the local system.
|origin_system	|string		| Human readable text identifying the system where this donation was created.
|action_date    |datetime   | Date of the donation
|amount         |number		| Amount of total donation (after any credits) in specified currency
|credited_amount|number		| Amount credited back to donor in specified currency
|credited_date	|datetime	| Date of the credit
|currency		|string		| ISO 4217 designation of currency. Example: USD, JPY
|recipients		|Recipient[]| Array of recipients associated with the donation
|payment		|Payment	| The payment details
|subscription_instance|string| A sequence number or some other value unique to this instance of the donation in the context of a subscription. Examples: 5, JAN-2014
|voided			|boolean	|Indicates if the donation has been voided
|voided_date  	|date		|Date of the void
|url			|string		|URL at which the donation was taken
|sources		|string[]   |Array of sources associated with the donation
|attributions	|string[]   |Array of attributions associated with the donation

## Recipient

An object representing the recipient of a donation.

| Name          | Type      | Description
|-----------    |-----------|--------------
|display_name	|string		|The recipient's display name. Example: Barack Obama
|legal_name		|string		|The recipient's legal name. Example: Obama for America
|amount  		|decimal	|The amount donated to the recipient

## Links

| Name          | Type      | Description
|-----------    |-----------|--------------
|modified_by	|Person*	|The Person who last modified the resource.
|donor      	|Person*	|The Person who made the donation.
|fundraising_page|FundraisingPage* |The related fundraising page the donation was taken on



## Payment

An object representing the payment details of a donation.

| Name          | Type      | Description
|-----------    |-----------|--------------
|method			|enum		|A flexible enumeration of "Credit Card", "Check", "Cash", "Electronic Funds Transfer"
|reference_number |string		|A check number, transaction ID, or some other information referencing the payment
|authorization_stored |boolean	|Indicates if payment information has been stored for future automatic payments

# Helpers

Donations are used by the helper methods listed below.

| Name                  | Description
|-----------------------|--------------
|[record_donation_helper](record_donation_helper.md)| Provides a simple method for adding a new donation and a new person to a system at the same time

# Related Resources

* [FundraisingPage](fundraising_page.md)
* [Person](people.md)


# Scenarios

## Scenario: Retrieving a donation

### Request

```
GET /donations/1E840712-CF6D-4BDD-934B-653F4BF6D4DF	
```

### Response


```javascript
200 OK
Content-Type: application/hal+json

{
    "identifiers": ["actblue:1E840712-CF6D-4BDD-934B-653F4BF6D4DF"],
	"created_date": "2013-04-12T20:44:55",
	"modified_date": "2013-04-12T21:42:34",
	"originating_system": "ActBlue",
	"action_date": "2013-04-12T20:44:55",
    "currency": "USD",
	"amount": 40.00,
	"credited_amount": 5.00,
	"credited_date": "2013-04-12T21:42:34",
    "voided": false,
	"voided_date": null,
	"url": "htts://actblue.com/page/BobsCandidates",
	"sources": ["email-your-friends"],
	"attributions": ["JohnSmith", "SusanSmith"],
	"payment": {
		"method": "Credit Card",
		"reference_number": "1232456",
		"authorization_stored": true
	},
	"recipients": [
		{
			"amount": 20.00,
			"display_name": "Barack Obama",
			"legal_name": "Obama for America"
		},
		{
			"amount": 20.00,
			"display_name": "Joe Candidate",
			"legal_name": "Joe for Congress"
		}
	],

    "_links" : {
        "_self": "/donations/1E840712-CF6D-4BDD-934B-653F4BF6D4DF",
		"osdi:modified_by": "/people/c8f802c7-29a6-467c-929e-36b7230a77ab"
		"osdi:donor": "/people/55c25b3c-3b31-4bef-8adc-0023cbac20b3"
        "osdi:fundraising_page": "/fundraisingpages/5f1e063a-a915-4c0d-b5f6-4f299652aa49"
    }
}
```
