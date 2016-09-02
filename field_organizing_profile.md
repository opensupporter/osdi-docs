---
layout: default
title: Field Organizing Profile
---

# Field Organizing Profile
This document describes the integration profile for Field Organizing. 

### Sections


* [Scenario Overview](#scenario-overview)
* [Related Resources](#related-resources)
* [API Exchanges](#api-exchanges)
    * [API Exchange: OCA retrieves the collection of scripts from VRM](#exchange-example-oca-list-collection-of-scripts-in-vrm)
    * [Exchange Example: OCA retrieves a script including questions and responses](#exchange-example-oca-retrieves-a-script-including-questions-and-responses)
    * [Exchange Example: OCA Submits canvass interaction results to VRM](#exchange-example-oca-submits-canvass-interaction-results-to-vrm)

## Scenario Overview

The Field Organizing Integration Profile assumes a common pattern where an OSDI compliant Canvassing Application (OCA) is used to canvass voters by asking them questions, capturing their responses and then reporting those responses to the Voter Relationship Manager (VRM)

The OCA may perform canvassing in a variety of ways such as mobile applications used by humans door-knocking, phone banking, mobile messaging etc.

The steps in this scenario, are loosely:

1. Voter import - This is currently out of band to the FOIP
2. API Exchange: OCA queries the collection of scripts in the VRM
3. OCA User selects relevant script(s) to canvass on
4. API Exchange: OCA downloads relevant scripts and associated questions
5. OCA side modifications or script processing may occur, such as applying branching or tailoring to the OCA
6. Field operations / canvassing occurs according to the OCA.
7. API Exchangfe: OCA reports canvassing result via record_canvass_helper


_[Back to top...](#)_

## Related Resources

* [Record Attendance Helper](record_attendance.html)
* [Event](events.html)
* [Person](people.html)

_[Back to top...](#)_

## API Exchanges

## Exchange Example: OCA retrieves the collection of scripts from VRM
#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/scripts

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "total_records": 1,
  "per_page": 1,
  "_links": {
    "self": {
      "href": "http://osdi-sample-system.org/api/v1/scripts"
    },
    "osdi:scripts": [
      {
        "href": "http://osdi-sample-system.org/api/v1/scripts/235196"
      }
    ]
  },
  "_embedded": {
    "osdi:scripts": [
      {
        "origin_system": "OSDI Sample System",
        "name": "osdi_script",
        "description": "OSDI Test Script",
        "title": "osdi_script",
        "summary": "OSDI Test Script",
        "status": "Active",
        "identifiers": [
          "osdi_sample_system:235196"
        ],
        "_links": {
          "self": {
            "href": "http://osdi-sample-system.org/api/v1/scripts/235196"
          }
        }
      }
    ]
  }
}
````


## Exchange Example: OCA retrieves a script including questions and responses
#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/scripts/235196

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "origin_system": "OSDI Sample System",
  "name": "osdi_script",
  "description": "OSDI Test Script",
  "title": "osdi_script",
  "summary": "OSDI Test Script",
  "status": "Active",
  "identifiers": [
    "osdi_sample_system:235196"
  ],
  "_links": {
    "self": {
      "href": "http://osdi-sample-system.org/api/v1/scripts/235196"
    }
  },
  "_embedded": {
    "osdi:script_questions": [
      {
        "origin_system": "OSDI Sample System",
        "name": "foobarbaz",
        "description": "What is your name?",
        "sequence": 1,
        "_embedded": {
          "osdi:question": {
            "origin_system": "OSDI Sample System",
            "name": "foobar",
            "description": "What is your name?",
            "title": "foobar",
            "summary": "What is your name?",
            "question_type": "SingleChoice",
            "identifiers": [
              "osdi_sample_system:202004"
            ],
            "_links": {
              "self": {
                "href": "http://osdi-sample-system.org/api/v1/questions/202004"
              },
              "curies": [
                {
                  "name": "osdi",
                  "href": "http://developers.ngpvan.com/osdi#{rel}",
                  "templated": true
                }
              ]
            }
          }
        },
        "_links": {
          "self": {
            "href": "http://osdi-sample-system.org/api/v1/scripts/235196/script_questions/1"
          },
          "osdi:question": {
            "href": "http://osdi-sample-system.org/api/v1/questions/202004"
          },
          "osdi:script": {
            "href": "http://osdi-sample-system.org/api/v1/scripts/235196"
          }
        }
      },
      {
        "origin_system": "OSDI Sample System",
        "name": "phone bank",
        "description": "Will you phone bank?",
        "sequence": 2,
        "_embedded": {
          "osdi:question": {
            "origin_system": "OSDI Sample System",
            "name": "pbank",
            "description": "Will you phone bank?",
            "title": "pbank",
            "summary": "Will you phone bank?",
            "question_type": "SingleChoice",
            "responses": [
              {
                "key": "856278",
                "name": "Yes",
                "title": "Yes"
              },
              {
                "key": "856279",
                "name": "No",
                "title": "No"
              }
            ],
            "identifiers": [
              "osdi_sample_system:203079"
            ],
            "_links": {
              "self": {
                "href": "http://osdi-sample-system.org/api/v1/questions/203079"
              },
              "curies": [
                {
                  "name": "osdi",
                  "href": "http://developers.ngpvan.com/osdi#{rel}",
                  "templated": true
                }
              ]
            }
          }
        },
        "_links": {
          "self": {
            "href": "http://osdi-sample-system.org/api/v1/scripts/235196/script_questions/2"
          },
          "osdi:question": {
            "href": "http://osdi-sample-system.org/api/v1/questions/203079"
          },
          "osdi:script": {
            "href": "http://osdi-sample-system.org/api/v1/scripts/235196"
          }
        }
      },
      {
        "origin_system": "OSDI Sample System",
        "name": "Data Entry",
        "sequence": 3,
        "_embedded": {
          "osdi:question": {
            "origin_system": "OSDI Sample System",
            "question_type": "SingleChoice",
            "identifiers": [
              "osdi_sample_system:52472"
            ],
            "_links": {
              "self": {
                "href": "http://osdi-sample-system.org/api/v1/questions/52472"
              },
              "curies": [
                {
                  "name": "osdi",
                  "href": "http://developers.ngpvan.com/osdi#{rel}",
                  "templated": true
                }
              ]
            }
          }
        },
        "_links": {
          "self": {
            "href": "http://osdi-sample-system.org/api/v1/scripts/235196/script_questions/3"
          },
          "osdi:question": {
            "href": "http://osdi-sample-system.org/api/v1/questions/52472"
          },
          "osdi:script": {
            "href": "http://osdi-sample-system.org/api/v1/scripts/235196"
          }
        }
      }
    ]
  }
}
````


## Exchange Example: OCA Submits canvass interaction results to VRM

#### Request

```javascript
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
