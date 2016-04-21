---
layout: default
title: Attendance
---

# Attendance

This document defines the Attendance resource.

Attendances are a type of action that a user may take by RSVPing to attend an event. Attendances have fields to describe them such as when the attendance was created and typically are linked to the person who made the attendance.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Attendance Fields](#attendance-fields)  
    * [Links](#links)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Attendance resources (GET)](#scenario-retrieving-a-collection-of-attendance-resources-get)
    * [Scenario: Retrieving an individual Attendance resource (GET)](#scenario-scenario-retrieving-an-individual-attendance-resource-get)
    * [Scenario: Creating a new attendance (POST)](#scenario-creating-a-new-attendance-post)
    * [Scenario: Modifying an attendance (PUT)](#scenario-modifying-an-attendance-put)
    * [Scenario: Deleting an attendance (DELETE)](#scenario-deleting-an-attendance-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for an Attendance resource is ```osdi:attendance``` for a single Attendance resource or ```osdi:attendances``` for a collection of Attendance resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Attendance Fields

A list of fields specific to the Attendance resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this attendance was created. (ex: "OSDI System")
|action_date		|string		|The date and time the attendance was made by the person.
|status			|flexenum			|The attendee's response status. One of "declined", "tentative", "accepted", "cancelled", or "needs action".  Note: OSDI vendors may implement varying or client-configured statuses; users should check with the vendor for available attendance status values. 
|attended		|boolean		|Represents whether the person actually attended the event or not.
|comment		|string			|An optional comment from the attendee.



_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Attendance*](attendances.html)	|A self-referential link to the attendance.
|person			|[Person*](people.html)		|A link to a single Person resource representing the person who RSVPed for the event.
|invited_by		|[Person*](people.html)	|A link to a Person resource representing the person that invited this attendee. This is expected to be used for guests.
|event			|[Event*](events.html)  		|A link to an Event resource representing the event on which this attendance was created.

_[Back to top...](#)_


## Helpers

{% include helpers_intro.md %}

|Name          |Description
|-----------    |-----------
|[record_attendance_helper](record_attendance.html)      |Allows the creation of an attendance and a person at the same time.

_[Back to top...](#)_


## Related Resources

* [Record Attendance Helper](record_attendance.html)
* [Event](events.html)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Attendance resources (GET)

Attendance resources are sometimes presented as collections of attendances. For example, calling the attendance endpoint on a particular event will return a collection of all the attendances made to that event.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances

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
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances?page=2"
        },
        "osdi:submissions": [
            {
                "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances"
        }
    },
    "_embedded": {
        "osdi:attendances": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "action_date": "2014-03-18T11:02:15Z",
                "status": "confirmed",
                "attended": true,
                "comment": "Looking forward to it!",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:event": {
                        "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:invited_by": {
                        "href": "https://osdi-sample-system.org/api/v1/person/8a625981-67a4-4457-8b55-2e30b267b2c2"
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
                "status": "tentative",
                "attended": false,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:event": {
                        "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29"
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

### Scenario: Scenario: Retrieving an individual Attendance resource (GET)

Calling an individual Attendance resource will return the resource directly, along with all associated fields and appropriate links to additional information about the attendance.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

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
    "status": "confirmed",
    "attended": true,
    "comment": "Looking forward to it!",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:event": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:invited_by": {
            "href": "https://osdi-sample-system.org/api/v1/person/8a625981-67a4-4457-8b55-2e30b267b2c2"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new attendance (POST)

Posting to the attendances collection endpoint and including a link to an existing Person resource will allow you to create a new attendance associated with that event and person. The response is the new attendance that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

For information on how to create a person along with an attendance, see the [Record Attendance Helper](record_attendance.html) documentation.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "action_date": "2014-03-18T11:02:15Z",
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
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:event": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://actionnetwork.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying an attendance (PUT)

You can update an attendance by calling a PUT operation on that attendance's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/

Header:
OSDI-API-Token:[your api key here]

{
    "status": "declined"
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
    "status": "declined",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:event": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://actionnetwork.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting an attendance (DELETE)

You may delete an attendance by calling the DELETE command on the attendance's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/attendances/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This attendance was successfully deleted."
}
```

_[Back to top...](#)_
