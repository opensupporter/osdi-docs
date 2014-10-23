---
layout: default
title: Form
---

# Form

This page defines the Form and Submission resources.

Forms are flexible actions for collecting user data. They can be as simple as a signup form collecting an email address on a website to complex surveys that collect lots of questions and answers from users. Forms take submissions, which represent the individual data each time the form was submitted by a user.

Forms make use of but don't encapsulate OSDI [Questions and Answers](questions.html).


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Field names and descriptions](#field-names-and-descriptions)
* [Links](#links)
* [Scenario: Retrieving a collection of form resources (GET)](#scenario-retrieving-a-collection-of-form-resources-get)
* [Scenario: Retrieving an individual form resource (GET)](#scenario-scenario-retrieving-an-individual-form-resource-get)
* [Scenario: Retrieving a collection of form submission resources (GET)](#scenario-retrieving-a-collection-of-form-submission-resources-get)
* [Scenario: Retrieving an individual form submission resource (GET)](#scenario-scenario-retrieving-an-individual-form-submission-resource-get)
* [Scenario: Creating a new form (POST)](#scenario-creating-a-new-form-post)
* [Scenario: Modifying a form (PUT)](#scenario-modifying-a-form-put)
* [Scenario: Deleting a form (DELETE)](#scenario-deleting-a-form-delete)


## Endpoints and URL structures

While OSDI does not specify specific endpoints and link structures for compliant systems to use, commonly used conventions are shown below. The links section of each resource or collection, described more fully below, should be your canonical source for the exact URLs pointing to specific other resources or collections.

**Endpoints:**

`https://osdi-sample-system.org/api/v1/forms`

Form resources live exclusively at the above endpoint. The endpoint returns a collection of all the forms in the OSDI system's database associated with the given API key.

**URL Structures:**

`https://osdi-sample-system.org/api/v1/forms/[id]`

To address a specific form, use their identifier without the system prefix to construct a URL, like `https://osdi-sample-system.org/api/v1/form/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3`

Forms have submissions, and so thos submissions can be retreived like so:
`https://osdi-sample-system.org/api/v1/form/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions`

A specific submissions is as follows:
`https://osdi-sample-system.org/api/v1/form/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions/7fj23fds-3sf1-fds3-asj9-832mkdsoie81`

_[Back to top...](#form)_


## Field names and descriptions

The field names for a form and submission, with standard names, punctuation and capitalization, and values where appropriate. 

**Note:** As with the entire OSDI specification, the specific fields a compliant system implements will vary between each system, as will the fields each system requires when creating or updating resources, which fields are writeable, and the operations you are allowed to perform on each resource.


### Forms

| Name		| Type		| Description
|-----------|-----------|------------------
| identifiers	| Identifier[]	| An array of identifiers the provider has determined to be associated with the form
| created_date	| datetime	| Date and Time of creation
| modified_date	| datetime	| Date and Time of last modification
| origin_system | string | Human readable identifier of the system where this form was created
| name	| string	| name of the form
| title	| string	| title of the form
| summary	| string	| summary of the form
| description	| string/html string	| description of the form, optionally an HTML string
| call_to_action	| string	| Text of the call to action of the form (ex: Fill out our survey)
| browser_url	| string	| A URL string pointing to the publicly available form page on the web
| total_submissions	| integer	| Read-only computed property representing the current count of submissions on the form
| creator	| Person*	| A single embedded instance of a person representing the creator of the form
| submissions	| Submissions[]* | A Collection of Submission resources


### Submissions

| Name		| Type		| Description
|-----------|-----------|------------------
| identifiers	| Identifier[]	| An array of identifiers the provider has determined to be associated with the form
| created_date	| datetime	| Date and Time of creation
| modified_date	| datetime	| Date and Time of last modification
| action_date | datetime  | Date and Time the submission was made by the person
| person	| Person*	| An embedded person that made the submission on the referenced form
| form	| Form*	| A reference to the form this submission is related to
| question_answers	| Question_Answers[]* | A Collection of Question Answer resources related to this submission

_[Back to top...](#form)_


## Links

The links associated with this person, available in the links section of the resource. 

**Note:** As with the entire OSDI specification, the specific links a compliant system supplies will vary between each system. In addition, systems may choose to embed a linked resource directly in the response in addition to linking to it in the links section, using the standard `_embedded` syntax described in the general overview documentation.

|Name          |Description
|-----------    |--------------
|submissions      |A link to the collection of form submissions associated with the form.
|question         |A link to the collection of questions associated with the form.

_[Back to top...](#form)_


## Scenario: Retreiving a collection of form resources (GET)

## Default embed policy

When retreiving a form resource, the creator can be embededed, but the submissions collection should only be linked.

When retreiving a submission or list of submissions, the person, the form related to the submission, and the related question answers can be embedded.

## A list of forms

**Request**

```javascript
GET https://osdi-sample-system.org/api/v1/forms/

Header:
OSDI-API-Token:[your api key here]
```

**Response**

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "total_pages": 6,
  "per_page": 25,
  "page": 1,
  "total_records": 139,
  "_links": {
    "next": {
      "href": "https://api.opensupporter.org/api/v1/forms?page=2"
    },
    "self": {
      "href": "https://api.opensupporter.org/api/v1/forms"
    },
    "osdi:forms": [
      {
        "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
      },
      {
        "href": "https://api.opensupporter.org/api/v1/forms/7580ac3e-9a72-11e3-a2e9-12313d316c29"
      },
      ...
    ],
    "curies": [
      {
        "name": "osdi",
        "href": "http://api.opensupporter.org/docs/v1/{rel}",
        "templated": true
      }
    ]
  },
  "_embedded": {
    "osdi:forms": [
      {
        "identifier": [
          "osdi_provider:9b385f65-23b3-47a4-a4b5-9abd537b37a7"
        ],
        "created_date": "2014-02-20T21:30:55Z",
        "modified_date": "2014-02-21T15:36:34Z",
        "origin_system": "OpenSupporter",
        "summary": "Take our year-end activist survey",
        "description": "<p>Please take this survey to tell us stuff about you.</p>",
        "call_to_action": "Take our survey",
        "browser_url": "https://api.opensupporter.org/forms/take-our-year-end-activist-survey",
        "total_submissions": 100,
        "_embedded": {
          "osdi:creator": {
            "given_name": "Jane",
            "family_name": "Doe",
            "identifiers": [
              "osdi_provider:c945d6fe-929e-11e3-a2e9-12313d316c29"
            ],
            "email_addresses": [
              {
                "primary": true,
                "address": "jane.doe@gmail.com"
              }
            ],
            "postal_addresses": [
              {
                "primary": true,
                "address_lines": [
                  "123 Something Rd."
                ],
                "locality": "Washington",
                "region": "DC",
                "postal_code": "20009",
                "country": "US",
                "language": "en",
                "location": {
                  "latitude": 38.919,
                  "longitude": -72.6375,
                  "accuracy": "Approximate"
                }
              }
            ],
            "_links": {
              "self": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
              },
              "osdi:submissions": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions"
              },
              ...
            }
          }
        },
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
          },
          "osdi:submissions": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions"
          },
          "osdi:creator": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
          }
        }
      },
      {
        "identifier": [
          "osdi_provider:7580ac3e-9a72-11e3-a2e9-12313d316c29"
        ],
        "created_date": "2014-02-14T15:35:59Z",
        "modified_date": "2014-02-14T15:39:12Z",
        "origin_system": "OpenSupporter",
        "summary": "Sign up for our email list",
        "description": "<p>Get the latest updates from us by adding your email here!</p>",
        "call_to_action": "Sign up",
        "browser_url": "https://api.opensupporter.org/forms/sign-up-for-our-email-list",
        "total_submissions": 4829,
        "_embedded": {
          "osdi:creator": {
            "given_name": "Tom",
            "family_name": "Jones",
            "identifiers": [
              "osdi_provider:c945d6fe-929e-11e3-a2e9-12313d316c29"
            ],
            "email_addresses": [
              {
                "primary": true,
                "address": "tom.jones@gmail.com"
              }
            ],
            "postal_addresses": [
              {
                "primary": true,
                "locality": "New York City",
                "region": "NY",
                "postal_code": "10001",
                "country": "US",
                "language": "en",
                "location": {
                  "latitude": 33.123,
                  "longitude": -76.5432,
                  "accuracy": "Approximate"
                }
              }
            ],
            "_links": {
              "self": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
              },
              "osdi:submissions": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions"
              },
              ...
            }
          }
        },
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/forms/7580ac3e-9a72-11e3-a2e9-12313d316c29"
          },
          "osdi:submissions": {
            "href": "https://api.opensupporter.org/api/v1/forms/7580ac3e-9a72-11e3-a2e9-12313d316c29/submissions"
          },
          "osdi:creator": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
          }
        }
      },
      ...
    ]
  }
}
```

_[Back to top...](#form)_


## Scenario: Retrieving an individual form resource (GET)

***Request***

```javascript
GET /api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/

