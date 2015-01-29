---
layout: default
title: Petition
---

# Petition

This document defines the Petition resource. 

Petitions represent an action directed at a target that a user may sign by submitting their information. Petitions have fields to describe them such as names, titles, summaries, and descriptions, and when activists submit a petition, [Signature](signatures.html) resources are created representing the individual signature an activist made on that petition.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Petition Fields](#petition-fields)  
    * [Related Objects](#related-objects)
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Petition resources (GET)](#scenario-retrieving-a-collection-of-petition-resources-get)
    * [Scenario: Retrieving an individual Petition resource (GET)](#scenario-scenario-retrieving-an-individual-petition-resource-get)
    * [Scenario: Creating a new petition (POST)](#scenario-creating-a-new-petition-post)
    * [Scenario: Modifying a petition (PUT)](#scenario-modifying-a-petition-put)
    * [Scenario: Deleting a petition (DELETE)](#scenario-deleting-a-petition-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Petition resource is ```osdi:petition``` for a single Petition resource or ```osdi:petitions``` for a collection of Petition resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Petition Fields

A list of fields specific to the Petition resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this petition was created. (ex: "OSDI System")
|name				|string		|The name of the petition. Intended for administrative display rather than a public title, though may be shown to a user.
|title				|string		|The title of the petition. Intended for public display rather than administrative purposes.
|description		|string		|A description of the petition, usually displayed publicly. May contain text and/or HTML.
|summary			|string		|A text-only single paragraph summarizing the petition. Shown on listing pages that have more than titles, but not enough room for full description.
|petition_text		|string		|The text of the petition letter to the target.
|browser_url		|string		|A URL string pointing to the publicly available petition page on the web.
|total_signatures	|integer	|A read-only computed property representing the current count of the total number of signatures on the petition.
|target				|[Targets[]](#targets)	|An array of target object hashes associated with this petition.

_[Back to top...](#)_


### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Targets

|Name          |Type      |Description
|-----------    |-----------|--------------
|target.name	|string    	|The name of the target

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Petition*](petitions.html)	|A self-referential link to the petition.
|creator		|[Person*](people.html)  		|A link to a single Person resource representing the creator of the petition.
|modified_by	|[Person* ](people.html) 		|A link to a Person resource representing the last editor of this petition.
|signatures		|[Signatures[]*](signatures.html)	|A link to the collection of Signature resources for this petition.
|record_signature_helper	|[Record Signature Helper*](record_signature.html)	|A link to the Record Signature Helper resource endpoint for this petition.

_[Back to top...](#)_


## Related Resources

* [Signature](signatures.html)
* [Record Signature Helper](record_signature.html)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Petition resources (GET)

Petition resources are sometimes presented as collections of petitions. For example, calling the petitions endpoint will return a collection of all the petitions stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/petitions/

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
            "href": "https://osdi-sample-system.org/api/v1/petitions?page=2"
        },
        "osdi:petitions": [
            {
                "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/petitions/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/petitions"
        }
    },
    "_embedded": {
        "osdi:petitions": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "Acme Co Petition",
                "title": "Tell Acme Co To Stop Doing The Bad Thing",
                "description": "<p>Acme Co is doing a bad thing!</p><p>Sign this petition to tell them to stop.</p>",
                "summary": "Acme Co is doing a bad thing!",
                "petition_text": "To: Acme Co -- Stop doing the bad thing!",
                "browser_url": "http://osdi-sample-system.org/petitions/acme-co-stop-doing-the-bad-thing",
                "total_signatures": 345,
                "target": [
                    {
                        "name": "Jane Doe, CEO, Acme Co"
                    },
                    {
                        "name": "John Smith, Chairman, Acme Co"
                    }
                ],
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:signatures": {
                        "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:record_signature_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_signature_helper"
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
                "title": "Congress: Raise the minimum wage!",
                "description": "<p>We need $15/hour now!</p>",
                "petition_text": "Congress, pass the minimum wage increase now!",
                "browser_url": "http://osdi-sample-system.org/petitions/raise-the-wage",
                "total_signatures": 10572,
                "target": [
                    {
                        "name": "Congress"
                    }
                ],
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/petitions/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:signatures": {
                        "href": "https://osdi-sample-system.org/api/v1/petitions/1efc3644-af25-4253-90b8-a0baf12dbd1e/signatures"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:record_signature_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/petitions/1efc3644-af25-4253-90b8-a0baf12dbd1e/record_signature_helper"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Petition resource (GET)

Calling an individual Petition resource will return the resource directly, along with all associated fields and appropriate links to additional information about the petition.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/petitions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "name": "Acme Co Petition",
    "title": "Tell Acme Co To Stop Doing The Bad Thing",
    "description": "<p>Acme Co is doing a bad thing!</p><p>Sign this petition to tell them to stop.</p>",
    "summary": "Acme Co is doing a bad thing!",
    "petition_text": "To: Acme Co -- Stop doing the bad thing!",
    "browser_url": "http://osdi-sample-system.org/petitions/acme-co-stop-doing-the-bad-thing",
    "total_signatures": 345,
    "target": [
        {
            "name": "Jane Doe, CEO, Acme Co"
        },
        {
            "name": "John Smith, Chairman, Acme Co"
        }
    ],
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:record_signature_helper": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_signature_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new petition (POST)

Posting to the petition collection endpoint will allow you to create a new petition. The response is the new petition that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/petitions/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "title": "Tell Acme Co To Stop Doing The Bad Thing",
    "name": "Acme Co Petition",
    "origin_system": "OpenSupporter"
}
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
    "origin_system": "OpenSupporter",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "Acme Co Petition",
    "title": "Tell Acme Co To Stop Doing The Bad Thing",
    "total_signatures": 0,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:record_signature_helper": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_signature_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a petition (PUT)

You can update a petition by calling a PUT operation on that petition's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "name": "Acme Co Petition [December 2014]"
}

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
    "origin_system": "OpenSupporter",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T22:04:31Z",
    "name": "Acme Co Petition [December 2014]",
    "title": "Tell Acme Co To Stop Doing The Bad Thing",
    "total_signatures": 0,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:record_signature_helper": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_signature_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a petition (DELETE)

You may delete a petition by calling the DELETE command on the petition's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/petitions/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This petition was successfully deleted."
}
```

_[Back to top...](#)_