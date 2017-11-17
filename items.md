---
layout: default
title: Item
---

# Item

This document defines the Item resource.

Items represent a resource's membership in a list. Items have fields to describe them such as when the item was created and what type of resource it represents and typically are linked to the resource itself.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Item Fields](#item-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Item resources (GET)](#scenario-retrieving-a-collection-of-item-resources-get)
    * [Scenario: Retrieving an individual Item resource (GET)](#scenario-scenario-retrieving-an-individual-item-resource-get)
    * [Scenario: Creating a new item (POST)](#scenario-creating-a-new-item-post)
    * [Scenario: Modifying an item (PUT)](#scenario-modifying-an-item-put)
    * [Scenario: Deleting an item (DELETE)](#scenario-deleting-an-item-delete)
    * [Scenario: Optimized List Item Retrieval (GET)](#scenario-optimized-list-item-retrieval-get)


{% include endpoints_and_url_structures.md %}

The link relation label for a Item resource is ```osdi:item``` for a single Item resource or ```osdi:items``` for a collection of Item resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Item Fields

A list of fields specific to the Item resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this item was created. (ex: "OSDI System")
|item_type		|string			|A property representing the type of resource this item links to. (ex: "osdi:person")

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Item*](items.html)	|A self-referential link to the item.
|[resouce-name]			|[Resource*]		|A link to a single resource of the type indicated in the item_type field, representing the resource linked to the item.
|list		|[List*](lists.html)  		|A link to a List resource representing the list on which this item was created.

_[Back to top...](#)_


## Related Resources

* [List](lists.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Item resources (GET)

Item resources are sometimes presented as collections of items. For example, calling the items endpoint on a particular list will return a collection of all the items in that list.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "total_pages": 10,
    "per_page": 25,
    "page": 1,
    "total_records": 250,
    "_links": {
        "next": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items?page=2"
        },
        "osdi:items": [
            {
                "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/1efc3644-af25-4253-90b8-a0baf12dbd1e"
            },
            //(truncated for brevity)
        ],
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-sample-system.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items"
        }
    },
    "_embedded": {
        "osdi:items": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "item_type": "osdi:person",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:list": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_sample_system:1efc3644-af25-4253-90b8-a0baf12dbd1e"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T20:44:13Z",
                "modified_date": "2014-03-20T20:44:13Z",
                "item_type": "osdi:event",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:list": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:event": {
                        "href": "https://osdi-sample-system.org/api/v1/events/adb951cb-51f9-420e-b7e6-de953195ec86"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Item resource (GET)

Calling an individual Item resource will return the resource directly, along with all associated fields and appropriate links to additional information about the item.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "item_type": "osdi:person",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:list": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new item (POST)

Posting to the items collection endpoint and including a link to an existing resource will allow you to create a new item associated with that list and other resource. The response is the new item that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "item_type": "osdi:person",
    "_links" : {
        "osdi:person" : {
            "href" : "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
        "foreign_system:1"
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "item_type": "osdi:person",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:list": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying an item (PUT)

You can update an item by calling a PUT operation on that item's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/

Header:
OSDI-API-Token:[your api key here]

{
    "item_type": "osdi:event",
    "_links" : {
        "osdi:event" : {
            "href" : "https://osdi-sample-system.org/api/v1/events/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}

```

#### Response
```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
        "foreign_system:1"
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T22:04:31Z",
    "item_type": "osdi:event",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:list": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:events": {
            "href": "https://osdi-sample-system.org/api/v1/events/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting an item (DELETE)

You may delete an item by calling the DELETE command on the item's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This item was successfully deleted."
}
```

_[Back to top...](#)_


### Scenario: Optimized List Item Retrieval (GET)

Where supported by the API provider, a single request may retrieve one item (or a collection of items) along with the resource(s) they represent.  For example, calling the items endpoint on a particular list will return a collection of the items in that list.  If the server optionally embeds into each item the resource to which the item refers, then the client will not need to make further API calls to retrieve the end resource(s).

The following example retrieves a list collection where each item in the embedded list links to an osdi:person resource and also embeds the osdi:person resource within it:


#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items

Header:
OSDI-API-Token:[your api key here]


```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "total_pages": 10,
    "per_page": 25,
    "page": 1,
    "total_records": 250,
    "_links": {
        "next": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items?page=2"
        },
        "osdi:items": [
            {
                "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/1efc3644-af25-4253-90b8-a0baf12dbd1e"
            },
            //(truncated for brevity)
        ],
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-sample-system.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items"
        }
    },
    "_embedded": {
        "osdi:items": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2017-03-20T21:04:31Z",
                "modified_date": "2017-03-20T21:04:31Z",
                "item_type": "osdi:person",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:list": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/5d7d6534-cd24-466a-a698-4f684fa7686e"
                    }
                },
                "_embedded": {
                    "osdi:person": {
                        "_links": {
                            "self": {
                                "href": "https://osdi-sample-system.org/api/v1/people/5d7d6534-cd24-466a-a698-4f684fa7686e",
                                "title": "David Grossman"
                            }
                        },
                        "created_date": "2017-05-20T19:45:51Z",
                        "email_addresses": [
                            {
                                "address": "dgros@sample.com",
                                "primary": true,
                                "status": "subscribed"
                            }
                        ],
                        "family_name": "Grossman",
                        "given_name": "David",
                        "identifiers": [
                            "osdi-sample-system:5d7d6534-cd24-466a-a698-4f684fa7686e"
                        ],
                        "modified_date": "2017-05-20T19:45:51Z",
                        "origin_system": "OSDI Sample System",
                        "postal_addresses": [
                            {
                                "address_lines": [
                                    "123 Creek Drive"
                                ],
                                "locality": "Askov",
                                "postal_code": "55726",
                                "primary": true,
                                "region": "MN"
                            }
                        ]
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_sample_system:1efc3644-af25-4253-90b8-a0baf12dbd1e"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T20:44:13Z",
                "modified_date": "2014-03-20T20:44:13Z",
                "item_type": "osdi:person",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:list": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/5d7d6534-cd24-466a-a698-4f684fa743f3"
                    }
                },
                "_embedded": {
                    "osdi:person": {
                        "_links": {
                            "self": {
                                "href": "https://osdi-sample-system.org/api/v1/people/5d7d6534-cd24-466a-a698-4f684fa743f3",
                                "title": "Christina Gonzalez"
                            }
                        },
                        "created_date": "2017-05-20T13:45:07Z",
                        "email_addresses": [
                            {
                                "address": "xtinag@sample.com",
                                "primary": true,
                                "status": "subscribed"
                            }
                        ],
                        "family_name": "Gonzalez",
                        "given_name": "Christina",
                        "identifiers": [
                            "osdi-sample-system:5d7d6534-cd24-466a-a698-4f684fa743f3"
                        ],
                        "modified_date": "2017-05-20T13:45:07Z",
                        "origin_system": "OSDI Sample System",
                        "postal_addresses": [
                            {
                                "address_lines": [
                                    "1200 18th Ave S"
                                ],
                                "locality": "Peoria",
                                "postal_code": "61601",
                                "primary": true,
                                "region": "IL"
                            }
                        ]
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```

_[Back to top...](#)_
