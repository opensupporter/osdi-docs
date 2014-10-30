---
layout: default
title: "Questions"
---

# Survey Questions and Answers

This document defines the Question and Answer resources. Questions are used in both Surveys and Forms. Answers are generally associated with questions as a collection.

## Field names and descriptions

### Question

| Name          | Type      | Description
|-----------    |-----------|--------------
|identifier			|Identifier[]		|Array of identifiers
|name			|string		|Name for the question
|question       |string     |Human readable text of the question
|question_type  |Flex Enum     |One of [MultiChoice, Freeform]

### QuestionResponse
A possible response or choice for a question.

| Name          | Type      | Description
|-----------    |-----------|--------------
|identifier			|Identifier[]		|Array of identifiers
|name       |string     |Human readable text of the answer
|value		|string		|Actual value
|default	|boolean	|True if this response should be the default response


## Scenario: Retrieving Available Questions

### Request
    GET https://osdi-sample-system.org/api/v1/questions/
    
    Header:
    OSDI-API-Token:[your api key here]

### Response

    200 OK
    Content-Type: application/json
    
    {
      "total_pages": 88,
      "per_page": 2,
      "page": 1,
      "total_records": 176,
      "_links": {
        "next": {
          "href": "https://osdi-sample-system.org/api/v1/questions?page=2"
        }
      },
      "_embedded": {
        "questions": [
          {
            "name": "best_editor",
            "question": "What is the best editor?",
            "question_type": "MultiChoice",
            "identifiers": [1],
            "_embedded": {
              "osdi:question_responses": [
                {
                  "name": "Emacs",
                  "value": "Emacs",
                  "default": true,
                  "identifiers": ["osdi_sample_system:10"],
                  "_links": {
                    "self": {
                      "href": "https://osdi-sample-system.org/api/v1/question_responses/10"
                    }
                  }
    
                },
                {
                  "name": "vi",
                  "value": "vi",
                  "default": false,
                  "identifiers": ["osdi_sample_system:11"],
                  "_links": {
                    "self": {
                      "href": "https://osdi-sample-system.org/api/v1/question_responses/11"
                    }
                  }
                }
              ]
            },
            "_links": {
              "osdi:question_responses": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/questions/1/question_responses"
              },
              "self": {
                "href": "https://osdi-sample-system.org/api/v1/questions/1"
              }
            }
          },
          {
            "name": "best_fruit",
            "question": "What is the best fruit?",
            "question_type": "MultiChoice",
            "identifiers": [2],
            "_embedded": {
              "osdi:question_responses": [{
                "name": "Bananas",
                "value": "banana",
                "default": false,
                "identifiers": [11],
                "_links": {
                  "self": {
                    "href": "https://osdi-sample-system.org/api/v1/question_responses/11"
                  }
                }
              },
              {
                "name": "apple",
                "value": "apple",
                "default": false,
                "identifiers": [12],
                "_links": {
                  "self": {
                    "href": "https://osdi-sample-system.org/api/v1/question_responses/11"
                  }
                }
              }
            ]},
            "_links": {
              "osdi:question_responses": { "href": "http://osdi-prototype.herokuapp.com/api/v1/questions/1/question_responses"}, 
              "self": {
                "href": "https://osdi-sample-system.org/api/v1/questions/2"
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
