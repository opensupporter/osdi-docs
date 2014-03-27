# FundraisingPage : Resource
| Name          | Type      | Description
|-----------    |-----------|--------------
|identifiers    |Identifier[] |The OSDI identifiers of this page
|originating_system	    |string	| Human readable text identifying where this page originated
|created_at	    |datetime	| Date and Time of creation
|modified_at	|datetime	| Date and Time of last modification
|name			|string		|The name of the page
|title			|string		|The title of the page
|summary 		|string		|The summary of the page
|description 	|string		|The description of the page
|url			|string	 	|The URL of the fundraising page
|total_donations|int		|Computed value of total donations made to the page
|total_revenue	|decimal	|Computed value of total donation revenue made to this page
|currency		|string		|ISO 4217 designation of currency. Example: USD, JPY
|creator		|Person*	|The person representing the creator of the fundraising page
|donations		|Donation[] |Collection of donations made from this page

# Recipient : ComplexType
| Name          | Type      | Description
|-----------    |-----------|--------------
|display_name	|string		|The recipient's display name. Example: Barack Obama
|legal_name		|string		|The recipient's legal name. Example: Obama for America
|amount  		|decimal	|The amount donated to the recipient

# Donation : Resource
| Name          | Type      | Description
|-----------    |-----------|--------------
|identifiers    |Identifier[] |The OSDI identifiers of this donation
|created_at	    |datetime	| Date and Time of creation
|modified_at	|datetime	| Date and Time of last modification
|originating_system			|string		|The original donation system. Example: ActBlue
|donor			|Person*    |Donor data collected at the time of donation
|donated_at  |date     	|Date of the donation
|amount         |number		|Amount of total donation (after any credits) in specified currency
|credited_amount|number		|Amount credited back to donor in specified currency
|credited_at	|datetime	|Date of the credit
|currency		|string		|ISO 4217 designation of currency. Example: USD, JPY
|recipients		|Recipient[]|Array of recipients associated with the donation
|payment		|hash		|A hash of payment details
|payment.method	|enum		|A flexible enumeration of "Credit Card", "Check", "Cash", "Electronic Funds Transfer"
|payment.reference_number	|string		|A check number, transaction ID, or some other information referencing the payment
|payment.authorization_stored	|boolean	|Indicates if payment information has been stored for future automatic payments
|subscription_instance|string|A sequence number or some other value unique to this instance of the donation in the context of a subscription. Examples: 5, JAN-2014
|voided			|boolean	|Indicates if the donation has been voided
|voided_at  	|date		|Date of the void
|url			|string		|URL at which the donation was taken
|sources		|string[]   |Array of sources associated with the donation
|attributions	|string[]   |Array of attributions associated with the donation
|fundraising_page|FundraisingPage* |The related fundraising page the donation was taken on 

## Donation Wire Example

```javascript
// GET /donations/5	
{
    "identifiers": ["actblue:5"],
	"created_at": "2013-04-12T20:44:55",
	"modified_at": "2013-04-12T21:42:34",
	"originating_system": "ActBlue",
	"donation_at": "2013-04-12T20:44:55",
    "currency": "USD",
	"amount": 40.00,
	"credited_amount": 5.00,
	"credited_at": "2013-04-12T21:42:34",
    "voided": false,
	"voided_at": null,
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
        "_self": "/donations/5",
		"osdi:donor": "/people/22"
        "osdi:fundraising_page": "/fundraisingpages/2"
    }
}
```