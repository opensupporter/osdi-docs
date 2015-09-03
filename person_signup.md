---
layout: default
title: Person Signup Helper
---

# Person Signup Helper

This document defines the Person Signup Helper resource. 

The Person Signup Helper is a helper endpoint to aid in the creation of [People](people.html) resources via POST. It provides a quick and easy way to add people to an OSDI system.

When using the Person Signup Helper, tagging and list membership info may be added at the same time as well, eliminating the need for multiple POST operations to store that information.

Some systems may attempt to match inputs via the Person Signup Helper to existing people in the database and update their record instead of creating a new person for every POST. The method used for matching will be detailed in that system's documentation. 

The response to a successful Person Signup Helper POST is the full representation of the person.

Some initial implementations may only support helpers -- direct RESTful access may not be supported. In those cases, the _links section may be omitted in responses.


### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Person Signup Helper Fields](#person-signup-helper-fields)
    * [Related Objects](#related-objects)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Creating a new person (POST)](#scenario-creating-a-new-person-post)


{% include endpoints_and_url_structures.md %}

The link relation label for the Person Signup Helper is ```osdi:person_signup_helper```.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}


### Person Signup Helper Fields

A list of fields specific for POSTing via the Person Signup Helper.

|Name          |Type      |Description
|-----------    |-----------|--------------
|add_tags      |strings[]     |An array of tag names corresponding to previously created tags to add to this person when it is created.
|add_tags_uri  |strings[]     |An array of tag URIs corresponding to previously created tags to add to this person when it is created.
|add_lists     |strings[]     |An array of list names corresponding to previously created lists to add to this person when it is created.
|person			|[Person*](#person)	|An object hash representing the person to be added.

_[Back to top...](#)_


### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Person

|Name          |Type      |Description
|-----------    |-----------|--------------
|person      |[Person*](people.html)     |An inlined hash representation of a person, containing any valid fields for the Person resource.

_[Back to top...](#)_


## Related Resources

* [Person](people.html)

_[Back to top...](#)_


## Scenarios

{% include scenarios_helper_intro.md %}


### Scenario: Creating a new person (POST)

Posting to the person signup helper endpoint will allow you to create a new person (or update a person if the system attempts to match people posted with helpers) along with associated tags and list membership information in one operation. The response is the person that was created or updated. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/people/person_signup_helper/

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
    "add_tags": [
        "volunteer",
        "donor"
    ],
    "add_tags_uri": [
        "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
    ],
    "add_lists_uri": [
        "https://osdi-sample-system.org/api/v1/lists/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
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
        }
    }
}
```

_[Back to top...](#)_
