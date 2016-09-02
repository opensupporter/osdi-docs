---
layout: default
title: Record Attendance Helper
---

# Record Attendance Helper

This document defines the Record Attendance Helper resource. 

The Record Attendance Helper is a helper endpoint to aid in the creation of [Attendance](attendances.html) and [People](people.html) resources via POST. It provides a quick and easy way to create attendances and people at the same time, eliminating the need for multiple POST operations to store that information.

The Record Attendance Helper POST body for ticketed events will look different from non-ticketed events, including fields for the tickets bought and who received those tickets (which can be different from the person who bought the tickets and created the attendance). 

Some systems may attempt to match people sent via the Record Attendance Helper to existing people in the database and update their record instead of creating a new person. The method used for matching will be detailed in that system's documentation. 

When using the Record Attendance Helper, tagging and list membership info may be added at the same time as well, eliminating the need for multiple POST operations to store that information.

In addition, you can indicate to the server whether to trigger additional actions, such as an autoresponse email sent back to the person who took action.

Typically, the response to a successful Record Attendance Helper POST is the full representation of the attendance. However, the Record Attendance Helper can be used without authentication, allowing for use in frontend javascript-based applications without giving away API key secrets, for example. If no authentication is passed, the response on success will simply be the server response code (ex: 200) and an empty JSON object. On error, the server response code (ex: 404, 500) plus an error message may be returned.

Some initial implementations may only support helpers -- direct RESTful access may not be supported. In those cases, the _links section may be omitted in responses.


### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
	* [Common Fields](#common-fields)
    * [Record Attendance Helper Fields](#record-attendance-helper-fields)
    * [Helper Action Functions](#helper-action-functions)
    * [Related Objects](#related-objects)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Creating a new attendance and person (POST)](#scenario-creating-a-new-attendance-and-person-post)
    * [Scenario: Creating a new attendance and person without authentication (POST)](#scenario-creating-a-new-attendance-and-person-without-authentication-post)


{% include endpoints_and_url_structures.md %}

The link relation label for the Record Attendance Helper is ```osdi:record_attendance_helper```.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields_helper.md %}

_[Back to top...](#)_


### Record Attendance Helper Fields

A list of fields specific for POSTing via the Record Attendance Helper.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this attendance was created. (ex: "OSDI System")
|action_date		|string		|The date and time the attendance was made by the person.
|status			|enum			|The attendee's response status. One of "declined", "tentative", "accepted", or "needs action".
|attended		|boolean		|For event RSVPs, represents whether the person actually attended the event or not. For ticketed events, field should be absent, as it's superseded by the `attended` field in the `ticket` object.
|comment		|string			|An optional comment from the attendee.
|referrer_data		|[Referrer Data*](#referrer-data)	|An object hash representing referrer and sourcing information about this attendance.
|person			|[Person*](#person)	|An object hash representing the person who made the attendance, or bought the tickets in the case of a ticketed event.
|tickets		|[Tickets[]](#tickets)	|If this event is a ticketed event, an array of object hashes representing each ticket purchased as part of this attendance. (ex: One $5 general admission ticket for Sam and two $50 VIP tickets for Sally and Saul.)

_[Back to top...](#)_

### Helper Action Functions

{% include helper_action_functions.md %}

_[Back to top...](#)_


### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Referrer Data

|Name          |Type      |Description
|-----------    |-----------|--------------
|referrer_data.source	|string    |The source code that was used when this attendance was created. Typically used to track individual links, such as a post on social media or a link in a specific email. (ex: "facebook-101016-mainpage")
|referrer_data.referrer	|string    |The code or ID representing a person or group that referred this attendance. Typically used to track which person referred the person who made this attendance. (ex: "jane-doe")
|referrer_data.website	|string    |The top level domain of the website where the person clicked from to then subsequently make this attendance. (ex: "facebook.com")
|referrer_data.url	|string    |The specific URL where the person clicked from to then subsequently make this attendance. (ex: "https://facebook.com/posts/12345")

#### Tickets

|Name          |Type      |Description
|-----------    |-----------|--------------
|ticket.title	|string    |The name of the ticket type that was purchased. (ex: "General admission")
|ticket.description	|string    |A longer description of the ticket type. (ex: "Gets you access to the convention floor.")
|ticket.amount	|float    |The price paid for this ticket, in the specified currency. (ex: "10.50")
|ticket.currency	|string    |ISO 4217 designation of currency. (ex: "USD", "JPY")
|attended		|boolean		|Represents whether the person actually attended the event or not.
|ticket.person		|[Person*](#person)	|An object hash representing the person who will use this ticket.


#### Person

|Name          |Type      |Description
|-----------    |-----------|--------------
|person      |[Person*](people.html)     |An inlined hash representation of a person, containing any valid fields for the Person resource.

_[Back to top...](#)_


## Related Resources

* [Attendance](attendances.html)
* [Person](people.html)

_[Back to top...](#)_


## Scenarios

{% include scenarios_helper_intro.md %}


### Scenario: Creating a new attendance and person (POST)

Posting to the record attendance helper endpoint will allow you to create a new attendance and person (or update a person if the system attempts to match people posted with helpers) in one operation. The response is the attendance that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

Ticketed event attendances and non-ticketed event attendances look different. First, an example of POSTING a non-ticketed event attendace:

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/record_attendance_helper

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
    "status": "accepted",
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
    "status": "accepted",
    "referrer_data": {
        "source": "facebook-101016-mainpage",
        "referrer": "jane-doe",
        "website": "facebook.com",
        "url": "https://facebook.com/posts/12345"
    },
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:event": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/adb951cb-51f9-420e-b7e6-de953195ec86"
        }
    }
}
```

Next, an example of POSTing a ticketed event attendance:

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/record_attendance_helper

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
    "status": "accepted",
    "referrer_data": {
        "source": "facebook-101016-mainpage",
        "referrer": "jane-doe",
        "website": "facebook.com",
        "url": "https://facebook.com/posts/12345"
    },
    "tickets": [
	    {
	        "title": "General Admission",
	        "description": "Gets you into the event and all activities.",
	        "amount": 5,
	        "currency": "USD",
	        "attended": true,
	        "person": {
                "family_name": "Edwin",
                "given_name": "Labadie",
                "email_addresses": [
                    {
                        "address":"test-3@example.com",
                        "primary": true,
                        "address_type": "Personal"
                    }
                ]
	        }
	    },
	    {
	        "title": "VIP",
	        "description": "Meet and greet before the event, and front-row seats.",
	        "amount": 500,
	        "currency": "USD",
	        "attended": false,
	        "person": {
                "family_name": "Jane",
                "given_name": "Doe",
                "email_addresses": [
                    {
                        "address":"jdoe@example.com",
                        "primary": true,
                        "address_type": "Personal"
                    }
                ]
	        }
	    }
	],
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
    "status": "accepted",
    "referrer_data": {
        "source": "facebook-101016-mainpage",
        "referrer": "jane-doe",
        "website": "facebook.com",
        "url": "https://facebook.com/posts/12345"
    },
    "tickets": [
	    {
	        "title": "General Admission",
	        "description": "Gets you into the event and all activities.",
	        "amount": 5,
	        "currency": "USD",
	        "attended": true,
	        "person": {
                "family_name": "Edwin",
                "given_name": "Labadie",
                "email_addresses": [
                    {
                        "address":"test-3@example.com",
                        "primary": true,
                        "address_type": "Personal"
                    }
                ]
	        }
	    },
	    {
	        "title": "VIP",
	        "description": "Meet and greet before the event, and front-row seats.",
	        "amount": 500,
	        "currency": "USD",
	        "attended": false,
	        "person": {
                "family_name": "Jane",
                "given_name": "Doe",
                "email_addresses": [
                    {
                        "address":"jdoe@example.com",
                        "primary": true,
                        "address_type": "Personal"
                    }
                ]
	        }
	    }
	],
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:event": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/adb951cb-51f9-420e-b7e6-de953195ec86"
        }
    }
}
```

_[Back to top...](#)_

### Scenario: Creating a new attendance and person without authentication (POST)

Posting to the record attendance helper endpoint without authentication will allow you to create a new attendance and person (or update a person if the system attempts to match people posted with helpers) in one operation, but without giving away API key secrets or leaking data, so this method is appropriate for frontend javascript applications. The response on success will simply be the server response code (ex: 200) and an empty JSON object. On error, the server response code (ex: 404, 500) plus an error message may be returned. While each implementing system will require different fields, any optional fields not included in a POST operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/record_attendance_helper

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
    "status": "accepted",
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