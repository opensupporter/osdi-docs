---
layout: default
title: "Tags"
---

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Query Fields](#query-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Query resources (GET)](#scenario-retrieving-a-collection-of-query-resources-get)
    * [Scenario: Retrieving an individual Query resource (GET)](#scenario-scenario-retrieving-an-individual-query-resource-get)
    * [Scenario: Creating a new query (POST)](#scenario-creating-a-new-query-post)
    * [Scenario: Modifying a query (PUT)](#scenario-modifying-a-query-put)
    * [Scenario: Deleting a query (DELETE)](#scenario-deleting-a-query-delete)


{% include endpoints_and_url_structures.md %}

## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


# Tags Fields
Tags are binary pieces of information that apply to individual people.

|Name   |Type   |Description
|---    |---    |---
|name   |string |name of tag
|description    |string |plaintext meaning of the tag


_[Back to top...](#)_


### Links
Tag resources have no links. Relevant links for tags can be found on the tagging resource.

## Related Resources
* [Tagging](tagging.md)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Create a new tag (POST)

To create a tag, send a json document containing the tag name and description

#### Request

> curl -X POST -d @tagcreate.json http://api.opensupporter.org/api/v1/tags

```
POST http://osdi-sample-system.org/api/v1/tags
Header:
OSDI-API-Token:[your api key here]

/* tagcreate.json */
{
     "name" : "acme-team",
     "description" : "Indicates a member of the acme team"
}
```

#### Response

```
{
  "name": "acme-team",
  "description": "Indicates a member of the acme team",
  "updated_at": "2014-04-18T19:15:31Z",
  "created_at": "2014-04-18T19:15:31Z",
  "_embedded": {
  },
  "_links": {
    "self": {
      "href": "http://api.opensupporter.org/api/v1/tags/8"
    }
  }
}
```

## Scenario Finding a tag reference for use in tagging by using odata query (GET)

> curl -v -G --data-urlencode "filter=name eq 'acme-team'" "http://osdi-sample-system/api/v1/tags"

#### Request
````javascript
http://osdi-sample-system.org/api/v1/tags?filter=name eq 'acme-team'

Header:
OSDI-API-Token:[your api key here]
````

### Response
```
200 OK

{
  "_embedded": {
    "osdi:tags": [
      {
        "name": "acme-team",
        "description": "Indicates a member of the acme team",
        "updated_at": "2014-04-18T19:15:31Z",
        "created_at": "2014-04-18T19:15:31Z",
        "_embedded": {
        },
        "_links": {
          "self": {
            "href": "http://api.opensupporter.org/api/v1/tags/8"
          }
        }
      }
    ]
  },
  "_links": {
    "self": {
      "href": "http://api.opensupporter.org/api/v1/tags"
    }
  }
}
```
