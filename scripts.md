---
layout: default
title: Scripts
---

# Script

This page defines the Script resource.

Scripts are collections of [Questions](questions.html), represented by the intermediate [Script Questions](script_questions.html) resource, asked to a person during a [Canvassing Effort](canvassing_efforts.html). 

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Script Fields](#script-fields) 
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Script resources (GET)](#scenario-retrieving-a-collection-of-script-resources-get)
    * [Scenario: Retrieving an individual Script resource (GET)](#scenario-retrieving-an-individual-script-resource-get)
    * [Scenario: Creating a new scipt (POST)](#scenario-creating-a-new-script-post)
    * [Scenario: Modifying a script (PUT)](#scenario-modifying-a-script-put)
    * [Scenario: Deleting a script (DELETE)](#scenario-deleting-a-script-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Script resource is ```osdi:script``` for a single Script resource or ```osdi:scripts``` for a collection of Script resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_

### Script Fields

| Name          | Type                | Description
| -----------   | -----------         | --------------
|origin_system      |string     |A human readable identifier of the system where this Script was created. (ex: "OSDI System")
|name               |string     |The name of the Script. Intended for administrative display rather than a public title, though may be shown to a user.
|title              |string     |The title of the Script. Intended for public display rather than administrative purposes.
|description        |string     |A description of the Script, usually displayed publicly. May contain text and/or HTML.
|summary            |string     |A text-only single paragraph summarizing the Script. Shown on listing pages that have more than titles, but not enough room for full description.

_[Back to top...](#)_

### Links

{% include links_intro.md %}

| Name          | Type       | Description
|-----------    |----------- |-----------
|self           |[Script*](scripts.html)    |A self-referential link to the Script.
|creator        |[Person*](people.html)         |A link to a single Person resource representing the creator of the Script.
|modified_by    |[Person* ](people.html)        |A link to a Person resource representing the last editor of this Script.
|script_questions  |[Script Questions[]*](script_questions.html)  |A link to the collection of Script Question resources for this Script.
|canvassing_effort  |[Canvassing Effort*](canvassing_efforts.html)  |A link to the collection of Script Question resources for this Script.

_[Back to top...](#)_


## Related Resources

* [Person](people.html)
* [Script Question](script_questions.html)
* [Canvassing Effort](canvassing_efforts.html)




_[Back to top...](#)_


## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Script resources (GET)

Script resources are sometimes presented as collections of scripts. For example, calling the scripts endpoint will return a collection of all the scripts stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/scripts/

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
            "href": "https://osdi-sample-system.org/api/v1/scripts?page=2"
        },
        "osdi:scripts": [
            {
                "href": "https://osdi-sample-system.org/api/v1/scipts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/scipts/a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
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
            "href": "https://osdi-sample-system.org/api/v1/scipts"
        }
    },
    "_embedded": {
        "osdi:scipts": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "Script 1",
                "title": "Persuasion Script",
                "description": "<p>Persuasion Script for Area A</p>",
                "summary": "Persuasion Script for Area A"
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/scripts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:script_questions" : {
                        "href": "https://osdi-sample-system.org/api/v1/script/c945d6fe-929e-11e3-a2e9/script_questions"
                    },
                    "osdi:canvassing_effort" : {
                        "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts/c945d6fe-929e-11e3-a2e9"
                    }
                }
            },
            {
                {
                    "identifiers": [
                        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa",
                        "foreign_system:1"
                    ],
                    "origin_system": "OSDI Sample System",
                    "created_date": "2014-03-20T21:04:31Z",
                    "modified_date": "2014-03-20T21:04:31Z",
                    "name": "Script 1",
                    "title": "Persuasion Script",
                    "description": "<p>Persuasion Script for Area A</p>",
                    "summary": "Persuasion Script for Area A",
                    "_links": {
                        "self": {
                            "href": "https://osdi-sample-system.org/api/v1/scripts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
                        },
                        "osdi:creator": {
                            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                        },
                        "osdi:modified_by": {
                            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                        },
                        "osdi:script_questions" : {
                            "href": "https://osdi-sample-system.org/api/v1/script/c945d6fe-929e-11e3-a2e9/script_questions"
                        },
                        "osdi:canvassing_effort" : {
                            "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts/c945d6fe-929e-11e3-a2e9"
                        }
                    }
                }
            },
            //truncated for brevity
        ]
    }
}
``` 

_[Back to top...](#)_       

### Scenario: Retrieving an individual Script resource (GET)

Calling an individual Script resource will return the resource directly, along with all associated fields, embedded Questions and appropriate links to additional information about the script.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/scripts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa

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
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "Script 1",
    "title": "Persuasion Script",
    "description": "<p>Persuasion Script for Area A</p>",
    "summary": "Persuasion Script for Area A",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/scripts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:script_questions" : {
            "href": "https://osdi-sample-system.org/api/v1/scripts/c945d6fe-929e-11e3-a2e9/script_questions"
        },
        "osdi:canvassing_effort" : {
            "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts/c945d6fe-929e-11e3-a2e9"
        }   
    }
}
```


_[Back to top...](#)_


### Scenario: Creating a new script (POST)

Posting to the script collection endpoint will allow you to create a new script. The response is the new script that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/scripts/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "name": "Script 1",
    "title": "Persuasion Script",
    "description": "<p>Persuasion Script for Area A</p>",
    "summary": "Persuasion Script for Area A",
}

```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate
{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "Script 1",
    "title": "Persuasion Script",
    "description": "<p>Persuasion Script for Area A</p>",
    "summary": "Persuasion Script for Area A",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/scripts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:script_questions": {
            "href": "https://osdi-sample-system.org/api/v1/scripts/c945d6fe-929e-11e3-a2e9/script_questions"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a script (PUT)

You can update a script by calling a PUT operation on that script's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/scipts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa

Header:
OSDI-API-Token:[your api key here]

{
    "name": "Script 1",
    "title": "Persuasion Script"
}

```

#### Response
```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate
{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "Script 1",
    "title": "Persuasion Script",
    "description": "<p>Persuasion Script for Area A</p>",
    "summary": "Persuasion Script for Area A",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/scripts/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:script_questions": {
            "href": "https://osdi-sample-system.org/api/v1/scripts/c945d6fe-929e-11e3-a2e9/script_questions"
        },
        "osdi:canvassing_effort" : {
            "href": "https://osdi-sample-system.org/api/v1/canvassing_efforts/c945d6fe-929e-11e3-a2e9"
        }
    }
}
```


_[Back to top...](#)_


### Scenario: Deleting a script (DELETE)

You may delete a script by calling the DELETE command on the script's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/scripts/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This script was successfully deleted."
}
```

_[Back to top...](#)_