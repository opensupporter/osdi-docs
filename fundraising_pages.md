---
layout: default
title: Fundraising Page
---

# Fundraising Page

This document defines the Fundraising Page resource. 

Fundraising pages represent a page on a website that can take donations or other types of payment from end users. Fundraising pages have fields to describe them such as names, titles, summaries, and descriptions, and when activists submit a fundraising page and are charged money, [Donation](donations.html) resources are created representing the individual donation an activist made on that fundraising page.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Fundraising Page Fields](#fundraising-page-fields)  
    * [Related Objects](#related-objects) 
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Fundraising Page resources (GET)](#scenario-retrieving-a-collection-of-fundraising-page-resources-get)
    * [Scenario: Retrieving an individual Fundraising Page resource (GET)](#scenario-scenario-retrieving-an-individual-fundraising-page-resource-get)
    * [Scenario: Creating a new fundraising page (POST)](#scenario-creating-a-new-fundraising-page-post)
    * [Scenario: Modifying a fundraising page (PUT)](#scenario-modifying-a-fundraising-page-put)
    * [Scenario: Deleting a fundraising page (DELETE)](#scenario-deleting-a-fundraising-page-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Fundraising Page resource is ```osdi:fundraising_page``` for a single Fundraising Page resource or ```osdi:fundraising_pages``` for a collection of Fundraising Page resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Fundraising Page Fields

A list of fields specific to the Fundraising Page resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this fundraising page was created. (ex: "OSDI System")
|name				|string		|The name of the fundraising page. Intended for administrative display rather than a public title, though may be shown to a user.
|title				|string		|The title of the fundraising page. Intended for public display rather than administrative purposes.
|description		|string		|A description of the fundraising page, usually displayed publicly. May contain text and/or HTML.
|summary			|string		|A text-only single paragraph summarizing the fundraising page. Shown on listing pages that have more than titles, but not enough room for full description.
|browser_url		|string		|A URL string pointing to the publicly available fundraising page page on the web.
|featured_image_url		|string		|A URL string pointing to a publicly available featured image file for this fundraising page on the web.
|total_donations	|integer	|A read-only computed property representing the current count of the total number of donations on the fundraising page.
|total_amount	|float	|A read-only computed property representing the current count of the total amount of money raised on the fundraising page.
|currency		|string	|ISO 4217 designation of currency. (ex: "USD" or "JPY")
{% include share_options_main_objects.md %}

_[Back to top...](#)_


### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

{% include share_options_related_objects.md %}

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Fundraising Page*](fundraising_pages.html)	|A self-referential link to the fundraising page.
|creator		|[Person*](people.html)  		|A link to a single Person resource representing the creator of the fundraising page.
|modified_by	|[Person* ](people.html) 		|A link to a Person resource representing the last editor of this fundraising page.
|donations		|[Donations[]*](donations.html)	|A link to the collection of Donation resources for this fundraising page.
|record_donation_helper	|[Record Donation Helper*](record_donation.html)	|A link to the Record Donation Helper resource endpoint for this fundraising page.

_[Back to top...](#)_


## Related Resources

* [Donation](donations.html)
* [Record Donation Helper](record_donation.html)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Fundraising Page resources (GET)

Fundraising page resources are sometimes presented as collections of fundraising pages. For example, calling the fundraising pages endpoint will return a collection of all the fundraising pages stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/fundraising_pages/

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
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages?page=2"
        },
        "osdi:fundraising_pages": [
            {
                "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages"
        }
    },
    "_embedded": {
        "osdi:fundraising_pages": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "2014 End Of Year Donations",
                "title": "Give to support us at the end of the year!",
                "description": "<p>It's time for our end of year fundraising push.</p><p>Please give generously!</p>",
                "summary": "It's time for our end of year fundraising push.",
                "browser_url": "http://osdi-sample-system.org/fundraising_pages/give-to-support-us",
                "featured_image_url": "http://osdi-sample-system.org/images/donate-image.jpg",
                "total_donations": 345,
                "total_amount": 4567.21,
                "currency": "USD",
                "share_url": "http://osdi-sample-system.org/fundraising_pages/my-fundraiser/",
                "total_shares": 345,
                "share_options": [
                    {
                        "facebook_share": {
                            "title": "Support us at the end of the year!",
                            "description": "Please give generously.",
                            "image": "http://odsi-sample-system.org/images/fundraiser-share-image.jpg",
                            "total_shares": 100
                        },
                        "twitter_share": {
                            "message": "Give to @OSDI at the end of the year! Click here: http://osdi-sample-system.org/fundraising_pages/my-fundraiser/",
                            "total_shares": 100
                        },
                        "email_share": {
                            "subject": "Give to us at the end of the year!",
                            "body": "Can you give? Click here: http://osdi-sample-system.org/fundraising_pages/my-fundraiser/",
                            "total_shares": 145
                        }
                    }
                ],
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:donations": {
                        "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:record_donation_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_donation_helper"
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
                "title": "Become a monthly donor",
                "description": "<p>Please become a monthly donor today!</p>",
                "total_donations": 43,
                "total_amount": 1298.25,
                "currency": "USD",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:donations": {
                        "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/1efc3644-af25-4253-90b8-a0baf12dbd1e/donations"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:record_donation_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/1efc3644-af25-4253-90b8-a0baf12dbd1e/record_donation_helper"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Fundraising Page resource (GET)

Calling an individual Fundraising Page resource will return the resource directly, along with all associated fields and appropriate links to additional information about the fundraising page.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/fundraising_pages/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "name": "2014 End Of Year Donations",
    "title": "Give to support us at the end of the year!",
    "description": "<p>It's time for our end of year fundraising push.</p><p>Please give generously!</p>",
    "summary": "It's time for our end of year fundraising push.",
    "browser_url": "http://osdi-sample-system.org/fundraising_pages/give-to-support-us",
    "featured_image_url": "http://osdi-sample-system.org/images/donate-image.jpg",
    "total_donations": 345,
    "total_amount": 4567.21,
    "currency": "USD",
    "share_url": "http://osdi-sample-system.org/fundraising_pages/my-fundraiser/",
    "total_shares": 345,
    "share_options": [
        {
            "facebook_share": {
                "title": "Support us at the end of the year!",
                "description": "Please give generously.",
                "image": "http://odsi-sample-system.org/images/fundraiser-share-image.jpg",
                "total_shares": 100
            },
            "twitter_share": {
                "message": "Give to @OSDI at the end of the year! Click here: http://osdi-sample-system.org/fundraising_pages/my-fundraiser/",
                "total_shares": 100
            },
            "email_share": {
                "subject": "Give to us at the end of the year!",
                "body": "Can you give? Click here: http://osdi-sample-system.org/fundraising_pages/my-fundraiser/",
                "total_shares": 145
            }
        }
    ],
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:record_donation_helper": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_donation_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new fundraising page (POST)

Posting to the fundraising page collection endpoint will allow you to create a new fundraising page. The response is the new fundraising page that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/fundraising_pages/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "name": "2014 End Of Year Donations",
    "title": "Give to support us at the end of the year!",
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
    "name": "2014 End Of Year Donations",
    "title": "Give to support us at the end of the year!",
    "total_donations": 0,
    "total_amount": 0,
    "currency": "USD",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:record_donations_helper": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_donations_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a fundraising page (PUT)

You can update a fundraising page by calling a PUT operation on that fundraising page's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "name": "2014 End Of Year Donations (version 1)"
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
    "name": "2014 End Of Year Donations (version 1)",
    "title": "Give to support us at the end of the year!",
    "total_donations": 0,
    "total_amount": 0,
    "currency": "USD",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:record_donations_helper": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_donations_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a fundraising page (DELETE)

You may delete a fundraising page by calling the DELETE command on the fundraising page's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/fundraising_pages/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This fundraising page was successfully deleted."
}
```

_[Back to top...](#)_