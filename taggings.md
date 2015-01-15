---
layout: default
title: "Taggings"
---

# Tagging
Taggings are used to associate tags with resources like people (Person)

Tags are associated to resources like people (Person) to indicate customer specific data.  

As an example, a customer might have a tag for volunteers.  Each Person who has signed up to volunteer would have the volunteer tag associated.  Tags are associated to a resource via a Tagging resource.

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Query Fields](#query-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Add a tagging with implied tagged item (GET)](#scenario-add-a-tagging-with-implied-tagged-item-get)
    
{% include endpoints_and_url_structures.md %}

## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_

### Tagging Fields
Tags are binary pieces of information that apply to individual people.

|Name   	|Type   |Description
|---    	|---    |---
|item_type | string | The type of resource to use as a key in links collection. eg "osdi:person"

_[Back to top...](#)_

### Links

|Name   	|Type   |Description
|---    	|---    |---
|resource-type  |link | The tagged item
|tag    	|link |The tag itself

_[Back to top...](#)_

## Related Resources

* [Result](tags.html)

_[Back to top...](#)_

# Scenarios

{% include scenarios_intro.md %}

### Scenario: Add a tagging with implied tagged item (GET)
Lets tag a user with the new tag
User: Martha Stewart, url: http://api.opensupporter.org/api/v1/people/69/taggings

> curl -X POST -d @../taggingcreate.json http://api.opensupporter.org/api/v1/people/69/taggings


### Request
```
POST http://api.opensupporter.org/api/v1/people/69/taggings 

Header:
OSDI-API-Token:[your api key here]

{
     "_links" : {
          "osdi:tag" : {
               "href" : "http://api.opensupporter.org/api/v1/tags/8"
          }
     }
}
```

### Response

```
200 OK

{
  "updated_at": "2014-04-18T20:01:13Z",
  "created_at": "2014-04-18T20:01:13Z",
  "item_type" : "osdi:person"
  "_embedded": {
    "osdi:tag": {
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
  },
  "_links": {
    "self": {
      "href": "http://api.opensupporter.org/api/v1/taggings/5"
    },
    "osdi:tag": {
      "href": "http://api.opensupporter.org/api/v1/tags/8"
    },
    "osdi:person": {
      "href": "http://api.opensupporter.org/api/v1/people/69"
    }
  }
}
```
