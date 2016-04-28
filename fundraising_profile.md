---
layout: default
title: Fundraising Profile
---

# Fundraising Profile
This document describes the integration profile for fundraising. 

### Sections


* [Scenario Overview](#scenario-overview)
* [Related Resources](#related-resources)
* [API Exchanges](#api-exchanges)
    * [Exchange Example: Fundraising application creates a fundraising page in digital organizing system](#exchange-example-fundraising-application-creates-a-fundraising-page-in-digital-organizing-system)
    * [Exchange Example: Fundraising application sends data about donations to the digital organizing system
](#exchange-example-fundraising-application-sends-data-about-donations-to-the-digital-organizing-system)

## Scenario Overview

The Fundraising Integration Profile assumes a common pattern where an OSDI compliant fundraising application is used to raise money from individuals and then reports the data collected while processing the donation (name of person, address, amount donated, etc...) to a digital organizing platform or contact relation management (CRM) system.

The steps in this scenario, are loosely:

1. Fundraising page creation: A user of the fundraising application creates a fundraising page to collect donations.
2. API Exchange: The fundraising application creates a fundraising page on the digital organizing platform corresponding to the one created by the user, to store data as donations are collected. The fundraising application stores the ID or URL of the created fundraising page for later use.
3. Donation collection: People donate on the fundraising page hosted by the fundraising application.
4. API Exchange: The fundraising application sends data about the donation and who made it to the digital organizing platform, using the fundraising page it created in step 2.

_[Back to top...](#)_

## Related Resources

* [Record Donation Helper](record_donation.html)
* [Fundraising Page](fundraising_pages.html)
* [Person](people.html)

_[Back to top...](#)_

## API Exchanges

### Exchange Example: Fundraising application creates a fundraising page in digital organizing system

#### Request

```javascript
POST https://digital-organizing-platform.org/api/v1/fundraising_pages/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "fundraising_application:1"
    ],
    "name": "End Of Year Giving Drive",
    "title": "Give to support us at the end of the year!",
    "origin_system": "FundraisingApplication"
}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "digital_organizing_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
        "fundraising_application:1"
    ],
    "origin_system": "FundraisingApplication",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "End Of Year Giving Drive",
    "title": "Give to support us at the end of the year!",
    "total_donations": 0,
    "total_amount": 0,
    "currency": "USD",
    "_links": {
        "self": {
            "href": "https://digital-organizing-platform.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:donations": {
            "href": "https://digital-organizing-platform.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations"
        },
        "osdi:creator": {
            "href": "https://digital-organizing-platform.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:record_donations_helper": {
            "href": "https://digital-organizing-platform.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/record_donations_helper"
        }
    }
}
```

_[Back to top...](#)_


### Exchange Example: Fundraising application sends data about donations to the digital organizing system

#### Request

```javascript
POST https://digital-organizing-platform.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/record_donation_helper

Header:
OSDI-API-Token:[your api key here]

{
    "person": {
        "family_name": "Edwin",
        "given_name": "Labadie",
        "additional_name": "Marques",
        "email_addresses": [
            {
                "address":"test-3@example.com"
            }
        ],
        "postal_addresses": [
            {
                "address_lines": [
                    "935 Ed Lock"
                ],
                "locality": "New Dudley",
                "region": "MN",
                "postal_code": "17678",
                "country": "US"
            }
        ],
        "phone_numbers": [
            {
                "number": 19876543210
            }
        ]    
    },
    "action_date": "2014-03-18T11:02:15Z",
    "currency": "USD",
    "amount": 40.00,
    "payment": {
        "method": "Credit Card"
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
    "add_tags": [
        "volunteer",
        "donor"
    ]
}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "digital_organizing_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "action_date": "2014-03-18T11:02:15Z",
    "currency": "USD",
    "amount": 40.00,
    "payment": {
        "method": "Credit Card"
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
            "href": "https://digital-organizing-platform.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29/donations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:fundraising_page": {
            "href": "https://digital-organizing-platform.org/api/v1/fundraising_pages/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://digital-organizing-platform.org/api/v1/people/adb951cb-51f9-420e-b7e6-de953195ec86"
        }
    }
}
```

_[Back to top...](#)_