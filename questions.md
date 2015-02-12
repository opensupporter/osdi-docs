---
layout: default
title: Questions
---

# Question

This page defines the Question resource.

Questions are queries asked to a person. When people answer questions, [Answer](answers.html) resources are created to store their answer. Examples of questions include "Do you support John Doe for City Council?" or "Do you approve or disapprove of the way Barak Obama is handling his job as president?"

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Question Fields](#question-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Question resources (GET)](#scenario-retrieving-a-collection-of-question-resources-get)
    * [Scenario: Retrieving an individual Question resource (GET)](#scenario-scenario-retrieving-an-individual-question-resource-get)
    * [Scenario: Creating a new question (POST)](#scenario-creating-a-new-question-post)
    * [Scenario: Modifying a question (PUT)](#scenario-modifying-a-question-put)
    * [Scenario: Deleting a question (DELETE)](#scenario-deleting-a-question-delete)


{% include endpoints_and_url_structures.md %}


The link relation label for a Question resource is ```osdi:question``` for a single Question resource or ```osdi:questions``` for a collection of Question resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_

### Question Fields

| Name          | Type                | Description
| -----------   | -----------         | --------------
|origin_system		|string     |A human readable identifier of the system where this question was created. (ex: "OSDI System")
|name				|string		|The name of the question. Intended for administrative display rather than a public title, though may be shown to a user.
|title				|string		|The title of the question. Intended for public display rather than administrative purposes.
|description		|string		|A description of the question, usually displayed publicly. May contain text and/or HTML.
|summary			|string		|A text-only single paragraph summarizing the question. Shown on listing pages that have more than titles, but not enough room for full description.
| question_type | string              | The format of the question. One of "Paragraph" or "MultiChoice".

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Question*](questions.html)	|A self-referential link to the question.
|creator		|[Person*](people.html)  		|A link to a single Person resource representing the creator of the question.
|modified_by	|[Person* ](people.html) 		|A link to a Person resource representing the last editor of this question.
|answers	|[Answers[]*](answers.html)	|A link to the collection of Answer resources for this question.

_[Back to top...](#)_


## Related Resources

* [Person](people.html)
* [Answer](answers.html)

_[Back to top...](#)_


## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Question resources (GET)

Question resources are sometimes presented as collections of questions. For example, calling the questions endpoint will return a collection of all the questions stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/questions/

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
            "href": "https://osdi-sample-system.org/api/v1/questions?page=2"
        },
        "osdi:questions": [
            {
                "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/questions/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/questions"
        }
    },
    "_embedded": {
        "osdi:questions": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "Volunteer Question",
                "title": "Do you want to volunteer?",
                "description": "<p>Do you want to volunteer? It will only take a few hours of time per week.</p>",
                "summary": "Volunteer question for canvass",
                "question_type": "MultiChoice",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
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
                "name":	"Why the respondant wants to get involved.",
                "title": "Why do you want to get involved with our organization?",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/1efc3644-af25-4253-90b8-a0baf12dbd1e/answers"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Question resource (GET)

Calling an individual Question resource will return the resource directly, along with all associated fields and appropriate links to additional information about the question.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/questions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "name": "Volunteer Question",
    "title": "Do you want to volunteer?",
    "description": "<p>Do you want to volunteer? It will only take a few hours of time per week.</p>",
    "summary": "Volunteer question for canvass",
    "question_type": "MultiChoice",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new question (POST)

Posting to the question collection endpoint will allow you to create a new question. The response is the new question that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/questions/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "title": "Do you want to volunteer?",
    "name": "Volunteer Question",
    "origin_system": "OpenSupporter",
    "question_type": "MultiChoice"
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
    "title": "Do you want to volunteer?",
    "name": "Volunteer Question",
    "origin_system": "OpenSupporter",
    "question_type": "MultiChoice",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a question (PUT)

You can update a question by calling a PUT operation on that question's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "name": "2014 Volunteer question",
    "title": "Do you want to volunteer this year?"
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
    "title": "Do you want to volunteer this year?",
    "name": "2014 Volunteer question",
    "origin_system": "OpenSupporter",
    "question_type": "MultiChoice",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a question (DELETE)

You may delete a question by calling the DELETE command on the question's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/questions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This questions was successfully deleted."
}
```

_[Back to top...](#)_