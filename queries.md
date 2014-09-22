---
layout: default
title: "Queries"
---

# Queries
A query is a collection of resources that fit a set of criteria

* Queries are nonarbitrary: a resource's inclusion in the collection is based on attributes intrinsic to that resource
* Queries may only be dynamic: A dynamic query will return the resources which match its criteria at the moment the query is retrieved. To implement a static query, which contains the resources which matched its criteria at the time the query was created, the API's list object may be used.
* Queries may only be created, deleted and edited on the content provider's native system; OSDI does not support 
* Query metadata may be updated via the API, but query criteria may only be modified and queries may only be created or deleted via the content provider's system
* Queries are unique collections of resources: a resource may match a query only once

| name 	| type	| description	|
|-------|-------|---------------|
| identifiers | Identifier[] | An array of identifiers
| description	| string	| description of the query's function; if possible, enough data to recreate query on the host system	|
| created_date	| timestamp	| time the query was created	|
| item_type     | string      | the type of item, eg "osdi:person"
| origin_system | string    | Human readable identifier of the system where this query was created
| name		| string	| name of the query	|
| total_items	| integer	| number of items in the query	|
| osdi_items | []*	 | the collection of resources which match the query's criteria at the time of the query's creation in static queries or at the time of retrieval in dynamic queries	|

# Scenarios

## Retrieve a list of all queries

### URL
	GET api/v1/queries?page=2&per_page=5

### Response
	{
      "total_pages": 5,
      "page": 2,
      "total_records": 25,
      "_embedded": {
        "queries": [
          {
			"summary" : "trivia participants",
			"description" : "people who participate in one of our labor history trivia challenges (tag = TRIVIA)",
			"created_date":"2014-03-17 20:23:23",
			"total_items":"3850",
			"_links" : {
					"href" : "api/v1/query/23"
				}
		   },
		    {
			"summary" : "November volunteers",
			"description" : "all volunteers who were avaialble for walks as of November 2013",
			"created_date":"2013-11-30 23:55:23",
			"item_type" : "osdi:person",
			"created\_at":"2013-11-30 23:55:23",
			"total_items":"3850",
			"_links" : {
					"href" : "api/v1/query/23"
				}
		   },
		   ...
		   ]

      "_links": {
        "self":{
        	"href":"http://api.opensupporter.org/api/v1/queries?page=2&per_page=5"
        	},
        	next" : {
            "href" : "http://api.opensupporter.org/api/v1/queries?page=3&per_page=5"
            },
        "previous" : {
            "href" : "http://api.opensupporter.org/api/v1/queries?page=1&per_page=5"
            }
        },
    }


## Retrieve a query with matching resources

### URL
	GET api/v1/query/{id}

### Response
	{
		"summary" : "November volunteers",
		"description" : "all volunteers who were avaialble for walks as of November 2013",
		"created_date":"2013-11-30 23:55:23",
        	"origin_system": "OpenSupporter",
		"total_items":"3850",
		"_links" : {
			"osdi:items" : {
			"href" : "http://api.opensupporter.org/api/v1/query/23/items"
			}
		}
	}

