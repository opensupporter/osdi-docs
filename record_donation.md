---
layout: default
title: "Record Donation Helper"
---

# Record Donation Helper

This document defines the Record Donation Helper resource. 

The Record Donation Helper is a helper endpoint to aid in the creation of [Donation](donations.html) and [People](people.html) resources via POST. It provides a quick and easy way to create donations and people at the same time, eliminating the need for multiple POST operations to store that information.

Some systems may attempt to match people sent via the Record Donation Helper to existing people in the database and update their record instead of creating a new person. The method used for matching will be detailed in that system's documentation. 

When using the Record Donation Helper, tagging and list membership info may be added at the same time as well, eliminating the need for multiple POST operations to store that information.

In addition, you can indicate to the server whether to trigger additional actions, such as an autoresponse email sent back to the person who took action.

Typically, the response to a successful Record Donation Helper POST is the full representation of the donation. However, the Record Donation Helper can be used without authentication, allowing for use in frontend javascript-based applications without giving away API key secrets, for example. If no authentication is passed, the response on success will simply be the server response code (ex: 200) and an empty JSON object. On error, the server response code (ex: 404, 500) plus an error message may be returned.

Some initial implementations may only support helpers -- direct RESTful access may not be supported. In those cases, the _links section may be omitted in responses.


### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
	* [Common Fields](#common-fields)
    * [Record Donation Helper Fields](#record-donation-helper-fields)
    * [Helper Action Functions](#helper-action-functions)
    * [Related Objects](#related-objects)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Creating a new donation and person (POST)](#scenario-creating-a-new-donation-and-person-post)
    * [Scenario: Creating a new donation and person without authentication (POST)](#scenario-creating-a-new-donation-and-person-without-authentication-post)
    

{% include endpoints_and_url_structures.md %}

The link relation label for the Record Donation Helper is ```osdi:record_donation_helper```.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields_helper.md %}

_[Back to top...](#)_


### Record Donation Helper Fields

A list of fields specific for POSTing via the Record Donation Helper.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this donation was created. (ex: "OSDI System")
|action_date		|string		|The date and time the donation was made by the person.
|amount         |number		| Amount of total donation (after any credits) in specified currency.
|credited_amount|number		| Amount credited back to donor in specified currency.
|credited_date	|datetime	| Date of the credit.
|currency		|string		| ISO 4217 designation of currency. Example: USD, JPY
|recipients		|[Recipient](#recipient)[]| Array of recipients associated with the donation.
|payment		|[Payment](#payment)	| The payment details.
|subscription_instance|string| A sequence number or some other value unique to this instance of the donation in the context of a subscription. Examples: 5, JAN-2014
|voided			|boolean	|Indicates if the donation has been voided.
|voided_date  	|datetime		|Date of the void.
|url			|string		|URL at which the donation was taken.
|referrer_data		|[Referrer Data*](#referrer-data)	|An object hash representing referrer and sourcing information about this donation.
|person			|[Person*](#person)	|An object hash representing the person who made the donation.

_[Back to top...](#)_

### Helper Action Functions

{% include helper_action_functions.md %}

_[Back to top...](#)_



### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.


#### Recipient

An object representing the recipient of a donation.

| Name          | Type      | Description
|-----------    |-----------|--------------
|display_name	|string		|The recipient's display name. Example: Barack Obama
|legal_name		|string		|The recipient's legal name. Example: Obama for America
|amount  		|float	|The amount donated to the recipient.

#### Payment

An object representing the payment details of a donation.

| Name          | Type      | Description
|-----------    |-----------|--------------
|method			|enum		|A flexible enumeration of "Credit Card", "Check", "Cash", or "Electronic Funds Transfer".
|reference_number |string		|A check number, transaction ID, or some other information referencing the payment.
|authorization_stored |boolean	|Indicates if payment information has been stored for future automatic payments.


#### Referrer Data

|Name          |Type      |Description
|-----------    |-----------|--------------
|referrer_data.source	|string    |The source code that was used when this donation was created. Typically used to track individual links, such as a post on social media or a link in a specific email. (ex: "facebook-101016-mainpage")
|referrer_data.referrer	|string    |The code or ID representing a person or group that referred this donation. Typically used to track which person referred the person who made this donation. (ex: "jane-doe")
|referrer_data.website	|string    |The top level domain of the website where the person clicked from to then subsequently make this donation. (ex: "facebook.com")
|referrer_data.url	|string    |The specific URL where the person clicked from to then subsequently make this donation. (ex: "https://facebook.com/posts/12345")

#### Person

|Name          |Type      |Description
|-----------    |-----------|--------------
|person      |[Person*](people.html)     |An inlined hash representation of a person, containing any valid fields for the Person resource.

_[Back to top...](#)_


## Related Resources

* [Donation](donations.html)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_helper_intro.md %}


### Scenario: Creating a new donation and person (POST)

Posting to the record donation helper endpoint will allow you to create a new donation and person (or update a person if the system attempts to match people posted with helpers) in one operation.  Donations created in this manner may also be linked to attendances or submissions, via the relevant property; below, the created donation is linked to an attendance.  The response is the donation that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/record_donation_helper

Header:
OSDI-API-Token:[your api key here]

{
    "person": {
        "identifiers": [
            "foreign_system:1"
        ],
        "family_name": "Edwin",
        "given_name": "Labadie",
        "additional_name": "Marques",
        "origin_system": "OpenSupporter",
        "email_addresses": [
            {
                "address":"test-3@example.com",
                "primary": true,
                "address_type": "Personal"
            }
        ],
        "postal_addresses": [
            {
                "primary": true,
                "address_lines": [
                    "935 Ed Lock"
                ],
                "locality": "New Dudley",
                "region": "MN",
                "postal_code": "17678",
                "country": "RU",
                "address_type": "Home",
                "status": "Verified"
            }
        ],
        "phone_numbers": [
            {
                "primary": true,
                "number": 19876543210,
                "number_type": "Mobile",
                "sms_capable": true
            }
        ],
        "gender": "Male"
    },
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "action_date": "2014-03-18T11:02:15Z",
    "currency": "USD",
    "amount": 40.00,
    "credited_amount": 5.00,
    "credited_date": "2013-04-12T21:42:34",
    "voided": false,
    "voided_date": null,
    "url": "htts://actblue.com/page/BobsCandidates",
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
    "osdi:attendance": {
        "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc"
    },
    "referrer_data": {
        "source": "facebook-101016-mainpage",
        "referrer": "jane-doe",
        "website": "facebook.com",
        "url": "https://facebook.com/posts/12345"
    },
{% include helper_action_examples.md %}
}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
        "foreign_system:1"
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "action_date": "2014-03-18T11:02:15Z",
    "origin_system": "OpenSupporter",
    "currency": "USD",
    "amount": 40.00,
    "credited_amount": 5.00,
    "credited_date": "2013-04-12T21:42:34",
    "voided": false,
    "voided_date": null,
    "url": "htts://actblue.com/page/BobsCandidates",
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
    "referrer_data": {
        "source": "facebook-101016-mainpage",
        "referrer": "jane-doe",
        "website": "facebook.com",
        "url": "https://facebook.com/posts/12345"
    },
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:fundraising_page": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/adb951cb-51f9-420e-b7e6-de953195ec86"
        },
        "osdi:attendance": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc"
        }
    }
}
```

_[Back to top...](#)_

### Scenario: Creating a new donation and person without authentication (POST)

Posting to the record donation helper endpoint without authentication will allow you to create a new donation and person (or update a person if the system attempts to match people posted with helpers) in one operation, but without giving away API key secrets or leaking data, so this method is appropriate for frontend javascript applications. The response on success will simply be the server response code (ex: 200) and an empty JSON object. On error, the server response code (ex: 404, 500) plus an error message may be returned. While each implementing system will require different fields, any optional fields not included in a POST operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/record_donation_helper

{
    "person": {
        "identifiers": [
            "foreign_system:1"
        ],
        "family_name": "Edwin",
        "given_name": "Labadie",
        "additional_name": "Marques",
        "origin_system": "OpenSupporter",
        "email_addresses": [
            {
                "address":"test-3@example.com",
                "primary": true,
                "address_type": "Personal"
            }
        ],
        "postal_addresses": [
            {
                "primary": true,
                "address_lines": [
                    "935 Ed Lock"
                ],
                "locality": "New Dudley",
                "region": "MN",
                "postal_code": "17678",
                "country": "RU",
                "address_type": "Home",
                "status": "Verified"
            }
        ],
        "phone_numbers": [
            {
                "primary": true,
                "number": 19876543210,
                "number_type": "Mobile",
                "sms_capable": true
            }
        ],
        "gender": "Male"
    },
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "action_date": "2014-03-18T11:02:15Z",
    "currency": "USD",
    "amount": 40.00,
    "credited_amount": 5.00,
    "credited_date": "2013-04-12T21:42:34",
    "voided": false,
    "voided_date": null,
    "url": "htts://actblue.com/page/BobsCandidates",
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
    "referrer_data": {
        "source": "facebook-101016-mainpage",
        "referrer": "jane-doe",
        "website": "facebook.com",
        "url": "https://facebook.com/posts/12345"
    },
{% include helper_action_examples.md %}
}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{}
```

_[Back to top...](#)_