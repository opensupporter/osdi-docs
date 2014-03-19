# Lists 
Lists are used to denote collections of resources. A list is a resource type that contains list metadata as well as a link to the items collection. The items collection is the actual list resources.

* Lists are arbitrary: the relationship between a list and a member resource is not based on a query or any other criteria
* Lists are editable: resources may be added to or removed from a list (pending a permission structure determined by the content provider)
* Lists are unique collections of resources: only one instance of a resource may belong to a given list
* Lists are dynamic: every time a list is retrieved, it will return the resources belonging to it at the moment of retrieval

## Attributes

| Name          | Type      | Description
|---------------|-----------|--------------
|name			|string     |Name of list
|description	|string     |A description of a list, eg "2012 donors"
|type	        |string     |A string description of the type of resources, eg "events"
|total_items	|integer    |The number of items on the list

## Collections
| Name         	| Type      | Description
|---------------|-----------|--------------
| osdi-items	| Type[]    |A collection of items in the list 

# Scenarios
## Get the list of lists
### URL
    GET api/v1/lists?page=&per_page=
### Response
    200 OK
    Content-Type: application/json

    {
      "total_pages": 5,
      "page": 2,
      "total_records": 25,
      "_embedded": {
        "lists": [
          {
			"name" : "supporters",
			"description" : "The set of all supporters for Ref74",
			"type" : "person",
			"total_items":"666",
			"_links" : {
					"href" : "api/v1/list/23",
					"title" : "R74 supporters"
				}
		   },
          {
			"name" : "venues",
			"description" : "The set of locations willing to host Ref74 events",
			"type" : "locations",
			"total_items":"13",
			"_links" : {
				"osdi-items" : {
					"href" : "api/v1/list/24",
					"title" : "R74 donors"
				}
			}
		   }
		   ...
		   ]

      "_links": {
        "self":{
        	"href":"http://api.opensupporter.org/api/v1/lists?page=2&per_page=5"
        	},
        	next" : {
            "href" : "http://api.opensupporter.org/api/v1/lists?page=3&per_page=5"
            },
        "previous" : {
            "href" : "http://api.opensupporter.org/api/v1/people?page=1&per_page=5"
            }
        },
    }

##Add a resource to a list / remove a resource from a list
### URL
* POST /api/v1/list/{id}
### Payload
{
	"add" :	collection of identifiers/links to resources to add to the list
	"remove" :	collection of identifiers/links to resources to remove from the list
}

### Response
* 204 No Content
	
## Retrieve a full list
### URL
* GET /api/v1/list/{id}
### Response
{
	"name" : "supporters",
	"description" : "The set of all supporters for Ref74",
	"type" : "person",
	"total_items":"666",
	"_links" : {
		"href" : "api/v1/list/23",
		"title" : "R74 supporters"
	}
}

## Create a new list
### URL
* PUT /api/v1/list
### Payload
{
	"name" : string,
	"description" :string,
	"type" : flexnum,
	"osdi-items" : collection of identifiers/links to be added to the list upon creation
}
### Response
* 201 Created
	
## Delete a list
### URL
* DELETE /api/v1/list/{id}
### Response
204 No Content
