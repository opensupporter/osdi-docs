---
layout: default
title: Canvasses
---

# Canvasses

This page defines the Canvass resource.

A canvass occurs when one person attempts to contact another person for the purpose of obtaining data about that person.  For example, a canvasser visits a voter's home and asks the voter whether she intends to vote in the next election; or, a campaign staffer calls a volunteer to ask whether he intends to attend the candidate's upcoming kick-off event.  The person being contacted is known as the "target" of the canvass, and the target may have [Answers](answers.html) or [Taggings](taggings.html) applied to them as a result of the canvass.  Alternatively, the target may have a non-canvass result (e.g. "not home") applied to them.

It is not necessary to create a Canvass in order to create an Answer or Tagging for a Person.  However, a Canvass can provide useful information about how the Answer or Tagging was collected, which may prove valuable for future organizing purposes.

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
    * [Scenario: Modifying a Canvass (PUT)](#scenario-modifying-a-canvass-put)
    * [Scenario: Deleting a Canvass (DELETE)](#scenario-deleting-a-canvass-delete)


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
|origin_system		|string     |A human readable identifier of the system where this canvass was created. (ex: "OSDI System")
|action_date		|string		|The date and time the canvass was attempted.
| contact_type  | string | A code indicating the method by which the person was contacted.  For example: "in-person"
| input_type    | string | A code indicating the method by which the canvass is being input into the system. For example: "mobile"
| failure_code  | string | A code indicating why the canvass failed, for eample: "not-home". Empty string or absent value indicates the target was successfully contacted.  It is usually the case that a Canvass with a non-empty failure_code will have no associated Answers or Taggings, and that a Canvass that does have Answers or Taggings should have an empty or absent failure_code.

_[Back to top...](#)_



### Links

{% include links_intro.md %}

|Name          	|Type		|Description
|-----------    |-----------|--------------
|self			|[Canvass*](canvasses.html)	|A self-referential link to the canvass.
|target		|[Person](people.html)  |A link to a single Person resource representing the person who was contacted.
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

Calling this endpoint allows consumers to see a person's canvass history.

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
                "contact_type": "in-person",
                "input_type": "mobile",
                "failure_code": "not-home",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:target": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:answers": [
                    ],
                    "osdi:taggings": [
                    ]
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
                "contact_type": "phoneCall",
                "input_type": "paper",
                "failure_code": "",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf"
                    },
                    "osdi:target": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:answers": [
                      {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0111/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ccc"
                      },
                      {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0222/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bbb"
                      }
                    ],
                    "osdi:taggings": [
                      {
                        "href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0aaa/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ddd"
                      },
                      {
                        "href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bbb/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0eee"
                      }
                    ]
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Retrieving an individual Canvass resource (GET)

Calling an individual Canvass resource will return the resource directly, along with all associated fields and appropriate links to additional information about the canvass.

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
    "contact_type": "in-person",
    "input_type": "mobile",
    "failure_code": "",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:target": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:answers": [
          {
          	"href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0111/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ccc"
          },
          {
          	"href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0222/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bbb"
          }
        ],
        "osdi:taggings": [
          {
          	"href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0aaa/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ddd"
          },
          {
          	"href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bbb/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0eee"
          }
        ]
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
    "contact_type": "in-person",
    "input_type": "mobile",
    "failure_code": "",
    "_links" : {
        "osdi:answers": [
          {
          	"href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0111/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ccc"
          },
          {
          	"href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0222/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bbb"
          }
        ],
        "osdi:taggings": [
          {
          	"href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0aaa/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ddd"
          },
          {
          	"href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bbb/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0eee"
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
    "contact_type": "in-person",
    "input_tinput_typeype": "mobile",
    "failure_code": "",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:target": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:answers": [
          {
          	"href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0111/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ccc"
          },
          {
          	"href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0222/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bbb"
          }
        ],
        "osdi:taggings": [
          {
          	"href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0aaa/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ddd"
          },
          {
          	"href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bbb/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0eee"
          }
        ]
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a Canvass (PUT)

You can update an Canvass by calling a PUT operation on that canvass's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

Header:
OSDI-API-Token:[your api key here]

{
    "contact_type": "phoneCall",
    "_links" : {
        "osdi:answers": [
          {
          	"href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0111/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ccc"
          },
        	{
          	"href": "https://osdi-sample-system.org/api/v1/questions/aaab4b2e-ae0e-4cd3-9ed7-d0ec501b0555/answers/aaab4b2e-ae0e-4cd3-9ed7-d0ec501b0fff"
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
    "contact_type": "phoneCall",
    "input_type": "mobile",
    "failure_code": "",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:target": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:answers": [
          {
          	"href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0111/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ccc"
          },
        	{
          	"href": "https://osdi-sample-system.org/api/v1/questions/aaab4b2e-ae0e-4cd3-9ed7-d0ec501b0555/answers/aaab4b2e-ae0e-4cd3-9ed7-d0ec501b0fff"
          }
        ],
        "osdi:taggings": [
          {
          	"href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0aaa/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ddd"
          },
          {
          	"href": "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bbb/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0eee"
          }
        ]
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a Canvass (DELETE)

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
    "notice": "This canvass was successfully deleted."
}
```

_[Back to top...](#)_