---
layout: default
title: Record Outreach Helper
---

# Record Outreach Helper

This document defines the Record Outreach Helper resource. 

The Record Outreach Helper is a helper endpoint to aid in the creation of [Outreach](outreaches.html) and [People](people.html) resources via POST. It provides a quick and easy way to create outreaches and people at the same time, eliminating the need for multiple POST operations to store that information.

Some systems may attempt to match people sent via the Record Outreach Helper to existing people in the database and update their record instead of creating a new person. The method used for matching will be detailed in that system's documentation. 

When using the Record Outreach Helper, tagging and list membership info may be added at the same time as well, eliminating the need for multiple POST operations to store that information.

In addition, you can indicate to the server whether to trigger additional actions, such as an autoresponse email sent back to the person who took action.

Typically, the response to a successful Record Outreach Helper POST is the full representation of the outreach. However, the Record Outreach Helper can be used without authentication, allowing for use in frontend javascript-based applications without giving away API key secrets, for example. If no authentication is passed, the response will simply be the server response code, to avoid leaking any data. (ex: 200 for success, 500 for error, etc...)

Some initial implementations may only support helpers -- direct RESTful access may not be supported. In those cases, the _links section may be omitted in responses.


### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
	* [Common Fields](#common-fields)
    * [Record Outreach Helper Fields](#record-outreach-helper-fields)
    * [Related Objects](#related-objects)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Creating a new outreach and person (POST)](#scenario-creating-a-new-outreach-and-person-post)
    * [Scenario: Creating a new outreach and person without authentication (POST)](#scenario-creating-a-new-outreach-and-person-without-authentication-post)


{% include endpoints_and_url_structures.md %}

The link relation label for the Record Outreach Helper is ```osdi:record_outreach_helper```.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields_helper.md %}

_[Back to top...](#)_


### Record Outreach Helper Fields

A list of fields specific for POSTing via the Record Outreach Helper.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this outreach was created. (ex: "OSDI System")
|action_date		|string		|The date and time the outreach was made by the person.
|type				|flexunum	|The type of outreach, specifying how the user performed the outreach to targets. One of "email", "in-person", "phone", "postal mail", or another type as needed.
|duration		|integer		|The duration in seconds of the outreach, if applicable. (ex: duration will only be present on phone outreach types)
|subject		|string		|The subject of the outreach, if applicable. (ex: subject will only be present on email outreach types)
|message		|string		|The message of the outreach, if applicable. (ex: message will only be present on email or postal mail outreach types)
|targets			|[Target[]](#target)    |A array of target object hashes representing the targets of the outreach.
|add_tags      |strings[]     |An array of tag names corresponding to previously created tags to add to this person when it is created.
|add_lists     |strings[]     |An array of list names corresponding to previously created lists to add to this person when it is created.
|person			|[Person*](#person)	|An object hash representing the person who made the outreach.
|triggers		|[Triggers](#triggers)	|An object hash representing responses a user would like to trigger from the server as part of the POST, such as sending an autoresponse email back to the person who took action with this helper.

_[Back to top...](#)_


### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Target

|Name          	|Type      |Description
|-----------    |-----------|--------------
|target.title	|string    |The title or position of the target. (ex: "Senator" or "CEO")
|target.organization	|string	|The organization the target belongs to. (ex: "U.S. Senate" or "Acme Corporation")
|target.given_name	|string    |The first or given name of the target. (ex: "John")
|target.family_name	|string    |The last or family name of the target. (ex: "Smith")
|target.ocdid	|string    |The Open Civic Data Division ID for this target's political geography, if applicable. See [here](http://docs.opencivicdata.org/en/latest/proposals/0002.html) for more documentation. (ex: "ocd-division/country:us/state:ny/cd:18", which corresponds to New York's 18th Congressional District)

#### Person

|Name          |Type      |Description
|-----------    |-----------|--------------
|person      |[Person*](people.html)     |An inlined hash representation of a person, containing any valid fields for the Person resource.

#### Triggers

|Name          |Type      |Description
|-----------    |-----------|--------------
|autoresponse   |object     |An object hash representing the autoresponse email trigger type.
|autoresponse.enabled   |boolean     |A boolean indicating whether the autoresponse email should be sent or not.

_[Back to top...](#)_


## Related Resources

* [Outreach](outreaches.html)
* [Person](people.html)

_[Back to top...](#)_


## Scenarios

{% include scenarios_helper_intro.md %}


### Scenario: Creating a new outreach and person (POST)

Posting to the record outreach helper endpoint will allow you to create a new outreach and person (or update a person if the system attempts to match people posted with helpers) in one operation. The response is the outreach that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/record_outreach_helper

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
    "type": "phone",
    "duration": 120,
    "targets": [
	    {
	        "title": "Senator",
	        "given_name": "John",
	        "family_name": "Smith",
	        "organization": "U.S. Senate",
	        "ocdid": "ocd-division/country:us/state:ny"
	    },
	    {
	        "title": "Senator",
	        "given_name": "Jennifer",
	        "family_name": "Larson",
	        "organization": "U.S. Senate",
	        "ocdid": "ocd-division/country:us/state:ny"
	    }
	],
	"add_tags": [
        "volunteer",
        "donor"
    ],
    "add_lists": [
        "supporters"
    ],
    "triggers": {
        "autoresponse": {
            "enabled": true
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
    "origin_system": "OpenSupporter",
    "type": "phone",
    "duration": 120,
    "targets": [
	    {
	        "title": "Senator",
	        "given_name": "John",
	        "family_name": "Smith",
	        "organization": "U.S. Senate",
	        "ocdid": "ocd-division/country:us/state:ny"
	    },
	    {
	        "title": "Senator",
	        "given_name": "Jennifer",
	        "family_name": "Larson",
	        "organization": "U.S. Senate",
	        "ocdid": "ocd-division/country:us/state:ny"
	    }
	],
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:advocacy_campaign": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/adb951cb-51f9-420e-b7e6-de953195ec86"
        }
    }
}
```

_[Back to top...](#)_

### Scenario: Creating a new outreach and person without authentication (POST)

Posting to the record outreach helper endpoint without authentication will allow you to create a new outreach and person (or update a person if the system attempts to match people posted with helpers) in one operation, but without giving away API key secrets or leaking data, so this method is appropriate for frontend javascript applications. The response is the server resonse code. (ex: 200 for success, 500 for error, etc...) While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/record_outreach_helper

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
    "type": "phone",
    "duration": 120,
    "targets": [
	    {
	        "title": "Senator",
	        "given_name": "John",
	        "family_name": "Smith",
	        "organization": "U.S. Senate",
	        "ocdid": "ocd-division/country:us/state:ny"
	    },
	    {
	        "title": "Senator",
	        "given_name": "Jennifer",
	        "family_name": "Larson",
	        "organization": "U.S. Senate",
	        "ocdid": "ocd-division/country:us/state:ny"
	    }
	],
	"add_tags": [
        "volunteer",
        "donor"
    ],
    "add_lists": [
        "supporters"
    ],
    "triggers": {
        "autoresponse": {
            "enabled": true
        }
    }
}
```

#### Response

```javascript
200 OK
```

_[Back to top...](#)_