---
layout: default
title: "Questions"
---

# Survey Questions and Answers

## Question
### Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
|identifier			|Identifier[]		|Array of identifiers
|name			|string		|Name for the question
|question       |string     |Human readable text of the question
|question_type  |string     |One of "MultiChoice"
|responses      |QuestionResponse[]*|A collection of possible responses

## QuestionResponse
A possible response or choice for a question.

### Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
|identifier			|Identifier[]		|Array of identifiers
|name       |string     |Human readable text of the value
|value		|string		|Actual value
|default	|boolean	|True if this response should be the default response

## QuestionAnswer
An answer to a question.  An answer is chosen by the user from one of the QuestionResponse options

### Attributes
| Name          | Type      | Description
|-----------    |-----------|--------------
|identifier		|Identifier[]		|Array of identifiers
|value          |string     |Human readable text of the value
|question		|Question*	|Reference to associated question
|person			|Person*	|Reference to associated person


## Retrieving Available Questions

Request

	GET /api/v1/questions HTTP/1.1

Response

~~~~
200 OK
Content-Type: application/json

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
~~~~

## Creating a QuestionAnswer

Request

	POST /api/v1/people/question_answers HTTP/1.1
	Content-Type: application/json

	{
		"value" : "Emacs",
		"question_id" : 5
	}
	
Response
