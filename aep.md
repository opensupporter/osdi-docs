---
layout: default
title: API Entry Point
---

# API Entry Point

This document defines the API Entry Point (AEP) resource. 

The AEP is the top level entry point for an OSDI API implementation. It provides links to other resource entry points, such as a collection of [Petition](petitions.html) resources in the system, documentation, and sometimes contains messages. By starting at the AEP and following successive links, a user should be able to reach all URLs available on the API.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [AEP Fields](#aep-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving the API Entry Point resource (GET)](#scenario-retrieving-the-api-entry-point-resource-get)


{% include endpoints_and_url_structures.md %}

_[Back to top...](#)_


## Fields


### AEP Fields

A list of fields specific to the AEP resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|motd		|string     |The system "message of the day" -- an informational message from the server.
|max_pagesize				|integer		|The maximum number of records a server can return in a single query. 
|vendor_name    | string    | A string representing the vendor name
|product_name   | string    | A string identifying the product name
|osdi_version	| string	| A string identifying the OSDI Version
|namespace      | string    | A string representing the prefix used for curies, identifiers, and other applicable places.

_[Back to top...](#)_

### Links

{% include links_intro.md %}

Note that on the AEP, links will often contain titles to inform new users about what each link leads to. 

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[AEP*](aep.html)	|A self-referential link to the API Entry Point.
|people		|[People[]*](people.html)  		|A link to the collection of People resources in the system.
|petitions		|[Petitions[]*](petitions.html)  		|A link to the collection of Petition resources in the system.
|events		|[Events[]*](events.html)  		|A link to the collection of Event resources in the system.
|forms		|[Forms[]*](forms.html)  		|A link to the collection of Form resources in the system.
|fundraising_pages		|[Fundraising Pages[]*](fundraising_pages.html)  		|A link to the collection of Fundraising Page resources in the system.
|donations		|[Donations[]*](donations.html)  		|A link to the collection of Donation resources in the system.
|tags		|[Tags[]*](tags.html)  		|A link to the collection of Tag resources in the system.
|lists		|[Lists[]*](lists.html)  		|A link to the collection of list resources in the system.
|queries		|[Queries[]*](queries.html)  		|A link to the collection of Query resources in the system.
|questions		|[Questions[]*](questions.html)  		|A link to the collection of Question resources in the system.
|metadata		|[Metadta[]*](metadata.html)  			|A link to the Metadata endpoint in the system.
|share_pages		|[Share Pages[]*](share_pages.html)  		|A link to the collection of Share Page resources in the system.
|docs		|N/A  		|A link to the human-readable documentation for the API system.
|person_signup_helper		|[Person Signup Helper*](person_signup.html)  		|A link to the Person Signup Helper resource.

_[Back to top...](#)_


## Related Resources

* [Person](people.html)
* [Petition](petitions.html)
* [Event](events.html)
* [Form](forms.html)
* [Fundraising Page](fundraising_pages.html)
* [Donation](donations.html)
* [Tag](tags.html)
* [List](lists.html)
* [Query](queries.html)
* [Question](questions.html)
* [Metadata](metadata.html)
* [Share Page](share_pages.html)
* [Person Signup Helper](person_signup.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving the API Entry Point resource (GET)

Calling the AEP URL will return the API Entry Point resource with links to the rest of the API system.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "motd": "Welcome to the OSDI API Entry Point!",
    "vendor_name" : "Foobar Incorporated",
    "product_name" : "Curly Braces OSDI Server",
	"osdi_version" : "1.0",
    "max_pagesize": 25,
    "namespace": "osdi_sample_system",
    "_links": {
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-sample-system.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/",
            "title": "This API entry point"
        },
        "osdi:people": {
            "href": "https://osdi-sample-system.org/api/v1/people",
            "title": "The collection of people in the system"
        },
        "osdi:petitions": {
            "href": "https://osdi-sample-system.org/api/v1/petitions",
            "title": "The collection of petitions in the system"
        },
        "osdi:events": {
            "href": "https://osdi-sample-system.org/api/v1/events",
            "title": "The collection of events in the system"
        },
        "osdi:forms": {
            "href": "https://osdi-sample-system.org/api/v1/forms",
            "title": "The collection of forms in the system"
        },
        "osdi:fundraising_pages": {
            "href": "https://osdi-sample-system.org/api/v1/fundraising_pages",
            "title": "The collection of fundraising_pages in the system"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/donations",
            "title": "The collection of donations in the system"
        },
        "osdi:tags": {
            "href": "https://osdi-sample-system.org/api/v1/tags",
            "title": "The collection of tags in the system"
        },
        "osdi:lists": {
            "href": "https://osdi-sample-system.org/api/v1/lists",
            "title": "The collection of lists in the system"
        },
        "osdi:queries": {
            "href": "https://osdi-sample-system.org/api/v1/queries",
            "title": "The collection of queries in the system"
        },
        "osdi:questions": {
            "href": "https://osdi-sample-system.org/api/v1/questions",
            "title": "The collection of questions in the system"
        },
        "osdi:metadata": {
            "href": "https://osdi-sample-system.org/api/v1/metadata",
            "title": "The collection of metadata resources in the system"
        },	
        "osdi:share_pages": {
            "href": "https://osdi-sample-system.org/api/v1/share_pages",
            "title": "The collection of share pages in the system"
        },
        "docs": {
            "href": "https://osdi-sample-system.org/docs/v1/",
            "title": "Documentation",
            "name": "Docs",
            "index": "index"
        },
        "osdi:person_signup_helper": {
            "href": "https://osdi-sample-system.org/api/v1/people/person_signup",
            "title": "The person signup helper for the system"
        }
    }
}

```	

_[Back to top...](#)_
