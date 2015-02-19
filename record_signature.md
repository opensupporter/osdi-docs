---
layout: default
title: Record Signature Helper
---

# Record Signature Helper

This document defines the Record Signature Helper resource. 

The Record Signature Helper is a helper endpoint to aid in the creation of [Signature](signatures.html) and [People](people.html) resources via POST. It provides a quick and easy way to create signatures and people at the same time, eliminating the need for multiple POST operations to store that information.

Some systems may attempt to match people sent via the Record Signature Helper to existing people in the database and update their record instead of creating a new person. The method used for matching will be detailed in that system's documentation. 

The response to a Record Signature Helper POST is the full representation of the signature.

Some initial implementations may only support helpers -- direct RESTful access may not be supported. In those cases, the _links section may be omitted in responses.


### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
	* [Common Fields](#common-fields)
    * [Record Signature Helper Fields](#record-signature-helper-fields)
    * [Related Objects](#related-objects)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Creating a new signature and person (POST)](#scenario-creating-a-new-signature-and-person-post)


{% include endpoints_and_url_structures.md %}

The link relation label for the Record Signature Helper is ```osdi:record_signature_helper```.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields_helper.md %}

_[Back to top...](#)_


### Record Signature Helper Fields

A list of fields specific for POSTing via the Record Signature Helper.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this signature was created. (ex: "OSDI System")
|action_date		|string		|The date and time the signature was made by the person.
|comments		|string			|The comments left by the person when the signature was created.
|person			|[Person*](#person)	|An object hash representing the person who made the submission.

_[Back to top...](#)_


### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Person

|Name          |Type      |Description
|-----------    |-----------|--------------
|person      |[Person*](people.html)     |An inlined hash representation of a person, containing any valid fields for the Person resource.

_[Back to top...](#)_


## Related Resources

* [Signature](signatures.html)
* [Person](people.html)

_[Back to top...](#)_


## Scenarios

{% include scenarios_helper_intro.md %}


### Scenario: Creating a new signature and person (POST)

Posting to the record signature helper endpoint will allow you to create a new signature and person (or update a person if the system attempts to match people posted with helpers) in one operation. The response is the signature that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/record_signature_helper

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
    "comments": "Support our campaign!"
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
    "comments": "Support our campaign!",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signature/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:petition": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/adb951cb-51f9-420e-b7e6-de953195ec86"
        }
    }
}
```

_[Back to top...](#)_