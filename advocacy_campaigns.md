---
layout: default
title: Advocacy Campaign
---

# Advocacy Campaign

This document defines the Advocacy Campaign resource. 

Advocacy campaigns represent an advocacy action directed at targets such as elected officials that a user may participate in by contacting those officials in some way, such as via email or phone. Advocacy campaigns have fields to describe them such as names, titles, summaries, descriptions, and targeting information, and when activists participate in an advocacy campaign, [Outreach](outreaches.html) resources are created representing the individual outreach an activist made to a target as part of that advocacy campaign.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Advocacy Campaign Fields](#advocacy-campaign-fields) 
    * [Related Objects](#related-objects) 
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Advocacy Campaign resources (GET)](#scenario-retrieving-a-collection-of-advocacy-campaign-resources-get)
    * [Scenario: Retrieving an individual Advocacy Campaign resource (GET)](#scenario-scenario-retrieving-an-individual-advocacy-campaign-resource-get)
    * [Scenario: Creating a new advocacy campaign (POST)](#scenario-creating-a-new-advocacy-campaign-post)
    * [Scenario: Modifying an advocacy campaign (PUT)](#scenario-modifying-an-advocacy-campaign-put)
    * [Scenario: Deleting an advocacy campaign (DELETE)](#scenario-deleting-an-advocacy-campaign-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for an Advocacy Campaign resource is ```osdi:advocacy_campaign``` for a single Advocacy Campaign resource or ```osdi:advocacy_campaigns``` for a collection of Advocacy Campaign resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Advocacy Campaign Fields

A list of fields specific to the Advocacy Campaign resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this advocacy campaign was created. (ex: "OSDI System")
|name				|string		|The name of the advocacy campaign. Intended for administrative display rather than a public title, though may be shown to a user.
|title				|string		|The title of the advocacy campaign. Intended for public display rather than administrative purposes.
|description		|string		|A description of the advocacy campaign, usually displayed publicly. May contain text and/or HTML.
|templates		|string[]		|A script to read over the phone, or a general template for a postcard or email. These may be captured in the description, but putting it in the `templates` field allows it to be highlighted by clients. May contain text and/or HTML.
|summary			|string		|A text-only single paragraph summarizing the advocacy campaign. Shown on listing pages that have more than titles, but not enough room for full description.
|targets			|string		|A human readable description of the target universe for this advocacy campaign. (ex: "U.S. Congress")
|browser_url		|string		|A URL string pointing to the publicly available advocacy campaign page on the web.
|featured_image_url		|string		|A URL string pointing to a publicly available featured image file for this advocacy campaign on the web.
|total_outreaches	|integer	|A read-only computed property representing the current count of the total number of outreaches on the advocacy campaign.
|type				|flexunum	|The type of advocacy campaign, specifying how users perform outreaches to targets. One of "email", "in-person", "phone", "postal mail", or another type as needed.
|targets			|[Target[]](#target)    |An array of target object hashes representing the targets of the outreach.
{% include share_options_main_objects.md %}

_[Back to top...](#)_

### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

{% include target_subobject.md %}

{% include share_options_related_objects.md %}

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Advocacy Campaigns*](advocacy_campaigns.html)	|A self-referential link to the advocacy campaign.
|creator		|[Person*](people.html)  		|A link to a single Person resource representing the creator of the advocacy campaign.
|modified_by	|[Person* ](people.html) 		|A link to a Person resource representing the last editor of this advocacy campaign.
|outreaches		|[Outreaches[]*](outreaches.html)	|A link to the collection of Outreach resources for this advocacy campaign.
|record_outreach_helper	|[Record Outreach Helper*](record_outreach.html)	|A link to the Record Outreach Helper resource endpoint for this advocacy campaign.

_[Back to top...](#)_


## Related Resources

* [Outreaches](outreaches.html)
* [Record Outreach Helper](record_outreach.html)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Advocacy Campaign resources (GET)

Advocacy campaign resources are sometimes presented as collections of advocacy campaigns. For example, calling the advocacy campaigns endpoint will return a collection of all the advocacy campaigns stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/advocacy_campaigns/

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
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns?page=2"
        },
        "osdi:advocacy_campaigns": [
            {
                "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns"
        }
    },
    "_embedded": {
        "osdi:advocacy_campaigns": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "Civil Rights Bill 2015 Advocacy Campaign",
                "title": "Tell Congress to pass the 2015 Civil Rights bill",
                "description": "<p>Congress is prepared to pass a civil rights bill.</p><p>Email your member of Congress and tell them to vote yes!</p>",
                "summary": "Congress is prepared to pass a civil rights bill -- tell your member of Congress to vote yes.",
                "target_universe": "U.S. Congress",
                "browser_url": "http://osdi-sample-system.org/advocacy_campaigns/civil-rights-2015",
                "featured_image_url": "http://osdi-sample-system.org/images/civil-rights-image.jpg",
                "type": "email",
                "total_outreaches": 345,
                "share_url": "http://osdi-sample-system.org/advocacy_campaigns/my-campaign/",
                "total_shares": 345,
                "share_options": [
                    {
                        "facebook_share": {
                            "title": "Write your representative!",
                            "description": "Please write today.",
                            "image": "http://odsi-sample-system.org/images/advocacy-share-image.jpg",
                            "total_shares": 100
                        },
                        "twitter_share": {
                            "message": "Write your representative with @OSDI to get rid of the bad things! Click here: http://osdi-sample-system.org/advocacy_campaigns/my-campaign/",
                            "total_shares": 100
                        },
                        "email_share": {
                            "subject": "Write your representatives!",
                            "body": "Can you write your representatives to get rid of the bad things? Click here: http://osdi-sample-system.org/advocacy_campaigns/my-campaign/",
                            "total_shares": 145
                        }
                    }
                ],
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:outreaches": {
                        "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/outreaches"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:record_outreach_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_outreach_helper"
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
                "title": "Call Congress: Raise the minimum wage!",
                "description": "<p>We need $15/hour now!</p>",
                "target_universe": "U.S. Senate",
                "browser_url": "http://osdi-sample-system.org/advocacy_campaigns/raise-the-wage",
                "type": "phone"
                "total_outreaches": 10572,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:outreaches": {
                        "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/1efc3644-af25-4253-90b8-a0baf12dbd1e/outreaches"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:record_outreach_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/1efc3644-af25-4253-90b8-a0baf12dbd1e/record_outreach_helper"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Advocacy Campaign resource (GET)

Calling an individual Advocacy Campaign resource will return the resource directly, along with all associated fields and appropriate links to additional information about the advocacy campaign.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/advocacy_campaigns/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "name": "Civil Rights Bill 2015 Advocacy Campaign",
    "title": "Tell Congress to pass the 2015 Civil Rights bill",
    "description": "<p>Congress is prepared to pass a civil rights bill.</p><p>Email your member of Congress and tell them to vote yes!</p>",
    "summary": "Congress is prepared to pass a civil rights bill -- tell your member of Congress to vote yes.",
    "target_universe": "U.S. Congress",
    "browser_url": "http://osdi-sample-system.org/advocacy_campaigns/civil-rights-2015",
    "featured_image_url": "http://osdi-sample-system.org/images/civil-rights-image.jpg",
    "type": "email",
    "total_outreaches": 345,
    "share_url": "http://osdi-sample-system.org/advocacy_campaigns/my-campaign/",
    "total_shares": 345,
    "share_options": [
        {
            "facebook_share": {
                "title": "Write your representative!",
                "description": "Please write today.",
                "image": "http://odsi-sample-system.org/images/advocacy-share-image.jpg",
                "total_shares": 100
            },
            "twitter_share": {
                "message": "Write your representative with @OSDI to get rid of the bad things! Click here: http://osdi-sample-system.org/advocacy_campaigns/my-campaign/",
                "total_shares": 100
            },
            "email_share": {
                "subject": "Write your representatives!",
                "body": "Can you write your representatives to get rid of the bad things? Click here: http://osdi-sample-system.org/advocacy_campaigns/my-campaign/",
                "total_shares": 145
            }
        }
    ],
    // Campaigns may be targeted toward a specific representative. In that
    // case, it might make sense to use the `target` field to include contact
    // info inline:
    "targets": [
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
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:outreaches": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/outreaches"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:record_outreach_helper": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_outreach_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new advocacy campaign (POST)

Posting to the advocacy campaign collection endpoint will allow you to create a new advocacy campaign. The response is the new advocacy campaign that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/advocacy_campaigns/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "name": "Civil Rights Bill 2015 Advocacy Campaign",
    "title": "Tell Congress to pass the 2015 Civil Rights bill",
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
    "name": "Civil Rights Bill 2015 Advocacy Campaign",
    "title": "Tell Congress to pass the 2015 Civil Rights bill",
    "total_outreaches": 0,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:outreaches": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/outreaches"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:record_outreach_helper": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_outreach_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying an advocacy campaign (PUT)

You can update an advocacy campaign by calling a PUT operation on that advocacy campaign's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "name": "Civil Rights Bill 2015-2016 Advocacy Campaign"
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
    "name": "Civil Rights Bill 2015-2016 Advocacy Campaign",
    "title": "Tell Congress to pass the 2015 Civil Rights bill",
    "total_signatures": 0,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:outreaches": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/outreaches"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:record_outreach_helper": {
            "href": "https://osdi-sample-system.org/api/v1/advocacy_campaigns/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_outreach_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting an advocacy campaign (DELETE)

You may delete an advocacy campaign by calling the DELETE command on the advocacy campaign's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/advocacy_campaigns/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This advocacy campaign was successfully deleted."
}
```

_[Back to top...](#)_