# API Entry Point
## Attributes


| Name			| Type		| Description
|---------------|-----------|---------------------------
| max_pagesize	| string	| a number that defines how many records a server can return in a single query.  
| motd			| string	| an informational message from the server
| people		| Person[]	|A reference to the Persons Collection
| events		| Event[]	|A reference to the Events Collection
| attendances	| Attendance[]|	A reference to the Attendance Collection
| donations		| Donation[]| A reference to the Donation collection
|questions		| Question[]| A reference to the Question collection
|question_answers|QuestionAnswer[]|	A reference to the questionAnswer collection.
|Interactions	|Interaction[]|	A reference to the Interaction collection

# Retrieving the API endpoint
## Request

	GET /api/v1 HTTP/1.1

## Response

~~~~
200 OK
Content-Length: nn
Content-Type: application/json

{
  "motd": "Welcome to the ACME Action Platform OSDI API endpoint!!",
  "_links": {
    "people": {
      "href": "/api/v1/people",
      "title": "The collection of people in the system"
    },
    "questions": {
      "href": "http://osdi-prototype.herokuapp.com/api/v1/questions",
      "title": "The collection of questions in the system"
    },
    "question_answers": {
      "href": "http://osdi-prototype.herokuapp.com/api/v1/question_answers",
      "title": "The collection of question answers in the system"
    },
    "self": {
      "href": "/api/v1",
      "title": "The root API Entry Point (Your are here)"
    },
    "http://localhost:3000/Readme.md": {
      "href": "http://localhost:3000/Readme.md",
      "title": "Documentation:",
      "name": "Docs",
      "index": "index"
    }
  }
}
~~~~