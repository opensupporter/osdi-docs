---
layout: default
title: Answers
---

# Answer

This page defines the Answer resource.

Answers are responses a person gave to a question defined by the [Question](questions.html) resource. For example, a Question might ask, "Do you support John Doe For City Council?" and an answer might be "Yes", indicating the person's resonse to the questio.

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Answer Fields](#answer-fields)
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Answer resources (GET)](#scenario-retrieving-a-collection-of-answer-resources-get)
    * [Scenario: Retrieving an individual Answer resource (GET)](#scenario-scenario-retrieving-an-individual-answer-resource-get)
    * [Scenario: Creating a new answer (POST)](#scenario-creating-a-new-answer-post)
    * [Scenario: Modifying an answer (PUT)](#scenario-modifying-an-answer-put)
    * [Scenario: Deleting an answer (DELETE)](#scenario-deleting-an-answer-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for an Answer resource is ```osdi:answer``` for a single Answer resource or ```osdi:answers``` for a collection of Answer resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Answer Fields

| Name          | Type      | Description
|-----------    |-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this answer was created. (ex: "OSDI System")
|action_date		|string		|The date and time the answer was given by the person.
|value				|string		|The response the person gave. 

_[Back to top...](#)_



### Links

{% include links_intro.md %}

|Name          	|Type		|Description
|-----------    |-----------|--------------
|self			|[Answer*](answers.html)	|A self-referential link to the answer.
|person		|[Person*](people.html)  |A link to a single Person resource representing the person to whom this answer belongs.
|question		|[Question*](questions.html)  |A link to the associated Question resource that the person answered.

_[Back to top...](#)_


## Related Resources

* [Question](questions.html)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Answer resources (GET)

Answer resources are sometimes presented as collections of answers. For example, calling the answer endpoint on a particular question will return a collection of all the answers for that question.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers

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
            "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers?page=2"
        },
        "osdi:answers": [
            {
                "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers"
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
                "value": "Yes",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:question": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
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
                "value": "No",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:question": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29"
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

### Scenario: Scenario: Retrieving an individual Answer resource (GET)

Calling an individual Answer resource will return the resource directly, along with all associated fields and appropriate links to additional information about the answer.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

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
    "value": "Yes",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:question": {
            "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new answer (POST)

Posting to the answers collection endpoint and including a link to an existing Person resource will allow you to create a new answer associated with that question and person. The response is the new answer that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "action_date": "2014-03-18T11:02:15Z",
    "value": "Yes",
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
    "value": "Yes",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:question": {
            "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://actionnetwork.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying an answer (PUT)

You can update an answer by calling a PUT operation on that answer's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/

Header:
OSDI-API-Token:[your api key here]

{
    "value": "No"
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
    "value": "No",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:question": {
            "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://actionnetwork.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting an answer (DELETE)

You may delete an answer by calling the DELETE command on the answer's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

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