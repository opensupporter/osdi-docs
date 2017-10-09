---
layout: default
title: Person
---

# Person

This document defines the Person resource.

People are individual users who are stored in the OSDI system's database in some way.

People have names, email addresses, and other information, and they have associated action histories recording the actions they've taken on the system, such as a list of their signatures on various petitions.


### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [People Fields](#people-fields)
    * [Related Objects](#related-objects)
    * [Links](#links)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Person resources (GET)](#scenario-retrieving-a-collection-of-person-resources-get)
    * [Scenario: Retrieving an individual Person resource (GET)](#scenario-scenario-retrieving-an-individual-person-resource-get)
    * [Scenario: Creating a new person (POST)](#scenario-creating-a-new-person-post)
    * [Scenario: Modifying a person (PUT)](#scenario-modifying-a-person-put)
    * [Scenario: Deleting a person (DELETE)](#scenario-deleting-a-person-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Person resource is ```osdi:person``` for a single Person resource or ```osdi:people``` for a collection of Person resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### People Fields

A list of fields specific to the Person resource.

|Name          |Type      |Description
|-----------    |-----------|--------------
|family_name      |string     |The person's last name.
|given_name     |string     |The person's first name.
|additional_name    |string     |An additional name not included in family or given. Usually a middle name.
|honorific_prefix           |string    |An honorific prefix like "Dr", "Mr", etc...
|honorific_suffix           |string    |An honorific suffix like "Jr.", "Ph.D", etc...
|gender         |enum     |The gender binary with which a person most closely identifies, or "Other" if the person identifies with neither. One of "Female", "Male", or "Other".
|gender_identity|string     |The self-described gender with which a person identifies. While this field is free-form, data should still follow standardized forms whenever possible (i.e. use "Female" and not "female" or "F"). _Examples: If a person self-identifies as "Female", both_ `gender` _and_ `gender_identity` _fields should have a value of "Female". If a person self-identifies as "Transgender Female",_ `gender` _should have a value of "Female" and_ `gender_identity` _should have a value of "Transgender Female"._
|party_identification   |flexenum     |Flexenum describing the person's politcal party identification. One of "None", "Democratic", "Republican", "Independent", or another free-form string.
|parties |[Parties[]](#parties)|An array of all party object hashes associated with the person (past and present).
|source         |string     |Information about the source where this person record was acquired.   _Example: "facebook-ad-october"_
|ethnicities|strings[]   |A unique string array representing a person's ethnicities.
|languages_spoken|strings[]      | Unique string array of RFC5646 tags representing the languages spoken by the person. Example: en,  en-US, fr-CA, pt-BR
|preferred_language | string  | The RFC5646 tag representing the person's preferred language.
|browser_url		|string		|A URL string pointing to the publicly available person page on the web, such as a public profile page.
|administrative_url		|string		|A URL string pointing to the person's administrative page on the web, such as a page for managing this person's record.
|birthdate	|[Birthdate](#birthdate)    |An object hash representing the birthdate of the person.
|employer|string    |The name of the person's employer.
|employer_address|[Employer Address](#employer-address)    |An object hash representing the postal address of the person's employer.
|postal_addresses      |[Postal Addresses[]](#postal-addresses)   |An array of postal address object hashes associated with the person.
|email_addresses	|[Email Addresses[]](#email-addresses)   |An array of email address object hashes associated with the person.
|phone_numbers	|[Phone Numbers[]](#phone-numbers)   |An array of phone number object hashes associated with the person.
|profiles       | [Profiles[]](#profiles) |An array of profile object hashes for online services related to the person.
|custom_fields	|[Custom Fields](#custom-fields)	|An object hash of key/value pairs associated with the person created by a user rather than a service or vendor.

_[Back to top...](#)_


### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Birthdate

|Name          |Type      |Description
|-----------    |-----------|--------------
|birthdate.month|integer    |An integer representing the month of the birth date of the person.
|birthdate.day  |integer    |An integer representing the day of the birth date of the person.
|birthdate.year|integer     |An integer representing the 4 digit year of the birth date of the person.

#### Parties

|Name          |Type      |Description
|-----------    |-----------|--------------
|parties.identification |flexenum |One of "None", "Democratic", "Republican", "Independent", or another free-form string.
|parties.last_verified_date   |datetime    |A value representing the last verified date of the party registration.
|parties.active   |boolean     |Whether or not this party registration is active for the affiliated person.

#### Employer Address

|Name          |Type      |Description
|-----------    |-----------|--------------
|employer_address.venue	|string	|Optional venue name at the employer address, useful for names of buildings. (ex: Smith Hall)
|employer_address.address_lines	|strings[]	|An array of strings representing the employer's street address.
|employer_address.locality	|string	|A city or other local administrative area.
|employer_address.region	|string	|State or subdivision codes according to ISO 3166-2 (Final 2 alpha digits).
|employer_address.postal_code	|string	|The region specific postal code, such as a zip code.
|employer_address.country	|string	|The country code according to ISO 3166-1 Alpha-2.
|employer_address.language	|string	|Language in which the address is recorded -- language code according to ISO 639.
|employer_address.location	|object	|An object hash representing the geocoded location information for the address.
|employer_address.location.latitude	|float	|A positive or negative float number representing the latitude of the address.
|employer_address.location.longitude	|float	|A positive or negative float number representing the longitude of the address.
|employer_address.location.accuracy	|enum	|A value representing the accuracy of the geocode. One of "Rooftop" or "Approximate".
|employer_address.status	|enum	|A value representing the status of the address. One of "Potential", "Verified", or "Bad".

{% include addresses.md %}

#### Profiles

|Name          |Type      |Description
|-----------    |-----------|--------------
|profiles.provider       | string |The provider name of the profile. _Example: "Facebook"_
|profiles.id       | string |The unique identifier provided by the provider for the profile. _Example: "135165"_
|profiles.url       | string |The URL to the person's web viewable profile. _Example: "http://facebook.com/john.doe"_
|profiles.handle       | string |The handle name of the profile. Twitter handles should not include the "@" _Example: "johndoe"_

#### Custom Fields

|Name          |Type      |Description
|-----------    |-----------|--------------
|custom_fields.[key]	|string	|The key associated with this custom field, with a corresponding value as a string. May be prefixed by servers based on naming conventions they document to control how collisions across systems and data sets occur.

_[Back to top...](#)_


### Links

{% include links_intro.md %}

|Name          	|Type		|Description
|-----------    |-----------|--------------
|self			|[Person*](people.html)	|A self-referential link to the person.
|donations		|[Donations[]*](#)  |A link to the collection of donations associated with the person.
|submissions	|[Submissions[]*](submissions.html)  |A link to the collection of form submissions associated with the person.
|attendances		|[Attendances[]*](attendances.html)        |A link to the collection of event attendances associated with the person.
|signatures		|[Signatures[]*](signatures.html)        |A link to the collection of petition signatures associated with the person.
|outreaches		|[Outreaches[]*](outreaches.html)        |A link to the collection of advocacy campaign outreaches associated with the person.
|answers		|[Answers[]*](answers.html)  |A link to the collection of answers to questions associated with the person.
|taggings		|[Taggings[]*](taggings.html)   	|A link to the collection of taggings associated with the person.
|items		|[Items[]*](items.html)   	|A link to the collection of list items associated with the person.
|memberships		|[Memberships[]*](memberships.html)   	|A link to the collection of memberships associated with the person.
|modified_by		|[Person*](people.html)  	|A link to a Person resource representing the last editor of this person.
|record_canvas_helper |[Record Canvass Helper*](record_canvass.html) | A link to the Record Canvass Helper for this person.

_[Back to top...](#)_


## Helpers

{% include helpers_intro.md %}

|Name          |Description
|-----------    |-----------
|[person_signup_helper](person_signup.html)      |Allows the creation of a person and associated tag and list membership.

_[Back to top...](#)_


## Related Resources

* [Person Signup Helper](person_signup.html)
* [Donation](#)
* [Submission](submissions.html)
* [Attendance](attendances.html)
* [Signature](signatures.html)
* [Answer](answers.html)
* [Tagging](taggings.html)
* [Item](items.html)

_[Back to top...](#)_


## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Person resources (GET)

Person resources are sometimes presented as collections of people. For example, calling the people endpoint will return a collection of all the people stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/people/

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "total_pages": 88,
    "per_page": 25,
    "page": 1,
    "total_records": 2188,
    "_links": {
        "next": {
            "href": "https://osdi-sample-system.org/api/v1/people?page=2"
        },
        "osdi:people": [
            {
                "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/people"
        }
    },
    "_embedded": {
        "osdi:people": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "given_name": "John",
                "family_name": "Smith",
                "honorific_prefix": "Mr.",
                "honorific_suffix": "Ph.D",
                "additional_name": "Scott",
                "gender": "Male",
                "gender_identity": "Male",
                "party_identification": "Democratic",
                "parties": [
                  {
                     "identification": "Democratic",
                     "last_verified_date": "2014-03-20T21:04:31Z",
                     "active": true
                  }
                ],
                "source": "october_canvass",
                "browser_url": "http://osdi-sample-system.org/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                "administrative_url": "http://osdi-sample-system.org/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/manage",
                "birthdate": {
                    "month": 6,
                    "day": 2,
                    "year": 1973
                },
                "ethnicities": [
                    "African American"
                ],
                "languages_spoken": [
                    "en-US",
                    "fr-CA"
                ],
                "preferred_language": "fr-CA",
                "employer": "Acme Corp",
                "employer_address": {
                    "venue": "Bull Hall",
                    "address_lines": [
                        "123 Acme Street",
                        "Suite 400"
                    ],
                    "locality": "New Yorkhaven",
                    "region": "NY",
                    "postal_code": "10001",
                    "country": "US",
                    "language": "en",
                    "location": {
                        "latitude": 38.9382,
                        "longitude": -77.3349,
                        "accuracy": "Rooftop"
                    },
                    "status": "Verified"
                },
                "occupation": "Accountant",
                "postal_addresses": [
                    {
                        "primary": true,
                        "address_type": "Home",
                        "address_lines": [
                            "1900 Pennsylvania Ave"
                        ],
                        "locality": "Washington",
                        "region": "DC",
                        "postal_code": "20009",
                        "country": "US",
                        "language": "en",
                        "location": {
                            "latitude": 38.919,
                            "longitude": -77.0379,
                            "accuracy": "Rooftop"
                        },
                        "last_verified_date": "2014-03-20T21:04:31Z"
                    }
                ],
                "email_addresses": [
                    {
                        "primary": true,
                        "address": "johnsmith@mail.com",
                        "address_type": "Personal",
                        "status": "subscribed"
                    }
                ],
                "phone_numbers": [
                    {
                        "primary": true,
                        "number": "11234567890",
                        "extension": "432",
                        "description": "Worksite line",
                        "number_type": "Work",
                        "operator": "ATT",
                        "country": "US",
                        "sms_capable": false,
                        "do_not_call": true
                    }
                ],
                "profiles": [
                    {
                        "provider": "Facebook",
                        "id": "john.doe.1234",
                        "url": "https://facebook.com/john.doe"
                    },
                    {
                        "provider": "Twitter",
                        "id": "eds34d8j2kddfd45",
                        "url": "https://twitter.com/johndoe",
                        "handle": "johndoe"
                    }
                ],
                "custom_fields": {
                    "is_volunteer": "true",
                    "most_important_issue": "Equal pay",
                    "union_member": "true"
                },
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
                    },
                    "osdi:attendance": {
                        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendance"
                    },
                    "osdi:signatures": {
                        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
                    },
                    "osdi:submissions": {
                        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
                    },
                    "osdi:donations": {
                        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
                    },
                    "osdi:outreaches": {
                        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/outreaches"
                    },
                    "osdi:taggings": {
                        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
                    },
                    "osdi:items": {
                        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/items"
                    },
                    "osdi:record_canvass_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_canvass_helper"
                    }
                }
            },
            {
                "given_name": "Jane",
                "family_name": "Doe",
                "identifiers": [
                    "osdi_sample_system:1efc3644-af25-4253-90b8-a0baf12dbd1e"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T20:44:13Z",
                "modified_date": "2014-03-20T20:44:13Z",
                "browser_url": "http://osdi-sample-system.org/people/1efc3644-af25-4253-90b8-a0baf12dbd1e",
                "administrative_url": "http://osdi-sample-system.org/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/manage",
                "email_addresses": [
                    {
                        "primary": true,
                        "address": "janedoe@mail.com",
                        "status": "unsubscribed"
                    }
                ],
                "postal_addresses": [
                    {
                        "primary": true,
                        "locality": "Washington",
                        "region": "DC",
                        "postal_code": "20009",
                        "country": "US",
                        "language": "en",
                        "location": {
                            "latitude": 38.919,
                            "longitude": -77.0379,
                            "accuracy": "Approximate"
                        }
                    }
                ],
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/answers"
                    },
                    "osdi:attendance": {
                        "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/attendance"
                    },
                    "osdi:signatures": {
                        "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/signatures"
                    },
                    "osdi:submissions": {
                        "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/submissions"
                    },
                    "osdi:donations": {
                        "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/donations"
                    },
                    "osdi:outreaches": {
                        "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/outreaches"
                    },
                    "osdi:taggings": {
                        "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/taggings"
                    },
                    "osdi:items": {
                        "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/items"
                    },
                    "osdi:record_canvass_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/record_canvass_helper"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Person resource (GET)

Calling an individual Person resource will return the resource directly, along with all associated fields and appropriate links to additional information about the person.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/people/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "given_name": "John",
    "family_name": "Smith",
    "honorific_prefix": "Mr.",
    "honorific_suffix": "Ph.D",
    "additional_name": "Scott",
    "gender": "Male",
    "gender_identity": "Male",
    "party_identification": "Democratic",
    "parties": [
      {
        "identification": "Democratic",
        "last_verified_date": "2014-03-20T21:04:31Z",
        "active": true
      }
    ],
    "source": "october_canvass",
    "browser_url": "http://osdi-sample-system.org/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
    "administrative_url": "http://osdi-sample-system.org/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/manage",
    "birthdate": {
        "month": 6,
        "day": 2,
        "year": 1973
    },
    "ethnicities": [
        "African American"
    ],
    "languages_spoken": [
        "en",
        "fr"
    ],
    "employer": "Acme Corp",
    "employer_address": {
        "venue": "Bull Hall",
        "address_lines": [
            "123 Acme Street",
            "Suite 400"
        ],
        "locality": "New Yorkhaven",
        "region": "NY",
        "postal_code": "10001",
        "country": "US",
        "language": "en",
        "location": {
            "latitude": 38.9382,
            "longitude": -77.3349,
            "accuracy": "Rooftop"
        },
        "status": "Verified"
    },
    "occupation": "Accountant",
    "postal_addresses": [
        {
            "primary": true,
            "address_type": "Home",
            "address_lines": [
                "1900 Pennsylvania Ave"
            ],
            "locality": "Washington",
            "region": "DC",
            "postal_code": "20009",
            "country": "US",
            "language": "en",
            "location": {
                "latitude": 38.919,
                "longitude": -77.0379,
                "accuracy": "Rooftop"
            }
        }
    ],
    "email_addresses": [
        {
            "primary": true,
            "address": "johnsmith@mail.com",
            "address_type": "personal",
            "status": "subscribed"
        }
    ],
    "phone_numbers": [
        {
            "primary": true,
            "number": "11234567890",
            "extension": "432",
            "description": "Worksite line",
            "number_type": "Work",
            "operator": "ATT",
            "country": "US",
            "sms_capable": false,
            "do_not_call": true
        }
    ],
    "profiles": [
        {
            "provider": "Facebook",
            "id": "john.doe.1234",
            "url": "https://facebook.com/john.doe"
        },
        {
            "provider": "Twitter",
            "id": "eds34d8j2kddfd45",
            "url": "https://twitter.com/johndoe",
            "handle": "johndoe"
        }
    ],
    "custom_fields": {
        "is_volunteer": "true",
        "most_important_issue": "Equal pay",
        "union_member": "true"
    },
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:attendance": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendance"
        },
        "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
        },
        "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
        },
        "osdi:outreaches": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/outreaches"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        },
        "osdi:items": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/items"
        },
        "osdi:record_canvass_helper": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_canvass_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new person (POST)

Posting to the people collection endpoint will allow you to create a new person. The response is the new person that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

For information on how to link a person with tags and list subscription information in one post, see the [Person Signup Helper](person_signup.html) documentation.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/people/

Header:
OSDI-API-Token:[your api key here]

{
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
            "address_type": "personal",
            "status": "subscribed"
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
    "family_name": "Edwin",
    "given_name": "Labadie",
    "additional_name": "Marques",
    "origin_system": "OpenSupporter",
    "browser_url": "http://osdi-sample-system.org/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
    "administrative_url": "http://osdi-sample-system.org/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/manage",
    "email_addresses": [
        {
            "address":"test-3@example.com",
            "primary": true,
            "address_type": "personal",
            "status": "subscribed"
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
    "gender": "Male",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/answers"
        },
        "osdi:attendance": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/attendance"
        },
        "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/signatures"
        },
        "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/submissions"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/donations"
        },
        "osdi:outreaches": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/outreaches"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/taggings"
        },
        "osdi:items": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/items"
        },
        "osdi:record_canvass_helper": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/record_canvass_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a person (PUT)

You can update a person by calling a PUT operation on that person's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "family_name": "Ed",
    "email_addresses": [
        {
            "address":"test-new@example.com",
            "primary": true,
            "address_type": "personal"
        }
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
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
        "foreign_system:1"
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T22:04:31Z",
    "family_name": "Ed",
    "given_name": "Labadie",
    "additional_name": "Marques",
    "origin_system": "OpenSupporter",
    "browser_url": "http://osdi-sample-system.org/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
    "administrative_url": "http://osdi-sample-system.org/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/manage",
    "email_addresses": [
        {
            "address":"test-new@example.com",
            "primary": true,
            "address_type": "personal",
            "status": "subscribed"
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
    "gender": "Male",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/answers"
        },
        "osdi:attendance": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/attendance"
        },
        "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/signatures"
        },
        "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/submissions"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/donations"
        },
        "osdi:outreaches": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/outreaches"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/taggings"
        },
        "osdi:items": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/items"
        },
        "osdi:record_canvass_helper": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/record_canvass_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a person (DELETE)

You may delete a person by calling the DELETE command on the person's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/people/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This person was successfully deleted."
}
```

_[Back to top...](#)_
