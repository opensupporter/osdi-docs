---
layout: default
title: Canvasses
---

# Canvasses

This page defines the Canvass resource.

A canvass occurs when one person attempts to contact another person for the purpose of obtaining data about that person.  For example, a canvasser visits a voter's home and asks the voter whether she intends to vote in the next election; or, a campaign staffer calls a volunteer to ask whether he intends to attend the candidate's upcoming kick-off event.  The person being contacted is known as the "target" of the canvass, and the target may have [Answers](answers.html) or [Taggings](taggings.html) applied to them as a result of the canvass.  Alternatively, the target may have a non-canvass result (e.g. "not home") applied to them.

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Canvass Fields](#canvass-fields)
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Canvass resources (GET)](#scenario-retrieving-a-collection-of-canvass-resources-for-a-person-get)
    * [Scenario: Retrieving an individual Canvass resource (GET)](#scenario-retrieving-an-individual-canvass-resource-get)
    * [Scenario: Creating a new Canvass (POST)](#scenario-creating-a-new-canvass-post)
    * [Scenario: Modifying an answer (PUT)](#scenario-modifying-an-answer-put)
    * [Scenario: Deleting an answer (DELETE)](#scenario-deleting-an-answer-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for an Canvass resource is ```osdi:canvass``` for a single Canvass resource or ```osdi:canvasses``` for a collection of Canvass resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Canvass Fields

| Name          | Type      | Description
|-----------    |-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this answer was created. (ex: "OSDI System")
|action_date		|string		|The date and time the canvass was attempted.
| contactType  | string | A code indicating the method by which the person was contacted.  For example: "in-person"
| inputType    | string | A code indicating the method by which the canvass is being input into the system. For example: "mobile"
| failureCode  | string | A code indicating why the canvass failed, for eample: "not home". Empty string or absent value indicates the canvass succeeded.

_[Back to top...](#)_



### Links

{% include links_intro.md %}

|Name          	|Type		|Description
|-----------    |-----------|--------------
|self			|[Canvass*](canvasses.html)	|A self-referential link to the answer.
|target		|[Person](people.html)  |A link to a single Person resource representing the person to whom this answer belongs.
|answers      |[Answer*](answers.html) | Zero or more answers to [Questions](questions.html) posed during the canvass.
|taggings     |[Tagging*](taggings.html) | Zero or more taggings applied as a result of the canvass.

_[Back to top...](#)_


## Related Resources

* [Question](questions.html)
* [Person](people.html)
* [Answer](answers.html)
* [Tagging](taggings.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}


### Scenario: Retrieving a collection of Canvass resources for a person (GET)

Calling this endpoing allows consumers to see a person's canvass history.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses

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
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses?page=2"
        },
        "osdi:canvasses": [
            {
                "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses"
        }
    },
    "_embedded": {
        "osdi:canvasses": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "action_date": "2014-03-18T11:02:15Z",
                "contactType": "in-person",
                "inputType": "mobile",
                "failureCode": "",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:target": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:answers": {
                        "href": "people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
                    },
                    "osdi:taggings": {
                        "href": "people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
                    },
                }
            },
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "action_date": "2014-03-18T11:02:15Z",
                "contactType": "phoneCall",
                "inputType": "paper",
                "failureCode": "",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf"
                    },
                    "osdi:target": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:answers": {
                        "href": "people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf/answers"
                    },
                    "osdi:taggings": {
                        "href": "people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf/taggings"
                    },
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Retrieving an individual Canvass resource (GET)

Calling an individual Canvass resource will return the resource directly, along with all associated fields and appropriate links to additional information about the answer.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

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
    "contactType": "in-person",
    "inputType": "mobile",
    "failureCode": "",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:target": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        },
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new Canvass (POST)

Posting to the Canvasses collection endpoint and including a link to existing Answer and Tagging resource(s) will allow you to create a new canvass that indicates that the indicated Person was canvassed and that the answers and taggings indicated were recorded as a result.  The response is the new canvass that was created.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "action_date": "2014-03-18T11:02:15Z",
    "contactType": "in-person",
    "inputType": "mobile",
    "failureCode": "",
    "_links" : {
        "osdi:answers": [
        	{
          	"href": "https://osdi-sample-system.org/api/v1/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ccc"
          },
          {
          	"href": "https://osdi-sample-system.org/api/v1/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bbb"
          }
        ],
        "osdi:taggings": [
        	{
          	"href": "https://osdi-sample-system.org/api/v1/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ddd"
          },
          {
          	"href": "https://osdi-sample-system.org/api/v1/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0eee"
          }
        ]
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
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "action_date": "2014-03-18T11:02:15Z",
    "contactType": "in-person",
    "inputType": "mobile",
    "failureCode": "",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:target": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        },
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying an answer (PUT)

You can update an answer by calling a PUT operation on that answer's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.  Answers and taggings indicated in a PUT will be added to the canvass - it is not possible to delete answers and taggings from a canvass, once applied.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/

Header:
OSDI-API-Token:[your api key here]

{
    "contactType": "phoneCall",
    "_links" : {
        "osdi:answers": [
        	{
          	"href": "https://osdi-sample-system.org/api/v1/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0111"
          },
        ]
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
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "action_date": "2014-03-18T11:02:15Z",
    "contactType": "phoneCall",
    "inputType": "mobile",
    "failureCode": "",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:target": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        },
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting an Canvass (DELETE)

You may delete a canvass by calling the DELETE command on the canvass's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This answer was successfully deleted."
}
```

_[Back to top...](#)_