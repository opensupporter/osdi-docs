---
layout: default
title: "Status"
---
# Status
OSDI reports errors and status information according to a standard schema.
This is done via the osdi:status resource

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Fields](#status-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Returning Simple Status Information](#scenario-simple-status-information)
    * [Scenario: Returning  Complex Status Information](#scenario-complex-status-information)

{% include endpoints_and_url_structures.md %}

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_

## Status Fields

| Name          | Type      | Description
|-----------    |-----------|--------------
| code			| integer	| A numeric status code. 
| description	| string	| A text description of the status
| trace			| Array[Status]| Additional trace information such as step-wise status.  Represented as an array of Status resources

## Related Resources

* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}


### Scenario: Simple status information

#### Request

````javascript
POST /api/v1/people

{ // imagine a request body that causes a failure }
````

#### Response

````
500 Error
Content-Type: application/json

{
	"osdi:status" : {
		"code" : 500,
		"description": "This system does not support direct creation of people"
	}
}
````

_[Back to top...](#)_	

### Scenario: Complex Status Information

Since person_signup_helper, like other helpers, performs multiple operations in a single request.  The helper upserts a person as well as adds tags and lists associations to the person.

As a result, on some systems it is possible to have the person upsert succeed while tagging or list additions could fail.

The osdi:status trace attribute provides the ability for the server to indicate to the client detailed status.

Whether or not a server returns trace information is vendor-specific.

#### Request
````javascript
POST /api/v1/people_signup_helper
Header:
OSDI-API-Token:[your api key here]

{ // imagine a bad person_signup_helper body }
````

#### Response
````javascript
500 Error
Content-Type: application/json

{
	"osdi:status" : {
		"code" : 500,
		"description": "Tagging failure"
		"trace" : [
			{ 
				"code" : 200,
				"description" : "person update successful"
			},
			{
				"code" : 500,
				"description" : "Tagging 'volunteer' failed. No such tag"
			},
			{
				"code" : 200,
				"description" : "List donors successful"
			}
		]
	}
}
````