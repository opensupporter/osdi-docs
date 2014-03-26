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
GET /api/v1/tags
### Response
200 OK

	{
	"total_pages": 5,
	"page": 2,
	"total_records": 25,
	"_embedded": {
		"tags": [
				{
					"name":"labor",
					"description":"this person is a labor supporter",
					"created_at":"2014-01-01 00:00:00",
					"modified_at":"2014-02-28 11:23:23",
					"originating_system":"voterlabs",
					"identifiers":[
						"voterlabs:987654",
						"datafarm:poisdfg"
					],
					"_links" : {
						"items" : {
							"href" : "api/v1/people?filter=tag eq 'voterlabs:987654'",
						}
					}
				},
				{
					"name":"reproductive rights",
					"description":"this person supports a right to reproductive choice",
					"created_at":"2014-01-01 00:00:00",
					"modified_at":"2014-02-28 11:23:23",
					"originating_system":"voterlabs",
					"identifiers":[
						"voterlabs:9538267"
					],
					"_links" : {
						"items" : {
							"href" : "api/v1/people?filter=tag eq 'voterlabs:9538267'"
						}
					}
				}
				....
			]
		 "_links": {
	        "self":{
	        	"href":"api/v1/tags?page=2&per_page=5"
	        	},
	    	next" : {
	            "href" : "api/v1/tags?page=3&per_page=5"
	            },
	        "previous" : {
	            "href" : "api/v1/tags?page=1&per_page=5"
	            }
	        },
	    }
	}

## Retrieve a single tag
### URL
GET /api/v1/tag/_namespace:id_
### Response
200 OK

	{
		"name":"labor",
		"description":"this person is a labor supporter",
		"created_at":"2014-01-01 00:00:00",
		"modified_at":"2014-02-28 11:23:23",
		"originating_system":"voterlabs",
		"identifiers":[
			"voterlabs:987654",
			"datafarm:poisdfg"
		],
		"_links" : {
			"items" : {
				"href" : "api/v1/people?filter=tag eq 'voterlabs:987654'",
			}
		}
	}


## Create a new tag
### URL
POST /api/v1/tags
### Payload
	{
		"name":_string_,
		"description":_optional string_,
		"identifiers":[
			_namespace:id_
			]
	}
### Response
201 Created

    {
      "name":_string_,
      "description":_string_,
      "identifiers":[
        _namespace:id_
      ],
      "_links" : {
        "items" : {
          "href" : "api/v1/tags/_namespace:id_"
        }
      }
    }

## Add a tag to a person
### URL
PUT /api/v1/person/tag/_namespace:id_
### Payload
    {
    "tag id" : "_namespace:id_"
    }
### Response
204 No Content

## Remove a tag from a person
### URL
DELETE /api/v1/person/tag
### Payload
    {
    "person id" : "_namespace:id_",
    "tag id" : "_namespace:id_"
    }
### Response
204 No Content

## Find people with a given tag
### URL
GET api/v1/people?filter=tag eq _namespace:id_
### Response
200 OK

    {
      "total_pages": 5,
      "page": 2,
      "total_records": 25,
      "people":[
        "person": {
              "href": "http://osdi-prototype.herokuapp.com/api/v1/people/_namespace:id_"
            },
            "person": {
              "href": "http://osdi-prototype.herokuapp.com/api/v1/people/_namespace:id_"
            }
            "person": {
              "href": "http://osdi-prototype.herokuapp.com/api/v1/people/_namespace:id_"
            }
            ....
      ]
    }
