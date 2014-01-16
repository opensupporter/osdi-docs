# Donation
## Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
|identifiers    |Identifier[] |The OSDI identifiers of this donation
|system			|string		|The donation system. Example: ActBlue
|recipient		|string		|The recipient of the donation. Example: Obama for America
|donor			|Person (model)		|Donor data collected at the time of donation
|donor_identifier|Identifier |The identifier of the donor
|donation_date  |date     	|Date of the donation
|amount			|number		|Amount of total donation (after any credits) in specified currency
|amount_credited|number		|Amount credited back to donor in specified currency
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
|url			|string		|URL at which the donation was taken
|sources			|string[]		|Sources associated with the donation
|attributions	|string[]		|Attributions associated with the donation