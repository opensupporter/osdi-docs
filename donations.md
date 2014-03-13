# Recipient : Resource
| Name          | Type      | Description
|-----------    |-----------|--------------
|identifiers    |Identifier[] |The OSDI identifiers of this recipient
|created_at	| datetime	| Date and Time of creation
|modified_at	| datetime	| Date and Time of last modification
|display_name	|string		|The recipient's display name. Example: Barack Obama
|legal_name		|string		|The recipient's legal name. Example: Obama for America

# FundraisingPage : Resource
| Name          | Type      | Description
|-----------    |-----------|--------------
|identifiers    |Identifier[] |The OSDI identifiers of this page
|created_at	| datetime	| Date and Time of creation
|modified_at	| datetime	| Date and Time of last modification
|name			|string		|The name of the page
|title			|string		|The title of the page
|description 	|string		|The description of the page
|url			|string	 	|The URL of the fundraising page
|donations_count|int		|Computed value of total donations made to the page
|total_revenue	|decimal	|Computed value of total donation revenue made to this page
|currency		|string		|ISO 4217 designation of currency. Example: USD, JPY
|creator		|Person		|The person representing the creator of the fundraising page
|donations		|Donation Collection|Collection of donations made from this page

# LineItem : ValueType
| Name          | Type      | Description
|-----------    |-----------|--------------
|recipient      |Recipient  |The recipient
|amount			|decimal	|The amount of the donation to this recipient

# Donation : Resource
| Name          | Type      | Description
|-----------    |-----------|--------------
|identifiers    |Identifier[] |The OSDI identifiers of this donation
|created_at	| datetime	| Date and Time of creation
|modified_at	| datetime	| Date and Time of last modification
|originating_system			|string		|The original donation system. Example: ActBlue
|donor			|Person		|Donor data collected at the time of donation
|donation_date  |date     	|Date of the donation
|total_amount	|number		|Amount of total donation (after any credits) in specified currency
|credited_amount|number		|Amount credited back to donor in specified currency
|credited_date	|number		|Date of the credit
|currency		|string		|ISO 4217 designation of currency. Example: USD, JPY
|line_items		|LineItem[]	|The line items associated with the donation
|payment		|hash		|A hash of payment details
|payment.method	|enum		|A flexible enumeration of "Credit Card", "Check", "Cash", "Electronic Funds Transfer"
|payment.reference_number	|string		|A check number, transaction ID, or some other information referencing the payment
|payment.authorization_stored	|boolean	|Indicates if payment information has been stored for future automatic payments
|recurrence		|hash		|A hash detailing the donation's part in a recurrence of other donations
|recurrence.recurring|boolean	|Indicates if the donation is part of a recurring donation series
|recurrence.correlation_key|string	|A common key shared by all recurrences of the donation
|recurrence.instance|string	|A sequence number or some other id unique to this instance of the recurrence. Examples: 5, JAN-2014
|recurrence.period|enum	|Flex enum of "Year", "Month", "Week", etc
|voided			|boolean	|Indicates if the donation has been voided
|voided_date	|date		|Date of the void
|url			|string		|URL at which the donation was taken
|sources			|string[]		|Sources associated with the donation
|attributions	|string[]		|Attributions associated with the donation
|fundraising_page|FundraisingPage |The related fundraising page the donation was taken on


## Donation Wire Example

	GET /donations/5
	{
	    "identifiers": ["trilogy:5"],
	    "total_amount": 50.00,
	    "currency": "USD",
	    "system": "trilogy",
		"line_items": [
			{
				"amount": 25.00,
				"_links": {
					"osdi:recipient": "/recipients/32"
				}
			},
			{
				"amount": 20.00,
				"_links": {
					"osdi:recipient": "/recipients/65"
				}
			},
			{
				"amount": 5.00,
				"_links": {
					"osdi:recipient": "/recipients/124"
				}
			}
		],
	
	    "_links" : {
            "_self": "/donations/5",
			"osdi:creator": "/people/22"
            "osdi:fundraising_page": "/fundraisingpages/2"
	    }
	}
