---
layout: default
title: Organization
---

# Organization

This document defines the Organization resource.

Organizations are political/legal entities that generally organize a group of people that are stored in the OSDI system's database in some way.

The Organization resource is as similar as possible to the [Person*](people.html) resource, removing some
fields that only apply to people (e.g. family name, gender identity, etc) and adding others like
legal status and logo. However, the similarities are much greater. Organizations have email and postal addresses,
facebook and twitter pages, etc.  Many systems will store Organizations and People in the same database table and separate them by a type field or otherwise.


### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Organization Fields](#organization-fields)
    * [Common to Person Fields](#common-to-person-fields)
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

The link relation label for a Person resource is ```osdi:organization``` for a single Organization resource or ```osdi:organizations``` for a collection of Organization resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Organization Fields

A list of fields specific to the Organization resource.  A few things are
purposefully distinct from Person and other objects.  For instance,
`organization` for the organization's name is unique so an organization
resource is easily distinguishable from other resource types.

|Name          |Type      |Description
|-----------    |-----------|--------------
|organization  |string     |The organization's human-readable common name. This may not be a full name, if the organization, for instance mostly goes by an acronym -- it should be the value that would be in a listing for the organization and in prose.
|legal_status  |flexenum   |The organization's legal status, or "unofficial" if the organization does not have a corresponding legal entity.  Common values will be "llc", "sole prop", "c3", "c4", and "pac".
|logo_image_url|string     |A URL string pointing to a publicly available image file of the organization's logo. It should be a format supported in the `&lt;img>` html tag.
|site_url      |string     |A URL pointing to the organization's own public homepage.  Whereas `browser_url` (below) may be to a local page contextual to the system, site_url should always be the organization's own site.
|summary       |string     |A short one-line description of the organization. If the `organization` key contains an acronym, this would be where you include the full name.
|description   |string     |A longer description of the organization, possibly contextual to the origin_system the record comes from.

_[Back to top...](#)_


### Common to Person Fields

A list of fields common to the Person resource. These fields are preserved in both so processing data can largely be the same for each.  Some of these fields have different connotations in the Organization resource.  For instance party_identification and languages_spoken are more about the official support/affiliation from the organization rather than about the total or average of all the organization's members.

|Name          |Type      |Description
|-----------    |-----------|--------------
|party_identification   |flexenum     |Flexenum describing the organization's politcal party identification. One of "None", "Democratic", "Republican", etc. Note that this is not about the organization's political 'tilt' but only if it has direct association with the political party
|source         |string     |Information about the source where this organization record was acquired.   _Example: "facebook-ad-october"_
|languages_spoken|strings[]      | Unique string array of RFC5646 tags representing the languages spoken by the organization. Example: en,  en-US, fr-CA, pt-BR
|browser_url		|string		|A URL string pointing to the publicly available organization page on the web, such as a public profile page.
|administrative_url		|string		|A URL string pointing to the organization's administrative page on the web, such as a page for managing this organization's record.
|postal_addresses      |[Postal Addresses[]](#postal-addresses)   |An array of postal address object hashes associated with the organization.
|email_addresses	|[Email Addresses[]](#email-addresses)   |An array of email address object hashes associated with the organization.
|phone_numbers	|[Phone Numbers[]](#phone-numbers)   |An array of phone number object hashes associated with the organization.
|profiles       | [Profiles[]](#profiles) |An array of profile object hashes for online services related to the organization.
|custom_fields	|[Custom Fields](#custom-fields)	|An object hash of key/value pairs associated with the organization created by a user rather than a service or vendor.

_[Back to top...](#)_


### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

{% include addresses.md %}

#### Profiles

|Name          |Type      |Description
|-----------    |-----------|--------------
|profiles.provider       | string |The provider name of the profile. _Example: "Facebook"_
|profiles.id       | string |The unique identifier provided by the provider for the profile. _Example: "135165"_
|profiles.url       | string |The URL to the organization's web viewable profile. _Example: "http://facebook.com/john.doe"_
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
|self			|[Organization*](organizations.html)	|A self-referential link to the organization.
|events		|[Events[]*](#)  |A link to the collection of events the organization has sponsored.
|petitions		|[Petitions[]*](#)  |A link to the collection of petitions the organization has sponsored.
|donations		|[Donations[]*](#)  |A link to the collection of donations associated with the organization.
|submissions	|[Submissions[]*](submissions.html)  |A link to the collection of form submissions associated with the organization.
|attendances		|[Attendances[]*](attendances.html)        |A link to the collection of event attendances associated with the organization.
|signatures		|[Signatures[]*](signatures.html)        |A link to the collection of petition signatures associated with the organization.
|outreaches		|[Outreaches[]*](outreaches.html)        |A link to the collection of advocacy campaign outreaches associated with the organization.
|answers		|[Answers[]*](answers.html)  |A link to the collection of answers to questions associated with the organization.
|taggings		|[Taggings[]*](taggings.html)   	|A link to the collection of taggings associated with the organization.
|items		|[Items[]*](items.html)   	|A link to the collection of list items associated with the organization.
|modified_by		|[Person*](people.html)  	|A link to a Person resource representing the last editor of this organization record.


_[Back to top...](#)_


## Related Resources

* [Petition](#)
* [Event](#)
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

### Scenario: Retrieving a collection of Organization resources (GET)

Organization resources are sometimes presented as collections of organizations. For example, calling the organizations endpoint will return a collection of all the organizations stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/organizations/

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
            "href": "https://osdi-sample-system.org/api/v1/organizations?page=2"
        },
        "osdi:organizations": [
            {
                "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/organizations"
        }
    },
    "_embedded": {
        "osdi:organizations": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "given_name": "John",
                "source": "october_canvass",
                "browser_url": "http://osdi-sample-system.org/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                "administrative_url": "http://osdi-sample-system.org/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/manage",
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
                    "most_important_issue": "Equal pay"
                },
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
                    },
                    "osdi:attendance": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendance"
                    },
                    "osdi:signatures": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
                    },
                    "osdi:submissions": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
                    },
                    "osdi:donations": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
                    },
                    "osdi:outreaches": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/outreaches"
                    },
                    "osdi:taggings": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
                    },
                    "osdi:items": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/items"
                    }
                }
            },
            {
                "given_name": "Jane",
                "identifiers": [
                    "osdi_sample_system:1efc3644-af25-4253-90b8-a0baf12dbd1e"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T20:44:13Z",
                "modified_date": "2014-03-20T20:44:13Z",
                "browser_url": "http://osdi-sample-system.org/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e",
                "administrative_url": "http://osdi-sample-system.org/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e/manage",
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
                        "href": "https://osdi-sample-system.org/api/v1/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e/answers"
                    },
                    "osdi:attendance": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e/attendance"
                    },
                    "osdi:signatures": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e/signatures"
                    },
                    "osdi:submissions": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e/submissions"
                    },
                    "osdi:donations": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e/donations"
                    },
                    "osdi:outreaches": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e/outreaches"
                    },
                    "osdi:taggings": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e/taggings"
                    },
                    "osdi:items": {
                        "href": "https://osdi-sample-system.org/api/v1/organizations/1efc3644-af25-4253-90b8-a0baf12dbd1e/items"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Organization resource (GET)

Calling an individual Organization resource will return the resource directly, along with all associated fields and appropriate links to additional information about the organization.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/organizations/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "source": "october_canvass",
    "browser_url": "http://osdi-sample-system.org/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
    "administrative_url": "http://osdi-sample-system.org/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/manage",
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
        "most_important_issue": "Equal pay"
    },
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:attendance": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendance"
        },
        "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
        },
        "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
        },
        "osdi:outreaches": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/outreaches"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        },
        "osdi:items": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/items"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new organization (POST)

