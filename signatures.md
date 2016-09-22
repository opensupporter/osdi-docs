---
layout: default
title: Signature
---

# Signature

This document defines the Signature resource. 

Signatures are a type of action that a user may take by completing a petition. Signatures have fields to describe them such as when the signature was created and typically are linked to the person who made the signature.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Signature Fields](#signature-fields)  
    * [Related Objects](#related-objects)
    * [Links](#links)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Signature resources (GET)](#scenario-retrieving-a-collection-of-signature-resources-get)
    * [Scenario: Retrieving an individual Signature resource (GET)](#scenario-scenario-retrieving-an-individual-signature-resource-get)
    * [Scenario: Creating a new signature (POST)](#scenario-creating-a-new-signature-post)
    * [Scenario: Modifying a signature (PUT)](#scenario-modifying-a-signature-put)
    * [Scenario: Deleting a signature (DELETE)](#scenario-deleting-a-signature-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Signature resource is ```osdi:signature``` for a single Signature resource or ```osdi:signatures``` for a collection of Signature resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Signature Fields

A list of fields specific to the Signature resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this signature was created. (ex: "OSDI System")
|action_date		|string		|The date and time the signature was made by the person.
|comments		|string			|The comments left by the person when the signature was created.
|referrer_data		|[Referrer Data*](#referrer-data)	|An object hash representing referrer and sourcing information about this signature.

_[Back to top...](#)_


### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Referrer Data

|Name          |Type      |Description
|-----------    |-----------|--------------
|referrer_data.source	|string    |The source code that was used when this signature was created. Typically used to track individual links, such as a post on social media or a link in a specific email. (ex: "facebook-101016-mainpage")
|referrer_data.referrer	|string    |The code or ID representing a person or group that referred this signature. Typically used to track which person referred the person who made this signature. (ex: "jane-doe")
|referrer_data.website	|string    |The top level domain of the website where the person clicked from to then subsequently make this signature. (ex: "facebook.com")
|referrer_data.url	|string    |The specific URL where the person clicked from to then subsequently make this signature. (ex: "https://facebook.com/posts/12345")

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Signature*](signatures.html)	|A self-referential link to the signature.
|person			|[Person*](people.html)		|A link to a single Person resource representing the person who signed the petition.
|petition		|[Petition*](petitions.html)  		|A link to a Petition resource representing the petition on which this signature was created.

_[Back to top...](#)_


## Helpers

{% include helpers_intro.md %}

|Name          |Description
|-----------    |-----------
|[record_signature_helper](record_signature.html)      |Allows the creation of a signature and a person at the same time.

_[Back to top...](#)_


## Related Resources

* [Record Signature Helper](record_signature.html)
* [Petition](petitions.html)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Signature resources (GET)

Signature resources are sometimes presented as collections of signatures. For example, calling the signatures endpoint on a particular petition will return a collection of all the signatures made on that petition.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures

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
            "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures?page=2"
        },
        "osdi:signatures": [
            {
                "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures"
        }
    },
    "_embedded": {
        "osdi:signatures": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "action_date": "2014-03-18T11:02:15Z",
                "comments": "Please stop doing the bad thing!",
                "referrer_data": {
                    "source": "facebook-101016-mainpage",
                    "referrer": "jane-doe",
                    "website": "facebook.com",
                    "url": "https://facebook.com/posts/12345"
                },
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:petition": {
                        "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29"
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
                "action_date": "2014-03-12T01:45:34Z",
                "referrer_data": {
                    "source": "email-101116-subjecttest1"
                },
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:petition": {
                        "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/adb951cb-51f9-420e-b7e6-de953195ec86"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Signature resource (GET)

Calling an individual Signature resource will return the resource directly, along with all associated fields and appropriate links to additional information about the signature.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

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
    "action_date": "2014-03-18T11:02:15Z",
    "comments": "Please stop doing the bad thing!",
    "referrer_data": {
        "source": "facebook-101016-mainpage",
        "referrer": "jane-doe",
        "website": "facebook.com",
        "url": "https://facebook.com/posts/12345"
    },
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:petition": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new signature (POST)

Posting to the signatures collection endpoint and including a link to an existing Person resource will allow you to create a new signature associated with that petition and person. The response is the new signature that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

For information on how to create a person along with a signature, see the [Record Signature Helper](record_signature.html) documentation.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "action_date": "2014-03-18T11:02:15Z",
    "comments": "Please stop!",
    "referrer_data": {
        "source": "api"
    },
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
    "action_date": "2014-03-18T11:02:15Z",
    "comments": "Please stop!",
    "referrer_data": {
        "source": "api"
    },
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:petition": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a signature (PUT)

You can update a signature by calling a PUT operation on that signature's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/

Header:
OSDI-API-Token:[your api key here]

{
    "action_date": "2014-03-17T11:02:15Z"
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
    "action_date": "2014-03-17T11:02:15Z",
    "comments": "Please stop!",
    "referrer_data": {
        "source": "facebook-101016-mainpage",
        "referrer": "jane-doe",
        "website": "facebook.com",
        "url": "https://facebook.com/posts/12345"
    },
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:petitions": {
            "href": "https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a signature (DELETE)

You may delete a signature by calling the DELETE command on the signature's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/petitions/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This signature was successfully deleted."
}
```

_[Back to top...](#)_