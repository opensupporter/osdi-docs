---
layout: default
title: Form
---

# Form

This document defines the Form resource. 

Forms represent a page, survey, or interaction that a user may participate in by submitting their information. Forms have fields to describe them such as names, titles, summaries, and descriptions, and when activists submit a form, [Submission](submissions.html) resources are created representing the individual submission an activist made on that form.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Form Fields](#form-fields)  
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Form resources (GET)](#scenario-retrieving-a-collection-of-form-resources-get)
    * [Scenario: Retrieving an individual Form resource (GET)](#scenario-scenario-retrieving-an-individual-form-resource-get)
    * [Scenario: Creating a new form (POST)](#scenario-creating-a-new-form-post)
    * [Scenario: Modifying a form (PUT)](#scenario-modifying-a-form-put)
    * [Scenario: Deleting a form (DELETE)](#scenario-deleting-a-form-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Form resource is ```osdi:form``` for a single Form resource or ```osdi:forms``` for a collection of Form resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Form Fields

A list of fields specific to the Form resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this form was created. (ex: "OSDI System")
|name				|string		|The name of the form. Intended for administrative display rather than a public title, though may be shown to a user.
|title				|string		|The title of the form. Intended for public display rather than administrative purposes.
|description		|string		|A description of the form, usually displayed publicly. May contain text and/or HTML.
|summary			|string		|A text-only single paragraph summarizing the form. Shown on listing pages that have more than titles, but not enough room for full description.
|call_to_action		|string		|The text of the call to action of the form. (ex: "Fill out our survey")
|browser_url		|string		|A URL string pointing to the publicly available form page on the web.
|total_submissions	|integer	|A read-only computed property representing the current count of the total number of submissions on the form.

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Form*](forms.html)	|A self-referential link to the form.
|creator		|[Person*](people.html)  		|A link to a single Person resource representing the creator of the form.
|modified_by	|[Person* ](people.html) 		|A link to a Person resource representing the last editor of this form.
|submissions	|[Submissions[]*](submissions.html)	|A link to the collection of Submission resources for this form.
|record_submission_helper	|[Record Submissions Helper*](record_submission.html)	|A link to the Record Submissions Helper resource endpoint for this form.

_[Back to top...](#)_


## Related Resources

* [Submission](submissions.html)
* [Record Submission Helper](record_submission.html)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Form resources (GET)

Form resources are sometimes presented as collections of forms. For example, calling the forms endpoint will return a collection of all the forms stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/forms/

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
            "href": "https://osdi-sample-system.org/api/v1/forms?page=2"
        },
        "osdi:forms": [
            {
                "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/forms/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/forms"
        }
    },
    "_embedded": {
        "osdi:forms": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "My Form",
                "title": "Tell Us About Yourself",
                "description": "<p>Please take a moment to tell us about yourself so we can learn more about you.</p>",
                "summary": "Please take a moment to tell us about yourself.",
                "call_to_action": "Tell us about yourself here",
                "browser_url": "http://osdi-sample-system.org/forms/tell-us-about-yourself",
                "total_submissions": 30,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:submissions": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:record_submission_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_submission_helper"
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
                "title": "Tell Your Story",
                "description": "<p>Tell us your story today!</p>",
                "browser_url": "http://osdi-sample-system.org/forms/tell-your-story",
                "total_submissions": 10,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:submissions": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/1efc3644-af25-4253-90b8-a0baf12dbd1e/submissions"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:record_submission_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/1efc3644-af25-4253-90b8-a0baf12dbd1e/record_submission_helper"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Form resource (GET)

Calling an individual Form resource will return the resource directly, along with all associated fields and appropriate links to additional information about the form.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/forms/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "name": "My Form",
    "title": "Tell Us About Yourself",
    "description": "<p>Please take a moment to tell us about yourself so we can learn more about you.</p>",
    "summary": "Please take a moment to tell us about yourself.",
    "call_to_action": "Tell us about yourself here",
    "browser_url": "http://osdi-sample-system.org/forms/tell-us-about-yourself",
    "total_submissions": 30,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:record_submission_helper": {
            "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_submission_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new form (POST)

Posting to the form collection endpoint will allow you to create a new form. The response is the new form that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/forms/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "title": "Take Our Survey",
    "name": "2014 User Survey",
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
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
        "foreign_system:1"
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "title": "Take Our Survey",
    "name": "2014 User Survey",
    "origin_system": "OpenSupporter",
    "total_submissions": 0,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:record_submission_helper": {
            "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_submission_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a form (PUT)

You can updating a form by calling a PUT operation on that form's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "name": "2014 New User Survey",
    "description": "<p>Take our survey!</p>"
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
    "title": "Take Our Survey",
    "name": "2014 New User Survey",
    "description": "<p>Take our survey!</p>",
    "origin_system": "OpenSupporter",
    "total_submissions": 0,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:record_submission_helper": {
            "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_submission_helper"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a form (DELETE)

You may delete a form by calling the DELETE command on the form's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/forms/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This form was successfully deleted."
}
```

_[Back to top...](#)_