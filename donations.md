---
layout: default
title: "Donations"
---

# Donation

This document defines the Donation resource. 

Donations are a type of action that a user may take by donating on a fundraising page. Donations have fields to describe them such as when the donation was created, the amount that was donated, and typically are linked to the person who made the donation.

### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Donation Fields](#donation-fields)  
    * [Links](#links)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Donation resources (GET)](#scenario-retrieving-a-collection-of-donation-resources-get)
    * [Scenario: Retrieving an individual Donation resource (GET)](#scenario-scenario-retrieving-an-individual-donation-resource-get)
    * [Scenario: Creating a new donation (POST)](#scenario-creating-a-new-donation-post)
    * [Scenario: Modifying a donation (PUT)](#scenario-modifying-a-donation-put)
    * [Scenario: Deleting a donation (DELETE)](#scenario-deleting-a-donation-delete)

{% include endpoints_and_url_structures.md %}

The link relation label for a Donation resource is ```osdi:donation``` for a single Donation resource or ```osdi:donations``` for a collection of Donation resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


## Donation Fields

| Name          | Type      | Description
|-----------    |-----------|--------------
|origin_system	|string		| Human readable text identifying the system where this donation was created.
|action_date    |datetime   | Date the donation was made.
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

## Related Objects
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


## Links

| Name          | Type      | Description
|-----------    |-----------|--------------
|self			|[Donation*](donations.html)	|A self-referential link to the donation.
|person			|[Person*](people.html)		|A link to a single Person resource representing the person who donated.
|fundraising_page			|[Fundraising Page*](fundraising_pages.html)  		|A link to a Fundraising Page resource representing the fundraising page on which this donation was submitted.

## Helpers

{% include helpers_intro.md %}

| Name                  | Description
|-----------------------|--------------
|[record_donation_helper](record_donation.html)| Provides a simple method for adding a new donation and a new person to a system at the same time.


## Related Resources

* [Record Donation Helper](record_donation.html)
* [Fundraising Page](fundraising_pages.html)
* [Person](people.html)



## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Donation resources (GET)

Donation resources are sometimes presented as collections of donations. For example, calling the donations endpoint on a particular fundraising page will return a collection of all the donations made on that fundraising page.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "total_pages": 10,
    "per_page": 25,
    "page": 1,
    "total_records": 250,
    "_links": {
        "next": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations?page=2"
        },
        "osdi:donations": [
            {
                "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/1efc3644-af25-4253-90b8-a0baf12dbd1e"
            },
            //(truncated for brevity)
        ],
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-sample-system.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations"
        }
    },
    "_embedded": {
        "osdi:donations": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
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
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:fundraising_page": {
                        "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_sample_system:1efc3644-af25-4253-90b8-a0baf12dbd1e"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T20:44:13Z",
                "modified_date": "2014-03-20T20:44:13Z",
                "action_date": "2014-03-12T01:45:34Z",
                "currency": "USD",
                "amount": 5.00,
                "voided": false,
                "voided_date": null,
                "url": "htts://actblue.com/page/BobsCandidates",
                "payment": {
                    "method": "Credit Card",
                    "reference_number": "12324567",
                    "authorization_stored": false
                },
                "recipients": [
                    {
                        "amount": 5.00,
                        "display_name": "Barack Obama",
                        "legal_name": "Obama for America"
                    }
                ],
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:fundraising_page": {
                        "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/adb951cb-51f9-420e-b7e6-de953195ec86"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Donation resource (GET)

Calling an individual Donation resource will return the resource directly, along with all associated fields and appropriate links to additional information about the donation.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
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
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:fundraising_page": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new donation (POST)

Posting to the donations collection endpoint and including a link to an existing Person resource will allow you to create a new donation associated with that fundraising page and person. The response is the new donation that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

For information on how to create a person along with a donation, see the [Record Donation Helper](record_donation.html) documentation.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "action_date": "2014-03-18T11:02:15Z",
    "currency": "USD",
    "amount": 40.00,
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
    "_links" : {
        "osdi:person" : { 
            "href" : "https://actionnetwork.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f" 
        }
    }
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
    "currency": "USD",
    "amount": 40.00,
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
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:fundraising_page": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://actionnetwork.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a donation (PUT)

You can update a donation by calling a PUT operation on that donation's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/

Header:
OSDI-API-Token:[your api key here]

{
    "action_date": "2014-03-17T11:02:15Z"
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
    "modified_date": "2014-03-20T22:04:31Z",
    "action_date": "2014-03-17T11:02:15Z",
    "currency": "USD",
    "amount": 40.00,
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
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:fundraising_page": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://actionnetwork.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a donation (DELETE)

You may delete a donation by calling the DELETE command on the donation's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This donation was successfully deleted."
}
```

_[Back to top...](#)_