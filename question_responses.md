---
layout: default
title: Question Responses
---

# Question Responses

One of several allowed responses to a question which has a defined enumeration.  For example, if a Question is "What is your most important issue in this election?", a Question Response might be "Environment", and another Question Response might be "Health Care"

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Resource Fields](#resource-fields)
    * [Related Objects](#related-objects)   
    * [Links](#links)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of resources (GET)](#scenario-retrieving-a-collection-of-resources-get)
    * [Scenario: Retrieving an individual resource (GET)](#scenario-scenario-retrieving-an-individual-resource-get)
    * [Scenario: Creating a new resource (POST)](#scenario-creating-a-new-resource-post)
    * [Scenario: Modifying a resource (PUT)](#scenario-modifying-a-resource-put)
    * [Scenario: Deleting a resource (DELETE)](#scenario-deleting-a-resource-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Question Response is ```osdi:response``` for a single Question Response or ```osdi:responses``` for a collection of Question Responses.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Question Response Fields

A list of fields specific to the Question Response.

|Name          |Type      |Description
|-----------    |-----------|--------------
|name               |string     |The name of the question response. Intended for administrative display rather than a public title, though may be shown to a user.
|title              |string     |The title of the question response. Intended for public display rather than administrative purposes.

_[Back to top...](#)_

### Links

{% include links_intro.md %}

|Name          	|Type		|Description
|-----------    |-----------|--------------
|self			|[QuestionResponse*](question_responses.html)	|A self-referential link to the resource.
|question		|[Question*](questions.html)  |A link to the question for which this response may be provided.
|answers        |[Answer[]](answers.html) | A link to the answers in which this response was provided.
_[Back to top...](#)_


## Related Resources

* [Answer](answers.html)
* [QuestionResponse](question_responses.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of question responses (GET)

Retrieve the responses which are possible for a particular question.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses

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
            "href": "https://osdi-sample-system.org/api/v1/resource?page=2"
        },
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-sample-system.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses"
        }
    },
    "_embedded": {
        "osdi:response": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bdd",
                ],
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "environment",
                "title": "Environment",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bdd"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bdd/answers"
                    },
                    "osdi:question": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bee",
                ],
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "healthcare",
                "title": "Health Care",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bee"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bee/answers"
                    },
                    "osdi:question": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    }
                }
            }
        ]
    }
}
```

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual response (GET)

Retrieve the details for an individual resource

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bdd

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
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bdd",
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "environment",
    "title": "Environment",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bdd"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bdd/answers"
        },
        "osdi:question": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        }
    }
}
```

_[Back to top...](#)_

### Scenario: Retrieving answers for a response (GET)

Discover which answers were provided for this response (and thereby, which people gave this response when asked the question.)

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bdd/answers

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
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bdd/answers?page=2"
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
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bdd/answers"
        }
    },
    "_embedded": {
        "osdi:answers": [
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
                    "osdi:responses": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/responses"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
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
                    "osdi:responses": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/1efc3644-af25-4253-90b8-a0baf12dbd1e/responses"
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


### Scenario: Creating a new response (POST)

Create a new response for a particular question.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/questions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b/responses/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "title": "Health care",
    "name": "healthcare"
}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9ueffff",
        "foreign_system:1"
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "title": "Health care",
    "name": "healthcare",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b/responses/d91b4b2e-ae0e-4cd3-9ed7-de9ueffff"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b/responses/d91b4b2e-ae0e-4cd3-9ed7-de9ueffff/answers"
        },
        "osdi:question": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a response (PUT)

Change the properties of an existing response.


#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/questions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b/responses/d91b4b2e-ae0e-4cd3-9ed7-de9ueffff

Header:
OSDI-API-Token:[your api key here]

{
    "title": "Health care (or medical care)"
}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9ueffff",
        "foreign_system:1"
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "title": "Health care (or medical care)",
    "name": "healthcare",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b/responses/d91b4b2e-ae0e-4cd3-9ed7-de9ueffff"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b/responses/d91b4b2e-ae0e-4cd3-9ed7-de9ueffff/answers"
        },
        "osdi:question": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a response (DELETE)

Delete an existing question response.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/questions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b/responses/d91b4b2e-ae0e-4cd3-9ed7-de9ueffff

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This question response was successfully deleted."
}
```

_[Back to top...](#)_
