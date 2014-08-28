# Lists 
Lists are used to denote collections of resources. A list is a resource type that contains list metadata as well as a link to the items collection. The items collection is the actual list resources.

* Lists are arbitrary: the relationship between a list and a member resource is not based on a query or any other criteria
* Lists are editable: resources may be added to or removed from a list (pending a permission structure determined by the content provider)
* Lists are unique collections of resources: only one instance of a resource may belong to a given list
* Lists are dynamic: every time a list is retrieved, it will return the resources belonging to it at the moment of retrieval

## Attributes

| Name          | Type      | Description
<<<<<<< HEAD
|-----------    |-----------|--------------
|identifier		|string		|A internally unique identifier, usually URL friendly
|name		    |string     |Name of list
|description	|string		|A description of a list, eg "2012 donors"
|type	        |string     |A string description of the type of resources, eg "events"
|is_dynamic		|bool		|A boolean value that indicates if the list is static or dynamic
=======
|---------------|-----------|--------------
|name			|string     |Name of list
|description	|string     |A description of a list, eg "2012 donors"
|type	        |string     |A string description of the type of resources, eg "events"
|total_items	|integer    |The number of items on the list
>>>>>>> deccfa27072f453dcdf43f10c39a0487083e97a0

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
          	"id" : "1",
			"name" : "Ref74 Supporters",
			"description" : "The set of all supporters for Ref74",
<<<<<<< HEAD
			"type" : "osdi:people",
			"is_dynamic" : false,
			"total_members" 3043, # computed field
			"_links" : {
				"self" : {
					"href" : "api/v1/list/1"
				},
				"members" : {
					"href" : "api/v1/people?list=1",
=======
			"type" : "person",
			"total_items":"666",
			"_links" : {
					"href" : "api/v1/list/23",
					"title" : "R74 supporters"
>>>>>>> deccfa27072f453dcdf43f10c39a0487083e97a0
				}
		   },
          {
<<<<<<< HEAD
          	"id" : "2",
			"name" : "Ref74 Donors",
			"description" : "The set of all 2012 donors for Ref74",
			"type" : "osdi:people",
			"is_dynamic" : false,
			"total_members" 3043, # computed field
			"_links" : {
				"self" : {
					"href" : "api/v1/list/2"
				},
				"members" : {
					"href" : "",
=======
			"name" : "venues",
			"description" : "The set of locations willing to host Ref74 events",
			"type" : "locations",
			"total_items":"13",
			"_links" : {
				"osdi-items" : {
					"href" : "api/v1/list/24",
					"title" : "R74 donors"
>>>>>>> deccfa27072f453dcdf43f10c39a0487083e97a0
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

<<<<<<< HEAD
### Get a list
  	GET /api/v1/list/1

  	200 OK
    Content-Type: application/json

  	{
  			"id" : 1,
			"name" : "Ref74 Supporters",
			"description" : "The set of all supporters for Ref74",
			"type" : "osdi:people",
			"total_members" 3043, # computed field
			"is_dynamic" : false,
			"created": datetime,
			"updated": datetime,
			"_links" : {
				"osdi:members" : {
					"href" : "api/v1/people?list=1",
				}
			}
	}

### Create a new list
	POST /api/v1/lists

	{
		"name": "Ref74 Volunteers",
		"type": "osdi:people",
		"description": "A list containing all of our volunteers"
	}

### Add a person to a list
	POST /api/v1/list/1/members

	Content-Type: application/json

	{	
		"data" : Person object
	}

	OR

	{
		"identifier" : "osdi:12345"
	}

	OR

	{
		"guid" : "c1e1d0d0-b562-0130-dc7c-168c51e904de"
	}

### Remove a person from a list
	DELETE /api/v1/list/1/members/12345

### Get members of a list

	GET /api/v1/people?list=1

	OR

	GET /api/v1/list/1/members

	{
    	"total_pages": 1,
    	"page": 1,
    	"total_records": 1,
    	"type": "osdi:people",
    	"_embedded" : {
    		"osdi:people" : [
	    		{
	    			"first_name": "Beyonce",
	    			...
	    		},
	    		...
	    	]
    	},
    	"_links": {
        	"self": {
          		"href": "http://osdi-prototype.herokuapp.com/api/v1/list/1/members"
        	},
        	"osdi:list": {
        		"href": "http://osdi-prototype.herokuapp.com/api/v1/list/1/"
        	}
      	}
    }
=======
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
	"type" : flexenum,
	"osdi-items" : collection of identifiers/links to be added to the list upon creation
}
### Response
* 201 Created
	
## Delete a list
### URL
* DELETE /api/v1/list/{id}
### Response
204 No Content
>>>>>>> deccfa27072f453dcdf43f10c39a0487083e97a0