Header:
OSDI-API-Token:[your api key here]
```

***Response***
```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
	"identifier": [
      "osdi_provider:9b385f65-23b3-47a4-a4b5-9abd537b37a7"
    ],
    "created_date": "2014-02-20T21:30:55Z",
    "modified_date": "2014-02-21T15:36:34Z",
    "origin_system": "OpenSupporter",
    "summary": "Take our year-end activist survey",
    "description": "<p>Please take this survey to tell us stuff about you.</p>",
	  "call_to_action": "Take our survey",
    "browser_url": "https://api.opensupporter.org/forms/take-our-year-end-activist-survey",
    "total_submissions": 100,
    "_embedded": {
      "osdi:creator": {
        "given_name": "Jane",
        "family_name": "Doe",
        "identifiers": [
          "osdi_provider:c945d6fe-929e-11e3-a2e9-12313d316c29"
        ],
        "email_addresses": [
          {
            "primary": true,
            "address": "jane.doe@gmail.com"
          }
        ],
        "postal_addresses": [
          {
            "primary": true,
            "address_lines": [
              "123 Something Rd."
            ],
            "locality": "Washington",
            "region": "DC",
            "postal_code": "20009",
            "country": "US",
            "language": "en",
            "location": {
              "latitude": 38.919,
              "longitude": -72.6375,
              "accuracy": "Approximate"
            }
          }
        ],
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
          },
          "osdi:submissions": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/submissions"
          },
          ...
        }
      }
    },
    "_links": {
      "self": {
        "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
      },
      "osdi:submissions": {
        "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions"
      },
      "osdi:creator": {
        "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
      }
    }
}
```

_[Back to top...](#form)_


## Scenario: Retrieving a collection of form submission resources (GET)

***Request***

```javascript
GET /api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions

