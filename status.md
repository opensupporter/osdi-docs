# Status
OSDI reports errors and status information according to a standard schema.
This is done via the osdi:status resource

## Issues
Should status codes be vendor specific or standard?
Should status codes need to align with the HTTP status code of the HTTP response

## Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
| code			| integer	| A numeric status code. 
| description	| string	| A text description of the status
| trace			| Array[Status]| Additional trace information such as step-wise status.  Represented as an array of Status resources
 

# Scenarios / Examples

> JSON respresenations below are provided as an informative reflection of what the wire format would look like.  
> The tables above are the authoritative specification of the attributes.  Any discrepancy should defer to the above tables.

## Simple status information
### A POST to people collection
This request fails.

    POST /api/v1/people

    500 ErrorK
    Content-Type: application/json

	{
		"osdi:status" : {
			"code" : 500,
			"description": "This system does not support direct creation of people"
		}
	}


## Status with trace information
Since person_signup_helper, like other helpers, performs multiple operations in a single request.  The helper upserts a person as well as adds tags and lists associations to the person.

As a result, on some systems it is possible to have the person upsert succeed while tagging or list additions could fail.

The osdi:status trace attribute provides the ability for the server to indicate to the client detailed status.

Whether or not a server returns trace information is vendor-specific.

### A POST to person_signup_helper

    POST /api/v1/people_signup_helper

    500 ErrorK
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