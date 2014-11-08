---
layout: default
title: "Tags"
---

# Tags
Tags are binary pieces of information that apply to individual people.

|Name   |Type   |Description
|---    |---    |---
|name   |string |name of tag
|description    |string |plaintext meaning of the tag

# Tagging
A `tagging` is a one-to-one collection between a `tag` and another resource such as an `event` or `person`. 

|Name   	|Type   |Description
|---    	|---    |---
|resource_type | string | The type of resource being linked, such as "osdi:person" or "osdi"event".  A more detailed explanation is provided below.
|resource |link | The tagged item
|tag    	|link |The tag itself

Additional comments about `resource_type`: As a `tagging` can link a `tag` to a variety of resources (`person`, `event`, `donation`,etc) the `resource_type` variable servers two primary purposes.  

The first purpose is that it is used to determine the type of resource to which a `tagging` should be applied when a non-implied `tagging` is created via POST.  

The second purpose is that the resource type allows resources to be grouped together by type in a response object.  For example, the same `tag` may be applied to both an `event` and a `person` using a tagging.  When creating a response, the server will not return both `event` and `person` resources in a single collection, but rather group the `event` and `person` resources into seperate collections using the `resource_type` as a the key.  This allows the consumer of the API to be able to quickly look only at the tagged resource types for which they are concerned. I.E. A consumer might only be interested in which `event` resources are linked to a `tag` through a `tagging` and not interested in which `person` resources also are linked to the same `tag` through a `tagging`.

# Scenarios

## Create a new tag

To create a tag, send a json document containing the tag name and description

### Request

> curl -X POST -d @tagcreate.json http://api.opensupporter.org/api/v1/tags

```
/* tagcreate.json */
{
     "name" : "acme-team",
     "description" : "Indicates a member of the acme team"
}
```

### Response

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

## Finding a tag reference for use in tagging by using odata query

> curl -v -G --data-urlencode "filter=name eq 'acme-team'" "http://localhost:3000/api/v1/tags"

### Response
```
{
  "per_page": 1,
  "page": 1,
  "total_records": 1,
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

## Add a tagging (Implied tagged_item)
Lets tag a user with the new tag
User: Martha Stewart, url: http://api.opensupporter.org/api/v1/people/69/taggings

> curl -X POST -d @../taggingcreate.json http://api.opensupporter.org/api/v1/people/69/taggings


### Request
```
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