Header:
OSDI-API-Token:[your api key here]
```

***Response***
```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "total_pages": 4,
  "per_page": 25,
  "page": 1,
  "total_records": 100,
  "_links": {
    "self": {
      "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions"
    },
    "next": {
      "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions/?page=2"
    },
    "osdi:submissions": [
      {
        "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions/25d2d08f-7c3a-4bdc-8329-815aa5117d54"
      },
      {
        "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions/13d2d08f-6c3a-3bec-8628-515aa5147e57"
      },
      ...
    ],
    "curies": [
      {
        "name": "osdi",
        "href": "http://api.opensupporter.org/docs/v1/{rel}",
        "templated": true
      }
    ]
  },
  "_embedded": {
    "osdi:submissions": [
      {
        "identifier": [
          "osdi_provider:25d2d08f-7c3a-4bdc-8329-815aa5117d54"
        ],
        "created_date": "2014-02-20T21:32:56Z",
        "modified_date": "2014-02-20T21:32:56Z",
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions/25d2d08f-7c3a-4bdc-8329-815aa5117d54"
          },
          "osdi:form": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
          },
          "osdi:person": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
          },
          "osdi:question_answers": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions/25d2d08f-7c3a-4bdc-8329-815aa5117d54/question_answers"
          }
        }
      },
      {
        "identifier": [
          "osdi_provider:13d2d08f-6c3a-3bec-8628-515aa5147e57"
        ],
        "created_date": "2014-02-20T21:32:56Z",
        "modified_date": "2014-02-20T21:32:56Z",
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions/13d2d08f-6c3a-3bec-8628-515aa5147e57"
          },
          "osdi:form": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
          },
          "osdi:person": {
            "href": "https://api.opensupporter.org/api/v1/people/35ad5d6ed-913e-12e6-a2e8-11673r314c14"
          },
          "osdi:question_answers": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions/13d2d08f-6c3a-3bec-8628-515aa5147e57/question_answers"
          }
        }
      },
      ...
    ]
  }
}
```

_[Back to top...](#form)_


## Scenario: Retrieving an individual form submission resource (GET)

***Request***

```javascript
GET /api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions/25d2d08f-7c3a-4bdc-8329-815aa5117d54