Posting to the organizations collection endpoint will allow you to create a new organization. The response is the new organization that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/organizations/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "given_name": "Labadie",
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
    "modified_date": "2014-03-20T21:04:31Z",
    "given_name": "Labadie",
    "origin_system": "OpenSupporter",
    "browser_url": "http://osdi-sample-system.org/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
    "administrative_url": "http://osdi-sample-system.org/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/manage",
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
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/answers"
        },
        "osdi:attendance": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/attendance"
        },
        "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/signatures"
        },
        "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/submissions"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/donations"
        },
        "osdi:outreaches": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/outreaches"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/taggings"
        },
        "osdi:items": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/items"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a organization (PUT)

You can update a organization by calling a PUT operation on that organization's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "given_name": "Ed",
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
    "given_name": "Labadie",
    "origin_system": "OpenSupporter",
    "browser_url": "http://osdi-sample-system.org/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
    "administrative_url": "http://osdi-sample-system.org/organizations/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/manage",
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
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/answers"
        },
        "osdi:attendance": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/attendance"
        },
        "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/signatures"
        },
        "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/submissions"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/donations"
        },
        "osdi:outreaches": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/outreaches"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/taggings"
        },
        "osdi:items": {
            "href": "https://osdi-sample-system.org/api/v1/organizations/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/items"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a organization (DELETE)

You may delete a organization by calling the DELETE command on the organization's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/organizations/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This organization was successfully deleted."
}
```

_[Back to top...](#)_
