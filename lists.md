# Lists Proposals
There are 3 proposals here.

Approach 1 creates a new resource type for lists

Approach 2 uses _links to represent them (like the AEP).

Approach 3 uses URI params to identify the list collection

# Lists (Approach 1 - list as resource type)
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
					"href" : uri,
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


# Lists (Approach 2 - list as just _links)
Lists are server side collections, saved queries or subsets of other collections.  

Each list is represented in a collection of _links where the hash key is the name of the list.  This name should be short and machine/json friendly.

## Link Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
|title			| string	| the name of the list
|description	|string		|A description of a list, eg "2012 donors"
|type	        |string     |A string description of the type of resources, eg "events"
| href			|string		|The URI to the resources


# Scenarios
## Get the list of lists

    GET /api/v1/lists

    200 OK
    Content-Type: application/json

    {
      "total_pages": 1,
      "page": 1,
      "total_records": 1,
      "_links": {
         "supporters" : {
			description" : "The set of all supporters for Ref74 that match criteria",
			"title" : "R74 Supporters"
			"type" : "person",
			"href" : uri,
				
		   },
		  "donors" : {
			"description" : "The set of all 2012 donors for Ref74",
			"title" : "R74 Donors"
			"type" : "person",
			"href" : uri,
				
		   },
        "self": {
          "href": "http://osdi-prototype.herokuapp.com/api/v1/lists"
        },
      }
    }

# Lists (Approach 3)
Lists are not unique resources.  Lists are indicated by URL query parameters. This is a peer to parameters like $filter.

## Selecting a saved list in a request
Saved lists are targeted with the URL query parameter $list.  The $list parameter value is the identifier of a given list.

Assuming an organization has a saved list called 'donors2013', a request to query items from that list would use a URL like:

> /api/v1/people?list=donors2013

