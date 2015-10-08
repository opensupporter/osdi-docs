---
layout: default
title: Share Page
---

# Share Page

This document defines the Share Page resource. 

Share pages represent a page on a website that is used to share content (including other pages) with others, chiefly through social media or email. Share pages have fields to describe them such as names, titles, summaries, and descriptions, and have attributes to describe the default language and other attributes that should be used when activists use the page to share content.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Share Page Fields](#share-page-fields)  
    * [Related Objects](#related-objects)
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Share Page resources (GET)](#scenario-retrieving-a-collection-of-share-page-resources-get)
    * [Scenario: Retrieving an individual Share Page resource (GET)](#scenario-scenario-retrieving-an-individual-share-page-resource-get)
    * [Scenario: Creating a new share page (POST)](#scenario-creating-a-new-share-page-post)
    * [Scenario: Modifying a share page (PUT)](#scenario-modifying-a-share-page-put)
    * [Scenario: Deleting a share page (DELETE)](#scenario-deleting-a-share-page-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Share Page resource is ```osdi:share_page``` for a single Share Page resource or ```osdi:share_pages``` for a collection of Share Page resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Share Page Fields

A list of fields specific to the Share Page resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this share page was created. (ex: "OSDI System")
|name				|string		|The name of the share page. Intended for administrative display rather than a public title, though may be shown to a user.
|title				|string		|The title of the share page. Intended for public display rather than administrative purposes.
|description		|string		|A description of the share page, usually displayed publicly. May contain text and/or HTML.
|summary			|string		|A text-only single paragraph summarizing the share page. Shown on listing pages that have more than titles, but not enough room for full description.
|browser_url		|string		|A URL string pointing to the publicly available share page page on the web.
|total_shares	|integer	|A read-only computed property representing the current count of the total number of times the share page has been used by activists.
|facebook_share	|[Facebook Share](#facebook-share)    |An object hash representing the default language and attributes used when an activist shares on Facebook.
|twitter_share	|[Twitter Share](#twitter-share)    |An object hash representing the default language and attributes used when an activist shares on Twitter.
|email_share	|[Email Share](#email-share)    |An object hash representing the default language and attributes used when an activist shares via email.

_[Back to top...](#)_

### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Facebook Share

|Name          |Type      |Description
|-----------    |-----------|--------------
|facebook_share.title |string    |The title of the post created when an activist uses the share page to share content on Facebook.
|facebook_share.description |string    |The description of the post created when an activist uses the share page to share content on Facebook.
|facebook_share.image |string    |The URL of an image that goes with post created when an activist uses the share page to share content on Facebook.
|facebook_share.browser_url |string    |The URL of the content to be shared on Facebook, linked in the post created when an activist uses the share page to share on Facebook.

#### Twitter Share

|Name          |Type      |Description
|-----------    |-----------|--------------
|twitter_share.message |string    |The text of the post created when an activist uses the share page to share content on Twitter.


#### Email Share

|Name          |Type      |Description
|-----------    |-----------|--------------
|email_share.subject |string    |The subject line of the email created when an activist uses the share page to share content via email.
|email_share.body |string    |The body text of the email created when an activist uses the share page to share content via email.

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Share Page*](share_pages.html)	|A self-referential link to the share page.
|creator		|[Person*](people.html)  		|A link to a single Person resource representing the creator of the share page.
|modified_by	|[Person* ](people.html) 		|A link to a Person resource representing the last editor of this share page.

_[Back to top...](#)_


## Related Resources

* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Share Page resources (GET)

Share page resources are sometimes presented as collections of share pages. For example, calling the share pages endpoint will return a collection of all the share pages stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/share_pages/

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
            "href": "https://osdi-sample-system.org/api/v1/share_pages?page=2"
        },
        "osdi:share_pages": [
            {
                "href": "https://osdi-sample-system.org/api/v1/share_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/share_pages/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/share_pages"
        }
    },
    "_embedded": {
        "osdi:share_pages": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "2015 Petition Share Page",
                "title": "Thanks for signing! Now share to keep up our momentum.",
                "description": "<p>Thanks for singing the petition!</p><p>Now, can you share it with your friends?</p>",
                "summary": "Thanks for signing! Now share!",
                "browser_url": "http://osdi-sample-system.org/share_pages/thanks-for-signing",
                "total_shares": 345,
                "facebook_share": {
	                "title": "Sign the petition!",
	                "description": "Please sign our awesome petition.",
	                "image": "http://odsi-sample-system.org/images/petition-share-image.jpg",
	                "browser_url": "http://osdi-sample-system.org/petitions/my-petition/"
	            },
	            "twitter_share": {
		            "message": "Sign the petition from @OSDI to get rid of the bad things! Click here: http://osdi-sample-system.org/petitions/my-petition/"
		        },
		        "email_share": {
			        "subject": "Sign the petition!",
			        "body": "Can you sign the petition to get rid of the bad things? Click here: http://osdi-sample-system.org/petitions/my-petition/"
			    },
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/share_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
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
                "title": "Share this awesome video with everyone!",
                "description": "<p>Watch this video, then click the buttons to share.</p>",
                "total_shares": 43,
                "facebook_share": {
	                "title": "Watch this video!",
	                "description": "Please check out this crazy video.",
	                "image": "http://odsi-sample-system.org/images/video-share-image.jpg",
	                "browser_url": "http://osdi-sample-system.org/share/my-video/"
	            },
	            "twitter_share": {
		            "message": "Watch this crazy video! Click here: http://osdi-sample-system.org/petitions/my-petition/"
		        },
		        "email_share": {
			        "subject": "Watch this video!",
			        "body": "Check out this crazy video I just watched! Click here: http://osdi-sample-system.org/petitions/my-petition/"
			    },
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/share_pages/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Share Page resource (GET)

Calling an individual Share Page resource will return the resource directly, along with all associated fields and appropriate links to additional information about the share page.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/share_pages/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "name": "2015 Petition Share Page",
    "title": "Thanks for signing! Now share to keep up our momentum.",
    "description": "<p>Thanks for singing the petition!</p><p>Now, can you share it with your friends?</p>",
    "summary": "Thanks for signing! Now share!",
    "browser_url": "http://osdi-sample-system.org/share_pages/thanks-for-signing",
    "total_shares": 345,
    "facebook_share": {
        "title": "Sign the petition!",
        "description": "Please sign our awesome petition.",
        "image": "http://odsi-sample-system.org/images/petition-share-image.jpg",
        "browser_url": "http://osdi-sample-system.org/petitions/my-petition/"
    },
    "twitter_share": {
        "message": "Sign the petition from @OSDI to get rid of the bad things! Click here: http://osdi-sample-system.org/petitions/my-petition/"
    },
    "email_share": {
        "subject": "Sign the petition!",
        "body": "Can you sign the petition to get rid of the bad things? Click here: http://osdi-sample-system.org/petitions/my-petition/"
    },
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/share_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new share page (POST)

Posting to the share page collection endpoint will allow you to create a new share page. The response is the new share page that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/share_pages/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "name": "2015 Petition Share Page",
    "title": "Thanks for signing! Now share to keep up our momentum.",
    "origin_system": "OpenSupporter",
    "facebook_share": {
        "title": "Sign the petition!",
        "description": "Please sign our awesome petition.",
        "image": "http://odsi-sample-system.org/images/petition-share-image.jpg",
        "browser_url": "http://osdi-sample-system.org/petitions/my-petition/"
    },
    "twitter_share": {
        "message": "Sign the petition from @OSDI to get rid of the bad things! Click here: http://osdi-sample-system.org/petitions/my-petition/"
    },
    "email_share": {
        "subject": "Sign the petition!",
        "body": "Can you sign the petition to get rid of the bad things? Click here: http://osdi-sample-system.org/petitions/my-petition/"
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
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "2015 Petition Share Page",
    "title": "Thanks for signing! Now share to keep up our momentum.",
    "total_shares": 0,
    "browser_url": "http://osdi-sample-system.org/share_pages/thanks-for-signing",
    "facebook_share": {
        "title": "Sign the petition!",
        "description": "Please sign our awesome petition.",
        "image": "http://odsi-sample-system.org/images/petition-share-image.jpg",
        "browser_url": "http://osdi-sample-system.org/petitions/my-petition/"
    },
    "twitter_share": {
        "message": "Sign the petition from @OSDI to get rid of the bad things! Click here: http://osdi-sample-system.org/petitions/my-petition/"
    },
    "email_share": {
        "subject": "Sign the petition!",
        "body": "Can you sign the petition to get rid of the bad things? Click here: http://osdi-sample-system.org/petitions/my-petition/"
    },
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/share_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a share page (PUT)

You can update a share page by calling a PUT operation on that share page's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/share_pages/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "name": "2015 Petition Share Page (version 1)"
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
    "name": "2015 Petition Share Page (version 1)",
    "title": "Thanks for signing! Now share to keep up our momentum.",
    "total_shares": 0,
    "browser_url": "http://osdi-sample-system.org/share_pages/thanks-for-signing",
    "facebook_share": {
        "title": "Sign the petition!",
        "description": "Please sign our awesome petition.",
        "image": "http://odsi-sample-system.org/images/petition-share-image.jpg",
        "browser_url": "http://osdi-sample-system.org/petitions/my-petition/"
    },
    "twitter_share": {
        "message": "Sign the petition from @OSDI to get rid of the bad things! Click here: http://osdi-sample-system.org/petitions/my-petition/"
    },
    "email_share": {
        "subject": "Sign the petition!",
        "body": "Can you sign the petition to get rid of the bad things? Click here: http://osdi-sample-system.org/petitions/my-petition/"
    },
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/share_pages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a share page (DELETE)

You may delete a share page by calling the DELETE command on the share page's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/share_pages/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This share page was successfully deleted."
}
```

_[Back to top...](#)_