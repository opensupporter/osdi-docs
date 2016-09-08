---
layout: default
title: Submission
---

# Submission

This document defines the Submission resource. 

Submissions are a type of action that a user may take by completing a form. Submissions have fields to describe them such as when the submission was created and typically are linked to the person who made the submission as well as any information they submitted in the form of [Question](#) and [Question Answer](#) resources.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Submission Fields](#submission-fields)  
    * [Links](#links)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Submission resources (GET)](#scenario-retrieving-a-collection-of-submission-resources-get)
    * [Scenario: Retrieving an individual Submission resource (GET)](#scenario-scenario-retrieving-an-individual-submission-resource-get)
    * [Scenario: Creating a new submission (POST)](#scenario-creating-a-new-submission-post)
    * [Scenario: Modifying a submission (PUT)](#scenario-modifying-a-submission-put)
    * [Scenario: Deleting a submission (DELETE)](#scenario-deleting-a-submission-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Submission resource is ```osdi:submission``` for a single Submission resource or ```osdi:submissions``` for a collection of Submission resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Submission Fields

A list of fields specific to the Submission resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this submission was created. (ex: "OSDI System")
|action_date		|string		|The date and time the submission was made by the person.

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Submission*](submissions.html)	|A self-referential link to the submission.
|person			|[Person*](people.html)		|A link to a single Person resource representing the person who submitted the information.
|form			|[Form*](forms.html)  		|A link to a Form resource representing the form on which this submission was created.
|answers	|[Answers[]*](answers.html)	|A link to the collection of Answer resources representing data submitted by the person when this submission was made.

_[Back to top...](#)_


## Related Resources

* [Record Submission Helper](record_submission.html)
* [Form](forms.html)
* [Person](people.html)
* [Answer](answers.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Submission resources (GET)

Submission resources are sometimes presented as collections of submissions. For example, calling the submissions endpoint on a particular form will return a collection of all the submissions made to that form.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions

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
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions?page=2"
        },
        "osdi:submissions": [
            {
                "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions"
        }
    },
    "_embedded": {
        "osdi:submissions": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "action_date": "2014-03-18T11:02:15Z",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:form": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
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
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:form": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/adb951cb-51f9-420e-b7e6-de953195ec86"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/1efc3644-af25-4253-90b8-a0baf12dbd1e/answers"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Submission resource (GET)

Calling an individual Submission resource will return the resource directly, along with all associated fields and appropriate links to additional information about the submission.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

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
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:form": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Creating a new submission (POST)

Posting to the submissions collection endpoint and including a link to an existing Person resource will allow you to create a new submission associated with that form and person. The response is the new submission that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

For information on how to link a submission with a question answer, see the [Question Answers](#) documentation. For information on how to create a person along with a submission, see the [Record Submission Helper](record_submission.html) documentation.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "action_date": "2014-03-18T11:02:15Z",
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
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:form": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/answers"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a submission (PUT)

You can update a submission by calling a PUT operation on that submission's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/

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
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:form": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/answers"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a submission (DELETE)

You may delete a submission by calling the DELETE command on the submission's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/forms/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This submission was successfully deleted."
}
```

_[Back to top...](#)_