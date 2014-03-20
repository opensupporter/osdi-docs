# Tags
Tags are binary pieces of information that apply to individual people.

## Attributes
|Name	|Type	|Description
|---	|---	|---
|name	|string	|name of tag
|description	|string	|plaintext meaning of the tag
|identifiers	|identifier[]	|An array of identifiers the provider has determined to be associated with the tag

# Scenarios
## Get the list of tags
### URL
* GET /api/v1/tags
### Response

* 200 OK
	{
	"total\_pages": 5,
	"page": 2,
	"total\_records": 25,
	"\_embedded": {
		"tags": [
				{
					"name":"labor",
					"description":"this person is a labor supporter",
					"identifiers":[
						"voterlabs:987654",
						"datafarm:poisdfg"
					],
					"\_links" : {
						"items" : {
							"href" : "api/v1/people?filter=tag eq 'voterlabs:987654'",
						}
					}
				},
				{
					"name":"reproductive rights",
					"description":"this person supports a right to reproductive choice",
					"identifiers":[
						"voterlabs:9538267"
					],
					"\_links" : {
						"items" : {
							"href" : "api/v1/people?filter=tag eq 'voterlabs:9538267'"
						}
					}
				}
				....
			]
		 "\_links": {
	        "self":{
	        	"href":"api/v1/tags?page=2&per\_page=5"
	        	},
	    	next" : {
	            "href" : "api/v1/tags?page=3&per\_page=5"
	            },
	        "previous" : {
	            "href" : "api/v1/tags?page=1&per\_page=5"
	            }
	        },
	    }
	}

## Create a new tag
### URL
* POST /api/v1/tags
### Payload
	{
		"name":_string_,
		"description":_optional string_,
		"identifiers":[
			_namespaced identifiers_
			]
	}
### Response
* 201 Created
{
	"name":_string_,
	"description":_string_,
	"identifiers":[
		_namespaced identifiers_
	],
	"_links" : {
		"items" : {
			"href" : "api/v1/tags/_namespaced identifier_"
		}
	}
}

## Add a tag to a person
### URL
* PUT /api/v1/person/_{person id}_tag
### Payload
{
	"tag id" : _tag id_
}
### Response
* 204 No Content

## Remove a tag from a person
### URL
* DELETE /api/v1/person/tag
### Payload
{
	"person id" : _person identifier_,
	"tag id" : _tag identifier_
}
### Response
* 204 No Content

## Find people with a given tag
### URL
* GET api/v1/people?filter=tag eq _tag identifier_
### Response
* 200 OK
{
	"total_pages": 5,
	"page": 2,
	"total_records": 25,
	"people":[
		"person": {
          "href": "http://osdi-prototype.herokuapp.com/api/v1/people/23"
        },
        "person": {
          "href": "http://osdi-prototype.herokuapp.com/api/v1/people/33"
        }
        "person": {
          "href": "http://osdi-prototype.herokuapp.com/api/v1/people/66"
        }
        ....
	]
}
