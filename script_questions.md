---
layout: default
title: Scripts
---

# Script Question

This page defines the Script Question resource.

Scripts Questions are intermediary resources that associate [Questions](questions.html) with  [Scripts](scripts.html). 

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Script Fields](#script-fields) 
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Script Question resources (GET)](#scenario-retrieving-a-collection-of-script-question-resources-get)
    * [Scenario: Add question to a script (POST)](#scenario-add-question-to-a-script-post)
    * [Scenario: Clear all questions in a script (DELETE)](#scenario-clear-all-questions-in-a-script-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Script Question resource is ```osdi:script_question``` for a single Script resource or ```osdi:script_questions``` for a collection of Script Question resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_

### Script Fields

| Name          | Type                | Description
| -----------   | -----------         | --------------
|sequence      |int     |A sequence number for the scipt question. Defines position of the linked question in a survey

_[Back to top...](#)_

### Links

{% include links_intro.md %}

| Name          | Type       | Description
|-----------    |----------- |-----------
|question  |[Question*](questions.html)  |A link to the associated Question resources for this script question.

_[Back to top...](#)_


## Related Resources

* [Script](scripts.html)
* [Question](questions.html)




_[Back to top...](#)_


## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Script Question resources (GET)

Script Question resources are always retrieved as a collections of script questions. Calling the script questions endpoint will return a collection of all the script questions associated with the script accessible with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/scripts/d91b4b2e-ae0e-4cd3-9ed7-d0ecb0bc3/script_questions

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
            "href": "https://osdi-sample-system.org/api/v1/scripts/d91b4b2e-ae0e-4cd3-9ed7-d0ecb0bc3/script_questions?page=2"
        },
        "osdi:script": {
            "href": "https://osdi-sample-system.org/api/v1/scripts/d91b4b2e-ae0e-4cd3-9ed7-d0ecb0bc3"
        },
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-sample-system.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": https://osdi-sample-system.org/api/v1/scripts/d91b4b2e-ae0e-4cd3-9ed7-d0ecb0bc3/script_questions
        }
    },
    "_embedded": {
        "osdi:scipt_questions": [
          {
            "sequence": 1,
            "_embedded": {
              "osdi:question":
                {
                  "origin_system": "OSDISystem",
                  "name": "foobar",
                  "description": "What is your name?",
                  "title": "foobar",
                  "summary": "What is your name?",
                  "question_type": "SingleChoice",
                  "identifiers": [
                    "OSDISystem:202004"
                  ],
                  "_links": {
                    "self": {
                      "href": "http://osdi-sample-system.org/api/v1/questions/202004"
                    },
                    "curies": [
                      {
                        "name": "osdi",
                        "href": "http://osdi-sample-system.org/osdi#{rel}",
                        "templated": true
                      }
                    ]
                  }
                }
            }
          },
          {
            "sequence": 2,
            "_embedded": {
              "osdi:question": 
                {
                  "origin_system": "OSDISystem",
                  "name": "pbank",
                  "description": "Will you phone bank?",
                  "title": "pbank",
                  "summary": "Will you phone bank?",
                  "question_type": "SingleChoice",
                  "responses": [
                    {
                      "key": "856278",
                      "name": "Yes",
                      "title": "Yes"
                    },
                    {
                      "key": "856279",
                      "name": "No",
                      "title": "No"
                    }
                  ],
                  "identifiers": [
                    "OSDISystem:203079"
                  ],
                  "_links": {
                    "self": {
                      "href": "http://osdi-sample-system.org/api/v1/questions/203079"
                    },
                    "curies": [
                      {
                        "name": "osdi",
                        "href": "http://osdi-sample-system.org/osdi#{rel}",
                        "templated": true
                      }
                    ]
                  }
                }
            }
          },
          {
            "sequence": 3,
            "_embedded": {
              "osdi:question":
                {
                  "origin_system": "OSDISystem",
                  "question_type": "SingleChoice",
                  "identifiers": [
                    "OSDISystem:52472"
                  ],
                  "_links": {
                    "self": {
                      "href": "http://osdi-sample-system.org/api/v1/questions/52472"
                    },
                    "curies": [
                      {
                        "name": "osdi",
                        "href": "http://osdi-sample-system.org/osdi#{rel}",
                        "templated": true
                      }
                    ]
                  }
                }
            }
          }
        ]
    }
}
``` 

_[Back to top...](#)_       


### Scenario: Add question to a script (POST)

Posting to the script questions collection endpoint will allow you to add a new question to an existing script.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/scripts/d91b4b2e-ae0e-4cd3-9ed7-d0ecb0bc3/script_questions

Header:
OSDI-API-Token:[your api key here]

{
    "origin_system": "OSDISystem",
    "sequence": 1,
    "_links" : {
      "osdi:question" : "http://osdi-sample-system.org/api/v1/questions/52472"
    }
}

```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate
{
    "notice": "This question was successfully added."
}
```

_[Back to top...](#)_



### Scenario: Clear all questions in a script (DELETE)

You may clear a script of all its questions by calling the DELETE command on the script questions endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/scripts/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b/script_questions

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "All script questions were cleared."
}
```

_[Back to top...](#)_