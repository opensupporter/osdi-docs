---
layout: default
title: Outreach
---

# Outreach

This document defines the Outreach resource. 

Outreaches are a type of action that a user may take by participating in an [advocacy campaign](advocacy_campaigns.html). Outreaches have fields to describe them such as when the outreach was created, who the user contacted as the target of their advocacy, and the content of the message a user sent to that target, and typically are linked to the person who made the outreach.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Outreach Fields](#outreach-fields)  
    * [Related Objects](#related-objects)
    * [Links](#links)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Outreach resources (GET)](#scenario-retrieving-a-collection-of-outreach-resources-get)
    * [Scenario: Retrieving an individual Outreach resource (GET)](#scenario-scenario-retrieving-an-individual-outreach-resource-get)
    * [Scenario: Creating a new outreach (POST)](#scenario-creating-a-new-outreach-post)
    * [Scenario: Modifying an outreach (PUT)](#scenario-modifying-an-outreach-put)
    * [Scenario: Deleting an outreach (DELETE)](#scenario-deleting-an-outreach-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Outreach resource is ```osdi:outreach``` for a single Outreach resource or ```osdi:outreaches``` for a collection of Outreach resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Outreach Fields

A list of fields specific to the Outreach resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this outreach was created. (ex: "OSDI System")
|action_date		|string		|The date and time the outreach was made by the person.
|type				|flexunum	|The type of outreach, specifying how the user performed the outreach to targets. One of "email", "in-person", "phone", "postal mail", or another type as needed.
|duration		|integer		|The duration in seconds of the outreach, if applicable. (ex: duration will only be present on phone outreach types)
|subject		|string		|The subject of the outreach, if applicable. (ex: subject will only be present on email outreach types)
|message		|string		|The message of the outreach, if applicable. (ex: message will only be present on email or postal mail outreach types)
|notes		|string		|Notes left by the person doing the outreach, if any. For example, any feedback they got from the person they called.
|referrer_data		|[Referrer Data*](#referrer-data)	|An object hash representing referrer and sourcing information about this outreach.
|targets			|[Target[]](#target)    |An array of target object hashes representing the targets of the outreach.

_[Back to top...](#)_

### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

{% include target_subobject.md %}

#### Referrer Data

|Name          |Type      |Description
|-----------    |-----------|--------------
|referrer_data.source	|string    |The source code that was used when this outreach was created. Typically used to track individual links, such as a post on social media or a link in a specific email. (ex: "facebook-101016-mainpage")
|referrer_data.referrer	|string    |The code or ID representing a person or group that referred this outreach. Typically used to track which person referred the person who made this outreach. (ex: "jane-doe")
|referrer_data.website	|string    |The top level domain of the website where the person clicked from to then subsequently make this outreach. (ex: "facebook.com")
|referrer_data.url	|string    |The specific URL where the person clicked from to then subsequently make this outreach. (ex: "https://facebook.com/posts/12345")

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Outreach*](outreachs.html)	|A self-referential link to the outreach.
|person			|[Person*](people.html)		|A link to a single Person resource representing the person who made the outreach.
|advocacy_campaign		|[Advocacy Campaign*](advocacy_campaigns.html)  		|A link to an Advocacy Campaign resource representing the advocacy campaign on which this outreach was created.

_[Back to top...](#)_


## Helpers

{% include helpers_intro.md %}

|Name          |Description
|-----------    |-----------
|[record_outreach_helper](record_outreach.html)      |Allows the creation of an outreach and a person at the same time.

_[Back to top...](#)_


## Related Resources

* [Record Outreach Helper](record_outreach.html)
* [Advocacy Campaign](advocacy_campaigns.html)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Outreach resources (GET)

Outreach resources are sometimes presented as collections of outreaches. For example, calling the outreaches endpoint on a particular advocacy campaign will return a collection of all the outreaches made on that advocacy campaign.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches

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
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches?page=2"
        },
        "osdi:outreaches": [
            {
                "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches"
        }
    },
    "_embedded": {
        "osdi:outreaches": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "action_date": "2014-03-18T11:02:15Z",
                "type": "email",
                "subject": "Vote no!",
                "message": "Please vote no on HR 100.",
                "referrer_data": {
                    "source": "facebook-101016-mainpage",
                    "referrer": "jane-doe",
                    "website": "facebook.com",
                    "url": "https://facebook.com/posts/12345"
                },
                // You may wish to explicitly record the target of the outreach
                // inline:
                "targets": [
                    {
                        "title": "Senator",
                        "given_name": "John",
                        "family_name": "Smith",
                        "organization": "U.S. Senate",
                        "ocdid": "ocd-division/country:us/state:ny"
                    },
                    {
                        "title": "Senator",
                        "given_name": "Jennifer",
                        "family_name": "Larson",
                        "organization": "U.S. Senate",
                        "ocdid": "ocd-division/country:us/state:ny",
                        "postal_addresses": [
                            {
                                "primary": true,
                                "address_type": "Home",
                                "address_lines": [
                                    "1900 Pennsylvania Ave"
                                ],
                                "locality": "Washington",
                                "region": "DC",
                                "postal_code": "20009",
                                "country": "US",
                                "language": "en",
                                "location": {
                                    "latitude": 38.919,
                                    "longitude": -77.0379,
                                    "accuracy": "Rooftop"
                                },
                                "last_verified_date": "2014-03-20T21:04:31Z"
                            }
                        ],
                        "email_addresses": [
                            {
                                "primary": true,
                                "address": "johnsmith@mail.com",
                                "address_type": "Personal",
                            }
                        ],
                        "phone_numbers": [
                            {
                                "primary": true,
                                "number": "11234567890",
                                "extension": "432",
                                "description": "Worksite line",
                                "number_type": "Work",
                                "operator": "ATT",
                                "country": "US",
                                "sms_capable": false,
                                "do_not_call": true
                            }
                        ]
                    }
                ],
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:advocacy_campaign": {
                        "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29"
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
                "type": "email",
                "subject": "Don't do it!",
                "message": "Vote no tomorrow!",
                "referrer_data": {
                    "source": "email-101116-subjecttest1"
                },
                "targets": [
                    {
                        "title": "Senator",
                        "given_name": "Jane",
                        "family_name": "Doe",
                        "organization": "U.S. Senate",
                        "ocdid": "ocd-division/country:us/state:va"
                    }
                },
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:advocacy_campaign": {
                        "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29"
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

### Scenario: Scenario: Retrieving an individual Outreach resource (GET)

Calling an individual Outreach resource will return the resource directly, along with all associated fields and appropriate links to additional information about the outreach.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

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
    "type": "email",
    "subject": "Vote no!",
    "message": "Please vote no on HR 100.",
    "referrer_data": {
        "source": "facebook-101016-mainpage",
        "referrer": "jane-doe",
        "website": "facebook.com",
        "url": "https://facebook.com/posts/12345"
    },
    "targets": [
        {
            "title": "Senator",
            "given_name": "John",
            "family_name": "Smith",
            "organization": "U.S. Senate",
            "ocdid": "ocd-division/country:us/state:ny"
        },
        {
            "title": "Senator",
            "given_name": "Jennifer",
            "family_name": "Larson",
            "organization": "U.S. Senate",
            "ocdid": "ocd-division/country:us/state:ny"
        }
    ],
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:advocacy_campaign": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new outreach (POST)

Posting to the outreaches collection endpoint and including a link to an existing Person resource will allow you to create a new outreach associated with that advocacy campaign and person. The response is the new outreach that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

For information on how to create a person along with an outreach, see the [Record Outreach Helper](record_outreach.html) documentation.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "action_date": "2014-03-18T11:02:15Z",
    "type": "phone",
    "duration": 120,
    "referrer_data": {
        "source": "api"
    },
    "targets": [
        {
            "title": "Senator",
            "given_name": "John",
            "family_name": "Smith",
            "organization": "U.S. Senate",
            "ocdid": "ocd-division/country:us/state:ny"
        },
        {
            "title": "Senator",
            "given_name": "Jennifer",
            "family_name": "Larson",
            "organization": "U.S. Senate",
            "ocdid": "ocd-division/country:us/state:ny"
        }
    ],
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
    "type": "phone",
    "duration": 120,
    "referrer_data": {
        "source": "api"
    },
    "targets": [
        {
            "title": "Senator",
            "given_name": "John",
            "family_name": "Smith",
            "organization": "U.S. Senate",
            "ocdid": "ocd-division/country:us/state:ny"
        },
        {
            "title": "Senator",
            "given_name": "Jennifer",
            "family_name": "Larson",
            "organization": "U.S. Senate",
            "ocdid": "ocd-division/country:us/state:ny"
        }
    ],
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:advocacy_campaign": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying an outreach (PUT)

You can update an outreach by calling a PUT operation on that outreach's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/

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
    "modified_date": "2014-03-20T21:04:31Z",
    "action_date": "2014-03-17T11:02:15Z",
    "type": "phone",
    "duration": 120,
    "referrer_data": {
        "source": "facebook-101016-mainpage",
        "referrer": "jane-doe",
        "website": "facebook.com",
        "url": "https://facebook.com/posts/12345"
    },
    "targets": [
        {
            "title": "Senator",
            "given_name": "John",
            "family_name": "Smith",
            "organization": "U.S. Senate",
            "ocdid": "ocd-division/country:us/state:ny"
        },
        {
            "title": "Senator",
            "given_name": "Jennifer",
            "family_name": "Larson",
            "organization": "U.S. Senate",
            "ocdid": "ocd-division/country:us/state:ny"
        }
    ],
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:advocacy_campaign": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting an outreach (DELETE)

You may delete an outreach by calling the DELETE command on the outreach's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/advocacy_campaigns/c945d6fe-929e-11e3-a2e9-12313d316c29/outreaches/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This outreach was successfully deleted."
}
```

_[Back to top...](#)_