---
layout: default
title: Question Resource
---

# Survey Question

This document defines the Question resource.

Questions together make up a survey.  Examples include "Do you support John Doe for City Council?", "Do you approve or disapprove of the way Barak Obama is handling his job as president?"

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Resource Fields](#resource-fields)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of resources (GET)](#scenario-retrieving-a-collection-of-resources-get)
    * [Scenario: Retrieving an individual resource (GET)](#scenario-scenario-retrieving-an-individual-resource-get)
    * [Scenario: Creating a new resource (POST)](#scenario-creating-a-new-resource-post)
    * [Scenario: Modifying a resource (PUT)](#scenario-modifying-a-resource-put)
    * [Scenario: Deleting a resource (DELETE)](#scenario-deleting-a-resource-delete)


{% include endpoints_and_url_structures.md %}


The link relation label for a Example Resource resource is ```osdi:example_resource``` for a single Example Resource resource or ```osdi:example_resources``` for a collection of Example Resource resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_

### Question Fields

| Name          | Type                | Description
| -----------   | -----------         | --------------
| identifier    | Identifier[]        | Array of identifiers
| name          | string              | Name for the question
| question      | string              | Human readable text of the question
| question_type | string              | One of "MultiChoice"
| responses     | QuestionResponse[]* | A collection of possible responses


## Related Resources

* [Person](#)
* [Response](#)


## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving Available Questions (GET)

### Request

```javascript
GET /api/v1/questions HTTP/1.1

Header:
OSDI-API-Token:[your api key here]
```

### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "_embedded": {
    "questions": [
      {
        "name": "Best Editor",
        "question": "What is the best editor?",
        "question_type": "MultiChoice",
        "id": 1,
        "_embedded": {
          "osdi:question_responses": [
            {
              "name": "Emacs",
              "value": "Emacs",
              "default": true,
              "_links": {
                "self": {
                  "href": "http://osdi-prototype.herokuapp.com/api/v1/question_responses/1"
                }
              }
            },
            {
              "name": "Vi",
              "value": "Vi",
              "default": false,
              "_links": {
                "self": {
                  "href": "http://osdi-prototype.herokuapp.com/api/v1/question_responses/2"
                }
              }
            }
          ]
        },
        "_links": {
          "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
          "osdi:question_responses": { "href": "http://osdi-prototype.herokuapp.com/api/v1/questions/1/question_responses"}, 
          "self": {
            "href": "http://osdi-prototype.herokuapp.com/api/v1/questions/1"
          }
        }
      },
      {
        "name": "Marriage Equality",
        "question": "Gays should have the right to Marry?",
        "question_type": "MultiChoice",
        "id": 2,
        "_embedded": {
          "osdi:question_responses": [
            {
              "name": "Strongly Support",
              "value": "5",
              "default": true,
              "_links": {
                "self": {
                  "href": "http://osdi-prototype.herokuapp.com/api/v1/question_responses/3"
                }
              }
            },
            {
              "name": "Strongly Oppose",
              "value": "1",
              "default": false,
              "_links": {
                "self": {
                  "href": "http://osdi-prototype.herokuapp.com/api/v1/question_responses/4"
                }
              }
            }
          ]
        },
        "_links": {
          "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
          "osdi:question_responses": { "href": "http://osdi-prototype.herokuapp.com/api/v1/questions/1/question_responses"}, 
          "self": {
            "href": "http://osdi-prototype.herokuapp.com/api/v1/questions/2"
          }
        }
      },
      {
        "name": "Bio",
        "question": "Tell us about yourself",
        "question_type": "Paragraph",
        "id": 3,
        "_embedded": {
          "osdi:question_responses": []
        },
        "_links": {
          "self": {
            "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
            "osdi:question_responses": { "href": "http://osdi-prototype.herokuapp.com/api/v1/questions/1/question_responses"}, 
            "href": "http://osdi-prototype.herokuapp.com/api/v1/questions/3"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "http://osdi-prototype.herokuapp.com/api/v1/questions"
    }
  }
}
```

_[Back to top...](#)_






