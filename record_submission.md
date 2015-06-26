---
layout: default
title: Record Submission Helper
---

# Record Submission Helper

This document defines the Record Submission Helper resource. 

The Record Submission Helper is a helper endpoint to aid in the creation of [Submission](submissions.html) and [People](people.html) resources via POST. It provides a quick and easy way to create submissions and people at the same time, eliminating the need for multiple POST operations to store that information.

Some systems may attempt to match people sent via the Record Submission Helper to existing people in the database and update their record instead of creating a new person. The method used for matching will be detailed in that system's documentation. 

When using the Record Submission Helper, tagging and list membership info may be added at the same time as well, eliminating the need for multiple POST operations to store that information.

The response to a Record Submission Helper POST is the full representation of the submission.

Some initial implementations may only support helpers -- direct RESTful access may not be supported. In those cases, the _links section may be omitted in responses.


### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
	* [Common Fields](#common-fields)
    * [Record Submission Helper Fields](#record-submission-helper-fields)
    * [Related Objects](#related-objects)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Creating a new submission and person (POST)](#scenario-creating-a-new-submission-and-person-post)


{% include endpoints_and_url_structures.md %}

The link relation label for the Record Submission Helper is ```osdi:record_submission_helper```.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields_helper.md %}

_[Back to top...](#)_


### Record Submission Helper Fields

A list of fields specific for POSTing via the Record Submission Helper.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this submission was created. (ex: "OSDI System")
|action_date		|string		|The date and time the submission was made by the person.
|add_tags      |strings[]     |An array of tag names corresponding to previously created tags to add to this person when it is created.
|add_lists     |strings[]     |An array of list names corresponding to previously created lists to add to this person when it is created.
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

* [Submission](submissions.html)
* [Person](people.html)

_[Back to top...](#)_


## Scenarios

{% include scenarios_helper_intro.md %}


### Scenario: Creating a new submission and person (POST)

Posting to the record submission helper endpoint will allow you to create a new submission and person (or update a person if the system attempts to match people posted with helpers) in one operation. The response is the submission that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/record_submission_helper

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
    "add_tags": [
        "volunteer",
        "donor"
    ],
    "add_lists": [
        "supporters"
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
    "action_date": "2014-03-18T11:02:15Z",
    "origin_system": "OpenSupporter",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:form": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/adb951cb-51f9-420e-b7e6-de953195ec86"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/answers"
        } 
    }
}
```

_[Back to top...](#)_