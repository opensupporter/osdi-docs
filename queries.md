---
layout: default
title: "Queries"
---

# Queries
A query is a collection of resources that fit a set of criteria.

* Queries are nonarbitrary: a resource's inclusion in the collection is based on attributes intrinsic to that resource
* Queries may only be dynamic: A dynamic query will return the resources which match its criteria at the moment the query is retrieved. To implement a static query, which contains the resources which matched its criteria at the time the query was created, the API's [list object](lists.md) object may be used.
* Queries may only be created, deleted and edited on the content provider's native system; OSDI does not support CRUD operations on queries
* Query metadata may be updated via the API, but query criteria may only be modified and queries may only be created or deleted via the content provider's system
* Queries are unique collections of resources: a resource may match a query only once

| name 	| type	| description	|
|-------|-------|---------------|
| identifiers | Identifier[] | An array of identifiers
| description	| string	| description of the query's function; if possible, enough data to recreate query on the host system	|
| created_date	| timestamp	| time the query was created	|
| origin_system | string    | Human readable identifier of the system where this query was created
| name		| string	| name of the query	|
| total_results	| integer	| number of results in the query	|
| osdi_results | []*	 | the collection of resources which match the query's criteria at the time of the query's creation in static queries or at the time of retrieval in dynamic queries	|

# Results
A result is an individual member of a query, linked to a resource type such as a person. A result can be of any resource type. Results are unique within their query.

**Note:** Because results represent the actual results of a query in real time, unlike other similar resources (like list items), resources that results link to will not themselves display a link back to all results for that resource to protect system resources. For example, a person resource should not have a link to all results that link to that person, as this would easily cause high server load as the system re-runs all queries to determine which queries that person matches at that moment.


| name 	| type	| description	|
|-------|-------|---------------|
| identifiers | Identifier[] | An array of identifiers
| created_date	| timestamp	| time the result was created	|
| origin_system | string    | Human readable identifier of the system where this result was created
| result_type     | string      | the type of result, eg "osdi:person"


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
			"total_result":"3850",
			"_links" : {
				"self": {
            				"href": "https://opensupporter.org/api/v1/queries/22"
          			},
          			"osdi:results": {
            				"href": "https://actionnetwork.org/api/v1/queries/22/results"
          			}
			}
		   },
		    {
			"summary" : "November volunteers",
			"description" : "all volunteers who were avaialble for walks as of November 2013",
			"created_date":"2013-11-30 23:55:23",
			"total_results":"3850",
			"_links" : {
				"self": {
            				"href": "https://opensupporter.org/api/v1/queries/23"
          			},
          			"osdi:results": {
            				"href": "https://actionnetwork.org/api/v1/queries/23/results"
          			}
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
		"total_results":"3850",
		"_links" : {
			"self": {
            			"href": "https://opensupporter.org/api/v1/queries/23"
          		},
          		"osdi:results": {
            			"href": "https://actionnetwork.org/api/v1/queries/23/results"
          		}
		}
	}

## Retrieve the results in a query

### URL
	GET api/v1/query/{id}/results

### Response
	{
	  "total_pages": 5,
	  "per_page": 25,
	  "page": 1,
	  "total_records": 123,
	  "_links": {
	    "next": {
	      "href": "https://opensupporter.org/api/v1/queries/71f8feef-61c8-4e6b-9745-ec1d7752f298/results?page=2"
	    },
	    "self": {
	      "href": "https://opensupporter.org/api/v1/queries/71f8feef-61c8-4e6b-9745-ec1d7752f298/results"
	    },
	    "osdi:results": [
	      {
	        "href": "https://opensupporter.org/api/v1/queries/71f8feef-61c8-4e6b-9745-ec1d7752f298/results/82e909f9-1ac7-4952-bbd4-b4690a14bec2"
	      },
	      {
	        "href": "https://opensupporter.org/api/v1/queries/71f8feef-61c8-4e6b-9745-ec1d7752f298/results/a9ccd87c-97f4-48db-9e6b-507509091839"
	      },
	      //truncated for brevity
	    ],
	    "curies": [
	      {
	        "name": "osdi",
	        "href": "https://opensupporter.org/docs/v1/{rel}",
	        "templated": true
	      }
	    ]
	  },
	  "_embedded": {
	    "osdi:results": [
	      {
	        "_links": {
	          "self": {
	            "href": "https://opensupporter.org/api/v1/queries/71f8feef-61c8-4e6b-9745-ec1d7752f298/results/82e909f9-1ac7-4952-bbd4-b4690a14bec2"
	          },
	          "osdi:query": {
	            "href": "https://opensupporter.org/api/v1/queries/71f8feef-61c8-4e6b-9745-ec1d7752f298"
	          },
	          "osdi:person": {
	            "href": "https://opensupporter.org/api/v1/people/82e909f9-1ac7-4952-bbd4-b4690a14bec2"
	          }
	        },
	        "identifiers": [
	          "open_supporter:82e909f9-1ac7-4952-bbd4-b4690a14bec2"
	        ],
	        "origin_system": "Open Supporter",
	        "created_date": "2014-03-18T22:25:31Z",
	        "modified_date": "2014-03-18T22:25:38Z",
	        "result_type": "osdi:person"
	      },
	      {
	        "_links": {
	          "self": {
	            "href": "https://opensupporter.org/api/v1/queries/71f8feef-61c8-4e6b-9745-ec1d7752f298/results/a9ccd87c-97f4-48db-9e6b-507509091839"
	          },
	          "osdi:query": {
	            "href": "https://opensupporter.org/api/v1/queries/71f8feef-61c8-4e6b-9745-ec1d7752f298"
	          },
	          "osdi:person": {
	            "href": "https://opensupporter.org/api/v1/people/a9ccd87c-97f4-48db-9e6b-507509091839"
	          }
	        },
	        "identifiers": [
	          "open_supporter:a9ccd87c-97f4-48db-9e6b-507509091839"
	        ],
	        "origin_system": "Open Supporter",
	        "created_date": "2014-03-18T22:24:24Z",
	        "modified_date": "2014-03-18T22:24:24Z",
	        "result_type": "osdi:person"
	      },
	      //truncated for brevity
	    ]
	  }
	}
