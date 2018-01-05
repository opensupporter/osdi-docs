---
layout: default
title: Phonebank Result
---

# Phonebank Result

This page defines the Phonebank result resource.

A phonebank result occurs when one person attempts to contact another person in a phonebank.  For example, a campaign staffer calls a volunteer to ask whether he intends to attend the upcoming kick-off event.  The person being contacted is known as the "target" of the phonebank, and the target may have [Answers](answers.html) or [Taggings](taggings.html) applied to them as a result.  Phonebank result is always part of a [Phonebank](phone_bank.html).

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Canvass Fields](#phone-bank-result-fields)
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Phonebank result resources for a person (GET)](#scenario-retrieving-a-collection-of-phone-bank-result-for-a-person-get)
    * [Scenario: Retrieving a collection of Phonebank result resources for a phone bank (GET)](#scenario-retrieving-a-collection-of-phone-bank-result-for-a-phone-bank-get)
    * [Scenario: Retrieving an individual Phonebank result resource (GET)](#scenario-retrieving-an-individual-phone-bank-result-get)
    * [Scenario: Retrieving Answers for an individual Phonebank result resource (GET)](#scenario-retrieving-answers-for-an-individual-phone-bank-result-get)
    * [Scenario: Retrieving Taggings for an individual Phonebank result resource (GET)](#scenario-retrieving-taggings-for-an-individual-phone-bank-result-get)
    * [Scenario: Creating a new Phonebank result (POST)](#scenario-creating-a-new-phone-bank-result-post)
    * [Scenario: Modifying a Phonebank result (PUT)](#scenario-modifying-a-phone-bank-result-put)
    * [Scenario: Deleting a Phonebank result (DELETE)](#scenario-deleting-a-phone-bank-result-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for an Phone bank result resource is ```osdi:phone-bank-result``` for a single resource or ```osdi:phone-bank-results``` for a collection of resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Phone bank result Fields

| Name          | Type      | Description
|-----------    |-----------|--------------
|origin_system	  |string    |A human readable identifier of the system where this Phonebank result was created. (ex: "OSDI System")
|call_date		  |string	 |The date and time the call was made.
|caller_id        |string    |The phone number that is displayed as the caller-id for this call
|phone_number     |string    |The phone number that was called
|duration         |string    |The length of the phone call in seconds. Calls that do not connect will have zero in this field.
|disposition      |enum      |Disposition of the phone call. Possible values are "answer". "busy", "do-not-call", "meaningful interaction", "machine" etc..

_[Back to top...](#)_



### Links

{% include links_intro.md %}

|Name          	|Type		|Description
|-----------    |-----------|--------------
|self			|[Phonebank Result*](phone-bank-result.html)	|A self-referential link to the Phonebank result.
|caller         |[Person*](people.html)         |A link to a single Person resource representing the person who made the call
|target		    |[Person*](people.html)  |A link to a single Person resource representing the person who was contacted.
|answers        |[Answers[]*](answers.html) | A link to the collection of Answers to [Questions](questions.html) posed during the Phonebank.
|attendances    |[Attendances[]*](attendances.html) | A link to the collection of Attendances to [Events](events.html) posed during the Phonebank.
|taggings       |[Taggings[]*](taggings.html) | A link to the collection of Taggings applied as a result of the Phonebank.
|phonebank      |[Phonebank*](phone_bank.html) | A link to the Phonebank this result was part of.

_[Back to top...](#)_


## Related Resources

* [Question](questions.html)
* [Person](people.html)
* [Answer](answers.html)
* [Tagging](taggings.html)
* [Phonebank](phone_bank.html)
* [Attendances](attendances.html)
* [Events](events.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}


### Scenario: Retrieving a collection of Phonebank result resources for a person (GET)

Calling this endpoint allows consumers to see a person's phone bank result history.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result

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
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result?page=2"
        },
        "osdi:phone-bank-results": [
            {
                "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result"
        }
    },
    "_embedded": {
        "osdi:phone-bank-results": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2017-03-20T21:04:31Z",
                "modified_date": "2018-03-20T21:04:31Z",
                "call_date": "2017-03-18T11:02:15Z",
                "caller_id": "18552345678",
                "phone_number": "15104024182",
                "duration": 36,
                "disposition": "answer",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:caller": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316444"
                    },
                    "osdi:target": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
                    },
                    "osdi:taggings": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
                    },
                    "osdi:attendances": {
                        "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendances"
                    },
                    "osdi:phone_bank": {
                        "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2017-03-20T21:04:31Z",
                "modified_date": "2018-03-20T21:04:31Z",
                "call_date": "2017-03-18T11:02:15Z",
                "caller_id": "18552345678",
                "phone_number": "15104024182",
                "duration": 36,
                "disposition": "answer",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf"
                    },
                    "osdi:caller": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316444"
                    },
                    "osdi:target": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf/answers"
                    },
                    "osdi:taggings": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf/taggings"
                    },
                    "osdi:attendances": {
                        "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendances"
                    },
                    "osdi:phone_bank": {
                        "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_	

### Scenario: Retrieving a collection of Phonebank result resources for a phone bank (GET)

Calling this endpoint allows consumers to see a Phonebank's result history.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa/phone-bank-result

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
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result?page=2"
        },
        "osdi:phone-bank-results": [
            {
                "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa/phone-bank-result"
        }
    },
    "_embedded": {
        "osdi:phone-bank-results": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2017-03-20T21:04:31Z",
                "modified_date": "2018-03-20T21:04:31Z",
                "call_date": "2017-03-18T11:02:15Z",
                "caller_id": "18552345678",
                "phone_number": "15104024182",
                "duration": 36,
                "disposition": "answer",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:caller": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316444"
                    },
                    "osdi:target": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
                    },
                    "osdi:taggings": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
                    },
                    "osdi:attendances": {
                        "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendances"
                    },
                    "osdi:phone-bank": {
                        "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2017-03-20T21:04:31Z",
                "modified_date": "2018-03-20T21:04:31Z",
                "call_date": "2017-03-18T11:02:15Z",
                "caller_id": "18552345678",
                "phone_number": "15104024182",
                "duration": 40,
                "disposition": "machine",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf"
                    },
                    "osdi:caller": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316444"
                    },
                    "osdi:target": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:answers": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf/answers"
                    },
                    "osdi:taggings": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bcf/taggings"
                    },
                    "osdi:attendances": {
                        "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendances"
                    },
                    "osdi:phone-bank": {
                        "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
``` 

_[Back to top...](#)_ 


### Scenario: Retrieving an individual Phonebank result resource (GET)

Calling an individual Phonebank result resource will return the resource directly, along with all associated fields and appropriate links to additional information.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

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
    "created_date": "2017-03-20T21:04:31Z",
    "modified_date": "2018-03-20T21:04:31Z",
    "call_date": "2017-03-18T11:02:15Z",
    "caller_id": "18552345678",
    "phone_number": "15104024182",
    "duration": 36,
    "disposition": "answer",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:caller": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316444"
        },
        "osdi:target": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:attendances": {
            "href": "https://osdi-sample-system.org/api/v1/events/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendances"
        },
        "osdi:phone-bank": {
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
        }
    }
}
```

_[Back to top...](#)_

### Scenario: Retrieving Answers for an individual Phonebank result resource (GET)

Retrieves the Answers that were collected in a particular the Phonebank result.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers

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
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers?page=2"
        },
        "osdi:answers": [
            {
                "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        }
    },
    "_embedded": {
        "osdi:answers": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "action_date": "2014-03-18T11:02:15Z",
                "value": "He's not sure",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:question": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
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
                "responses": [
                    "Y"
                ],
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29/answers/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:question": {
                        "href": "https://osdi-sample-system.org/api/v1/questions/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/adb951cb-51f9-420e-b7e6-de953195ec86"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```

_[Back to top...](#)_

### Scenario: Retrieving Taggings for an individual Phonebank result resource (GET)

Retrieves the Taggings that were collected in a Phonebank result.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings

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
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings?page=2"
        },
        "osdi:taggings": [
            {
                "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/1efc3644-af25-4253-90b8-a0baf12dbd1e"
            },
        ],
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-sample-system.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        }
    },
    "_embedded": {
        "osdi:taggings": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "item_type": "osdi:person",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:tag": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
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
                "item_type": "osdi:event",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:tag": {
                        "href": "https://osdi-sample-system.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}

```

_[Back to top...](#)_


### Scenario: Creating a new Phonebank result (POST)

Posting to the Phonebank result collection endpoint and including a link to existing Phonebank, Answer and Tagging resource(s), will allow you to create a new phone bank result that indicates that the indicated Person was called during that phone bank and that the answers and taggings indicated were recorded as a result.  The response is the new phone bank result that was created.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "call_date": "2017-03-18T11:02:15Z",
    "caller_id": "18552345678",
    "phone_number": "15104024182",
    "duration": 56,
    "disposition": "answer",
    "_links" : {
        "osdi:caller" : { 
            "href" : "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316444" 
        },
        "osdi:phone-bank": {
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
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
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "call_date": "2017-03-18T11:02:15Z",
    "caller_id": "18552345678",
    "phone_number": "15104024182",
    "duration": 56,
    "disposition": "answer",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:caller": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316444"
        },
        "osdi:target": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        },
        "osdi:phone-bank": {
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a Phonebank result (PUT)

You can update an Phonebank result by calling a PUT operation on that result's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3

Header:
OSDI-API-Token:[your api key here]

{
    "disposition": "send_information"
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
    "call_date": "2017-03-18T11:02:15Z",
    "caller_id": "18552345678",
    "phone_number": "15104024182",
    "duration": 56,
    "disposition": "send_information",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:caller": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316444"
        },
        "osdi:target": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        },
        "osdi:phone-bank": {
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Deleting a Phonebank result (DELETE)

You may delete a Phonebank result by calling the DELETE command on the result's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/phone-bank-result/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This result was successfully deleted."
}
```

_[Back to top...](#)_
