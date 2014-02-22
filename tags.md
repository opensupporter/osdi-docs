# Tags
Tags are binary pieces of information that apply to individual people.

## Attributes
|Name	|Type	|Description
|---	|---	|---
|name	|string	|name of tag
|description	|string	|plaintext meaning of the tag
|identifiers	|identifier[]	|A collection of identifiers the provider has determined to be associated with the tag
|parent	|string (optional)	|broader-scope tag containing this tag

# Scenarios
## Get the list of tags
GET /api/v1/tags

200 OK
Content-type: application/json

	{
		"total_pages": 1,
		"page": 1,
		"total_records": 1,
		"_embedded": {
			"tags": [
				{
					"name":"labor",
					"description":"this person is a labor supporter",
					"identifiers":[
						"voterlabs:987654",
						"datafarm:poisdfg"
					],
					"_links" : {
						"items" : {
							"href" : "api/v1/people?tag=labor",
						}
					}
				},
				{
					"name":"minimum wage",
					"description":"this person supports an increase in the minimum wage",
					"parent":"labor",
					"identifiers":[
						"voterlabs:987654",
						"datafarm:poisdfg"
					],
					"_links" : {
						"items" : {
							"href":"api/v1/people?tag=minimum_wage",
							"parent":"api/v1/people?tag=labor"
						}
					}
				},
				{
					"name":"collective bargaining",
					"description":"this person supports a right to collective bargaining",
					"parent":"labor",
					"identifiers":[
						"voterlabs:6549843",
						"datafarm:dgktjcd"
					],
					"_links" : {
						"items" : {
							"href" : "api/v1/people?tag=collective_bargaining",
							"parent":"api/v1/people?tag=labor"
						}
					}
				},
				{
					"name":"reproductive rights",
					"description":"this person supports a right to reproductive choice",
					"identifiers":[
						"voterlabs:9538267"
					],
					"_links" : {
						"items" : {
							"href" : "api/v1/people?tag=reproductive_rights"
						}
					}
				},
				]
			 "_links": {
			 "self": {
			 "href": "http://osdi-prototype.herokuapp.com/api/v1/tags"
			},
		      }
		    }
	}
	
## Get the list of child tags
GET /api/v1/tags/children/labor

## Add a tag to a person

## Remove a tag from a person

## Find people with a given tag/value

200 OK
Content-type: application/json

	{
		"total_pages": 1,
		"page": 1,
		"total_records": 1,
		"_embedded": {
			"tags": [
				{
					"name":"minimum wage",
					"description":"this person supports an increase in the minimum wage",
					"parent":"labor",
					"identifiers":[
						"voterlabs:987654",
						"datafarm:poisdfg"
					],
					"_links" : {
						"items" : {
							"href" : "api/v1/people?list=minimum_wage",
						}
					}
				},
				{
					"name":"collective bargaining",
					"description":"this person supports a right to collective bargaining",
					"parent":"labor",
					"identifiers":[
						"voterlabs:6549843",
						"datafarm:dgktjcd"
					],
					"_links" : {
						"items" : {
							"href" : "api/v1/people?list=collective_bargaining",
						}
					}
				}
			]
			 "_links": {
			 "self": {
			 "href": "http://osdi-prototype.herokuapp.com/api/v1/tags/children/labor"
			},
		      }
		    }
	}

