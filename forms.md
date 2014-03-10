# Forms

This page defines Forms, Form Signups.

Forms are flexible actions for collecting user data. They can be as simple as a signup form collecting an email address on a website to complex surveys that collect lots of questions and answers from users.

Forms make use of but don't encapsulate OSDI [Questions and Answers](questions.md).

## Forms

| Name		| Type		| Description
|-----------|-----------|------------------
| identifiers	| Identifier[]	| A collection of identifiers the provider has determined to be associated with the petition
| created_at	| datetime	| Date and Time of creation
| modified_at	| datetime	| Date and Time of last modification
| summary	| string	| title / summary of petition
| description	| string/html string	| description of the petition, optionally an HTML string
| call_to_action	| string	| Text of the call to action of the form (ex: Fill out our survey)
| url	| string	| A URL string pointing to the publicly available petition page on the web
| total_signups	| integer	| Read-only computed property representing the current count of signups on the form
| creator	| Person*	| A single embedded instance of a person representing the creator of the petition
| signups	| Signups[]| A Collection of Signup resources

## Signups

| Name		| Type		| Description
|-----------|-----------|------------------
| identifiers	| Identifier[]	| A collection of identifiers the provider has determined to be associated with the petition
| created_at	| datetime	| Date and Time of creation
| modified_at	| datetime	| Date and Time of last modification
| person	| Person*	| An embedded person that made the signup on the referenced form
| form	| Form*	| An embedded  reference to the form this signup is related to
| question_answers	| Question_Answers[]	| A Collection of Question Answer resources related to this signup


# Retrieving Resources (GET)

## Default embed policy

When retreiving a form resource, the creator can be embededed, but the signups collection should only be linked.

When retreiving a signup or list of signups, the person, the form related to the signup, and the related question answers can be embedded.

## A list of forms

Only two shown for brevity.

```
GET /api/v1/forms/
200 OK
```

```javascript
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
        "created_at": "2014-02-20T21:30:55Z",
        "modified_at": "2014-02-21T15:36:34Z",
        "summary": "Take our year-end activist survey",
        "description": "<p>Please take this survey to tell us stuff about you.</p>",
        "call_to_action": "Take our survey",
        "url": "https://api.opensupporter.org/forms/take-our-year-end-activist-survey",
        "total_signups": 100,
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
              "osdi:signups": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/signups"
              },
              ...
            }
          }
        },
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
          },
          "osdi:signups": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups"
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
        "created_at": "2014-02-14T15:35:59Z",
        "modified_at": "2014-02-14T15:39:12Z",
        "summary": "Sign up for our email list",
        "description": "<p>Get the latest updates from us by adding your email here!</p>",
        "call_to_action": "Sign up",
        "url": "https://api.opensupporter.org/forms/sign-up-for-our-email-list",
        "total_signups": 4829,
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
              "osdi:signups": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/signups"
              },
              ...
            }
          }
        },
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/forms/7580ac3e-9a72-11e3-a2e9-12313d316c29"
          },
          "osdi:signups": {
            "href": "https://api.opensupporter.org/api/v1/forms/7580ac3e-9a72-11e3-a2e9-12313d316c29/signups"
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


## A single form
```
GET /api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/
200 OK
```

```javascript
{
	"identifier": [
      "osdi_provider:9b385f65-23b3-47a4-a4b5-9abd537b37a7"
    ],
    "created_at": "2014-02-20T21:30:55Z",
    "modified_at": "2014-02-21T15:36:34Z",
    "summary": "Take our year-end activist survey",
    "description": "<p>Please take this survey to tell us stuff about you.</p>",
	"call_to_action": "Take our survey",
    "url": "https://api.opensupporter.org/forms/take-our-year-end-activist-survey",
    "total_signups": 100,
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
          "osdi:signups": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/signups"
          },
          ...
        }
      }
    },
    "_links": {
      "self": {
        "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
      },
      "osdi:signups": {
        "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups"
      },
      "osdi:creator": {
        "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
      }
    }
}
```

## A list of signups on a form

Only two shown for brevity.

```
GET /api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups
200 OK
```

```javascript
{
  "total_pages": 4,
  "per_page": 25,
  "page": 1,
  "total_records": 100,
  "_links": {
    "self": {
      "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups"
    },
    "next": {
      "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups/?page=2"
    },
    "osdi:signups": [
      {
        "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups/25d2d08f-7c3a-4bdc-8329-815aa5117d54"
      },
      {
        "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups/13d2d08f-6c3a-3bec-8628-515aa5147e57"
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
    "osdi:signups": [
      {
        "identifier": [
          "osdi_provider:25d2d08f-7c3a-4bdc-8329-815aa5117d54"
        ],
        "created_at": "2014-02-20T21:32:56Z",
        "modified_at": "2014-02-20T21:32:56Z",
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups/25d2d08f-7c3a-4bdc-8329-815aa5117d54"
          },
          "osdi:form": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
          },
          "osdi:person": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
          },
          "osdi:question_answers": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups/25d2d08f-7c3a-4bdc-8329-815aa5117d54/question_answers"
          }
        }
      },
      {
        "identifier": [
          "osdi_provider:13d2d08f-6c3a-3bec-8628-515aa5147e57"
        ],
        "created_at": "2014-02-20T21:32:56Z",
        "modified_at": "2014-02-20T21:32:56Z",
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups/13d2d08f-6c3a-3bec-8628-515aa5147e57"
          },
          "osdi:form": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
          },
          "osdi:person": {
            "href": "https://api.opensupporter.org/api/v1/people/35ad5d6ed-913e-12e6-a2e8-11673r314c14"
          },
          "osdi:question_answers": {
            "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups/13d2d08f-6c3a-3bec-8628-515aa5147e57/question_answers"
          }
        }
      },
      ...
    ]
  }
}
```


## A single signup on a form

```
GET /api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups/25d2d08f-7c3a-4bdc-8329-815aa5117d54
200 OK
```
```javascript
{
	"identifier": [
	  "osdi_provider:25d2d08f-7c3a-4bdc-8329-815aa5117d54"
	],
	"created_at": "2014-02-20T21:32:56Z",
	"modified_at": "2014-02-20T21:32:56Z",
	"_links": {
	  "self": {
	    "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups/25d2d08f-7c3a-4bdc-8329-815aa5117d54"
	  },
	  "osdi:form": {
	    "href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
	  },
	  "osdi:person": {
	    "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
	  },
	  "osdi:question_answers": {
      	"href": "https://api.opensupporter.org/api/v1/forms/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signups/25d2d08f-7c3a-4bdc-8329-815aa5117d54/question_answers"
      }
	}
}
```


# Adding/Modifying/Removing Resources (POST/PATCH/PUT/DELETE)

>TBD