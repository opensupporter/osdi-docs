---
layout: default
title: Simple Organizing Profile
---

# Simple Organizing Profile
This document describes the integration profile for Simple Organizing. This is used by Spoke.

### Sections


* [Scenario Overview](#scenario-overview)
* [Related Resources](#related-resources)
* [API Exchanges](#api-exchanges)
    * [API Exchange: OCA retrieves the collection of scripts from VRM](#exchange-example-oca-list-collection-of-scripts-in-vrm)
    * [Exchange Example: OCA retrieves a script including questions and responses](#exchange-example-oca-retrieves-a-script-including-questions-and-responses)
    * [Exchange Example: OCA Submits canvass interaction results to VRM](#exchange-example-oca-submits-canvass-interaction-results-to-vrm)

## Scenario Overview

The Simple Organizing Integration Profile assumes a common pattern where an OSDI compliant Canvassing Application (OCA) is used to canvass voters by asking them questions, capturing their responses and then reporting those responses to the Voter Relationship Manager (VRM)

The OCA may perform canvassing in a variety of ways such as mobile applications used by humans door-knocking, phone banking, mobile messaging etc.

The steps in this scenario, are loosely:

1. Voter import via List Exchange Profile or out of band bulk import
2. API Exchange: OCA queries the collection of questions and responses in the VRM
3. API Exchange: OCA queries the collection of tags/Activist Codes in the VRM
3. OCA User assigns the questions, responses and tags to appropriate actions in the OCA, such as responses in its local scripts. 

When assigned events occur, the OCA will submit data back to the VRM
1. [Optional if OCA doesn't have the VRM ID] Person Signup Helper is used to match the OCA person to the VRM person.  The OCA may apply tags during this as well.
2. Record Canvass Helper is used to apply question responses, and tags to a person



_[Back to top...](#)_

## Related Resources

* [Person Signup Helper](person_signup.html)
* [Person](people.html)
* [Tag](tags.html)
* [Question](questions.html)
* [List Exchange Profile](list_exchange_profile.html)

_[Back to top...](#)_

## API Exchanges

## Exchange Example: OCA retrieves the collection of scripts from VRM
#### Request

```
GET https://osdi-sample-system.org/api/v1/questions

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```json
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "total_pages": null,
  "per_page": 50,
  "page": 1,
  "_links": {
    "self": {
      "href": "http://osdi-sample-system.org/api/v1//api/v1/questions"
    }
  },
  "_embedded": {
    "osdi:questions": [
           {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "Volunteer Question",
                "title": "Do you want to volunteer?",
                "description": "<p>Do you want to volunteer? It will only take a few hours of time per week.</p>",
                "summary": "Volunteer question for canvass",
                "question_type": "SingleChoice",
                "responses": [
                  {
                    "key": "Y",
                    "name": "yes",
                    "title": "Yes"
                  },
                  {
                    "key": "M",
                    "name": "maybe",
                    "title": "Maybe"
                  },
                  {
                    "key": "N",
                    "name": "no",
                    "title": "No"
                  }
                ],
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    }
                }
            }
        ]
    }
}
````



## Exchange Example: OCA Submits canvass interaction results to VRM

#### Request

```json
POST https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/record_canvass_helper

Header:
OSDI-API-Token:[your api key here]

{
    "canvass": {
      "origin_system": "OSDI Sample System",
      "action_date": "2014-03-18T11:02:15Z",
      "contact_type": "in-person",
      "input_type": "mobile",
      "success": true,
      "status_code": "",
      "canvasser": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316444"
    },
    "triggers": {
        "autoresponse": {
            "enabled": true
        }
    },
    "add_tags": [
        "volunteer",
        "donor"
    ],
    "add_tags_uri": [
        "https://osdi-sample-system.org/api/v1/tags/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
    ],
    "add_lists": [
        "supporters"
    ],
    "add_lists_uri": [
        "https://osdi-sample-system.org/api/v1/lists/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
    ],
    "add_questions_responses_uri": [
      {
        "question": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29",
        "responses": [ "r1", "r2", "r2"]
      },
      {
        "question": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c2a",
        "value": "Heard about the candidate at the Labor Day Picnic"
      }
    ]
}

```

#### Response

```json
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
    "contact_type": "in-person",
    "input_type": "mobile",
    "success": true,
    "status_code": "",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:canvasser": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316444"
        },
        "osdi:target": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/canvasses/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        }
    }
}
````

_[Back to top...](#)_


## Exchange Example: OCA Uses Person Signup Helper to Match/Create Person in VRM

#### Request

```json
POST https://osdi-sample-system.org/api/v1/people/person_signup_helper/

Header:
OSDI-API-Token:[your api key here]

{
    "person": {
        "identifiers": [
            "foreign_system:1"
        ],
        "family_name": "Edwin",
        "given_name": "Labadie",
        "additional_name": "Marques",
        "origin_system": "OpenSupporter",
        "email_addresses": [
            {
                "address":"test-3@example.com",
                "primary": true,
                "address_type": "Personal"
            }
        ],
        "postal_addresses": [
            {
                "primary": true,
                "address_lines": [
                    "935 Ed Lock"
                ],
                "locality": "New Dudley",
                "region": "MN",
                "postal_code": "17678",
                "country": "RU",
                "address_type": "Home",
                "status": "Verified"
            }
        ],
        "phone_numbers": [
            {
                "primary": true,
                "number": 19876543210,
                "number_type": "Mobile",
                "sms_capable": true
            }
        ],
        "gender": "Male"
    },
{% include helper_action_examples.md %}
}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "id": "d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
        "foreign_system:1"
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "family_name": "Edwin",
    "given_name": "Labadie",
    "additional_name": "Marques",
    "origin_system": "OpenSupporter",
    "email_addresses": [
        {
            "address":"test-3@example.com",
            "primary": true,
            "address_type": "Personal"
        }
    ],
    "postal_addresses": [
        {
            "primary": true,
            "address_lines": [
                "935 Ed Lock"
            ],
            "locality": "New Dudley",
            "region": "MN",
            "postal_code": "17678",
            "country": "RU",
            "address_type": "Home",
            "status": "Verified"
        }
    ],
    "phone_numbers": [
        {
            "primary": true,
            "number": 19876543210,
            "number_type": "Mobile",
            "sms_capable": true
        }
    ],
    "gender": "Male",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/answers"
        },
        "osdi:attendance": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/attendance"
        },
        "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/signatures"
        },
        "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/submissions"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/donations"
        },
        "osdi:outreaches": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/outreaches"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/taggings"
        },
        "osdi:items": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/items"
        }
    }
}
```

_[Back to top...](#)_
