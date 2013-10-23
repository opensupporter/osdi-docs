# Lists 
Lists are server side collections, saved queries or subsets of other collections.  

A list is a resource type that contains list metadata as well as a link to the items collection.  The items collection is the actual list resources.

## Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
|name		    |string     |Name of list
|description	|string		|A description of a list, eg "2012 donors"
|type	        |string     |A string description of the type of resources, eg "events"



## Collections
| Name          | Type      | Description
|-----------    |-----------|--------------
| items			| Type[]	|A collection of items in the list 

# Scenarios
## Get the list of lists

    GET /api/v1/lists

    200 OK
    Content-Type: application/json

    {
      "total_pages": 1,
      "page": 1,
      "total_records": 1,
      "_embedded": {
        "lists": [
          {
			"name" : "supporters",
			"description" : "The set of all supporters for Ref74",
			"type" : "person",
			"_links" : {
				"items" : {
					"href" : "api/v1/people?list=supporters",
					"title" : "R74 supporters"
				}
			}
		   },
          {
			"name" : "donors",
			"description" : "The set of all 2012 donors for Ref74",
			"type" : "person",
			"_links" : {
				"items" : {
					"href" : uri,
					"title" : "R74 donors"
				}
			}
		   }


      "_links": {
        "self": {
          "href": "http://osdi-prototype.herokuapp.com/api/v1/lists"
        },
      }
    }