Header:
OSDI-API-Token:[your api key here]
```

***Response***

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
	"identifier": [
	  "osdi_provider:25d2d08f-7c3a-4bdc-8329-815aa5117d54"
	],
	"created_date": "2014-02-20T21:32:56Z",
	"modified_date": "2014-02-20T21:32:56Z",
	"_links": {
	  "self": {
	    "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions/25d2d08f-7c3a-4bdc-8329-815aa5117d54"
	  },
	  "osdi:form": {
	    "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
	  },
	  "osdi:person": {
	    "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
	  },
	  "osdi:question_answers": {
      	"href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/submissions/25d2d08f-7c3a-4bdc-8329-815aa5117d54/question_answers"
      }
	}
}
```

_[Back to top...](#form)_


## Scenario: Creating a new form (POST)

Posting to the forms collection endpoint will allow you to create a new form. The response is the new form that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

**Request**

```javascript
POST https://osdi-sample-system.org/api/v1/people/

Header:
OSDI-API-Token:[your api key here]

{
  "identifiers": [
      "foreign_system:1"
  ],
  "summary": "Take our year-end activist survey",
  "description": "<p>Please take this survey to tell us stuff about you.</p>",
  "call_to_action": "Take our survey",
  "browser_url": "https://api.opensupporter.org/forms/take-our-year-end-activist-survey"  
}
```

**Response**

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
  "summary": "Take our year-end activist survey",
  "description": "<p>Please take this survey to tell us stuff about you.</p>",
  "call_to_action": "Take our survey",
  "browser_url": "https://api.opensupporter.org/forms/take-our-year-end-activist-survey",
  "_links": {
    "self": {
      "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
    },
    "osdi:submissions": {
      "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/submissions"
    },
  }
}
```

_[Back to top...](#form)_


## Scenario: Modifying a form (PUT)

You can updating a form by calling a PUT operation on that form's resource endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

**Note:** Modifying members of an array separately is not supported. To change the contents of an array, first GET the current contents and then PUT back only those you wish to keep.

**Request**

```javascript
PUT https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "summary": "Take our new year-end activist and supporter survey"
}

```

**Response**

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
  "summary": "Take our new year-end activist and supporter survey",
  "description": "<p>Please take this survey to tell us stuff about you.</p>",
  "call_to_action": "Take our survey",
  "browser_url": "https://api.opensupporter.org/forms/take-our-year-end-activist-survey",
  "_links": {
    "self": {
      "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
    },
    "osdi:submissions": {
      "href": "https://osdi-sample-system.org/api/v1/forms/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/submissions"
    },
  }
}
```

_[Back to top...](#form)_


## Scenario: Deleting a form (DELETE)

You may delete a form by calling the DELETE command on the form resource's endpoint.

**Request**

```javascript
DELETE https://osdi-sample-system.org/api/v1/forms/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

**Response**

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "notice": "This form was successfully deleted."
}
```

_[Back to top...](#form)_
