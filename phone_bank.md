---
layout: default
title: Phonebank
---

# Phonebank

This page defines the Phonebank resource.

Phonebank resource represent specific phone banking events planned for a specific time period. The resource contains information about start and end time, people to be called, and a [Script](scripts.html) that is used for the effort. As people are contacted, [Phonebank Result](phone_bank_result.html) resources are created representing the individual interaction between a volunteer and a person, as well as the data that resulted from that interaction.

### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Script Fields](#effort-fields)
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Phonebank resources (GET)](#scenario-retrieving-a-collection-of-phonebank-resources-get)
    * [Scenario: Retrieving an individual Phonebank resource (GET)](#scenario-retrieving-an-individual-phonebank-resource-get)
    * [Scenario: Creating a new Phonebank (POST)](#scenario-creating-a-new-phonebank-post)
    * [Scenario: Modifying a Phonebank (PUT)](#scenario-modifying-a-phonebank-put)
    * [Scenario: Deleting a Phonebank (DELETE)](#scenario-deleting-a-phonebank-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for an Phonebank resource is ```osdi:phonebank``` for a single Phonebank resource or ```osdi:phonebanks``` for a collection of Phonebank resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_

### Phonebank Fields

| Name          | Type                | Description
| -----------   | -----------         | --------------
|origin_system      |string     |A human readable identifier of the system where this Phonebank was created. (ex: "OSDI System")
|name               |string     |The name of the Phonebank. Intended for administrative display rather than a public title, though may be shown to a user.
|title              |string     |The title of the Phonebank. Intended for public display rather than administrative purposes.
|description        |string     |A description of the Phonebank, usually displayed publicly. May contain text and/or HTML.
|summary            |string     |A text-only single paragraph summarizing the Phonebank. Shown on listing pages that have more than titles, but not enough room for full description.
|start_time        |datetime     |The start date and time for the Phone banking Effort.
|end_time        |datetime     |The end date and time for the Phone banking Effort.
|daily_start_hour |integer     |The hour of the day volunteers should start calling. This is in 24 hour time
|daily_stop_hour |integer     |The hour of the day volunteers should stop calling. This is in 24 hour time
|caller_id        |string     |The phone number that is displayed as the caller-id for this phonebank
|status           |flexenum      |Status of the Phonebank. Possible values are: "draft", "paused", "scheduled", "started", or "stopped"
|dialing_mode           |flexenum      |The type of the dialing for this phonebank. One of "predictive", "power", "manual", or another value.
|voicemail_audio_url    |string      |A URL string pointing to a audio file used for voice mail audio drops.
|administrative_url    |string      |A URL string pointing to the Phonebank administrative page on the web.
|browser_url    |string      |A URL string pointing to the Phonebank public page on the web.
|total_completed	|integer	|A read-only computed property representing the current count of the total number completed on the Phonebank.


_effort [Back to top...](#)_

### Links

{% include links_intro.md %}

| Name          | Type       | Description
|-----------    |----------- |-----------
|self           |[Phonebank*](phone_bank.html)    |A self-referential link to the phone bank.
|creator        |[Person*](people.html)         |A link to a single Person resource representing the creator of the Phonebank.
|modified_by    |[Person* ](people.html)        |A link to a Person resource representing the last editor of this Phonebank.
|taggings       |[Taggings[]* ](taggings.html)    |A link to the collection of Tagging resources for this Phonebank.
|phone_bank_results      |[Phonebank_results[]*](phone_bank_result.html)        |A link to a collection of Phone bank results resources representing the results that occured.
|script  |[Script*](scripts.html) | A link to the Script resource associated with this Phonebank.
|target_list  |[List*](lists.html) | A link to the List resource that represents the list of People who will receive calls in this phonebank.
|advocacy_targets  |[List*](lists.html) | A link to the List resource that represents the list of People who will be advocacy targets in this phonebank.
|volunteers  |[List*](lists.html) | A link to the List resource that represents the list of People who will be the volunteers in this phonebank.
|events  |[List*](lists.html) | A link to the List resource that represents a collection of events associated with this Phonebank. These are the events volunteers are signing up people for in the phonebank.


_[Back to top...](#)_


## Related Resources

* [Person](people.html)
* [List](lists.html)
* [Script](scripts.html)
* [Taggings](taggings.html)
* [Phone bank result](phone_bank_result.html)


_[Back to top...](#)_


## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Phonebank resources (GET)

Phonebank resources are sometimes presented as collections of phonebanks. For example, calling the phone banks endpoint will return a collection of all the phone banks in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/phone_bank/

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
            "href": "https://osdi-sample-system.org/api/v1/phone_bank?page=2"
        },
        "osdi:phone_bank": [
            {
                "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/phone_bank/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/phone_bank"
        }
    },
    "_embedded":
    {
        "osdi:phone_bank": [
            {
                "identifiers": [
                    "osdi_sample_system:a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bca",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2017-03-20T21:04:31Z",
                "modified_date": "2017-03-20T21:04:31Z",
                "name": "Rally for Mountains",
                "title": "Rally for Mountains Team 2",
                "description": "Rally for Mountains phone bank for Team 2",
                "summary": "Rally for Mountains phone bank effort 1 for Team 2",
                "start_time": "2018-02-19T8:00:00Z",
                "end_time": "2018-02-20T8:00:00Z",
                "type": "power",
                "daily_start_hour": 9,
                "daily_stop_hour": 17,
                "caller_id": "18552345678",
                "status": "started",
                "administrative_url": "http://osdi-sample-system.org/pb-campaigns/rally-v1/manage",
                "browser_url": "http://osdi-sample-system.org/pb-campaigns/rally-v1",
                "voicemail_audio_url": "http://osdi-sample-system.org/audio-files/rally-voicemail.mp3",
                "total_completed": 100,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/phone_bank/a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bca"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:taggings": {
                        "href": "https://osdi-sample-system.org/api/v1/phone_bank/a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bca/taggings"
                    },
                    "osdi:script": {
                        "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
                    },
                    "osdi:target_list": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:advocacy_targets": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:volunteers": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:events": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:phone_bank_results": {
                        "href": "https://osdi-sample-system.org/api/v1/phone_bank/a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bca/phone_bank_results"
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2017-03-20T21:04:31Z",
                "modified_date": "2017-03-20T21:04:31Z",
                "name": "Rally for Rivers",
                "title": "Rally for Rivers Team 1",
                "description": "Rally for Rivers phone bank for Team 1",
                "summary": "Rally for Rivers phone bank effort 1 for Team 1",
                "start_time": "2016-02-19T8:00:00Z",
                "end_time": "2016-02-20T8:00:00Z",
                "type": "power",
                "daily_start_hour": 9,
                "daily_stop_hour": 17,
                "caller_id": "18552345678",
                "status": "started",
                "administrative_url": "http://osdi-sample-system.org/pb-campaigns/rally-v1/manage",
                "browser_url": "http://osdi-sample-system.org/pb-campaigns/rally-v1",
                "voicemail_audio_url": "http://osdi-sample-system.org/audio-files/rally-voicemail.mp3",
                "total_completed": 100,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:script" : {
                        "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
                    },
                    "osdi:target_list": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:advocacy_targets": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:volunteers": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:events": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:phone_bank_results": {
                        "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/phone_bank_results"
                    }
                }
            },   
            //truncated for brevity
        ]
    }
}
```

_[Back to top...](#)_       

### Scenario: Retrieving an individual Phone bank resource (GET)

Calling an individual Phonebank resource will return the resource directly.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa

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
        "osdi_sample_system:a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bca",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2017-03-20T21:04:31Z",
    "modified_date": "2017-03-20T21:04:31Z",
    "name": "Rally for Rivers",
    "title": "Rally for Rivers Team 1",
    "description": "Rally for Rivers phone bank for Team 1",
    "summary": "Rally for Rivers phone bank effort 1 for Team 1",
    "start_time": "2018-02-19T8:00:00Z",
    "end_time": "2018-02-20T8:00:00Z",
    "type": "power",
    "daily_start_hour": 9,
    "daily_stop_hour": 17,
    "caller_id": "18552345678",
    "status": "started",
    "administrative_url": "http://osdi-sample-system.org/pb-campaigns/rally-v1/manage",
    "browser_url": "http://osdi-sample-system.org/pb-campaigns/rally-v1",
    "voicemail_audio_url": "http://osdi-sample-system.org/audio-files/rally-voicemail.mp3",
    "total_completed": 100,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:script" : {
            "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
        },
        "osdi:target_list": {
            "href": "https://osdi-sample-system.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
        },
        "osdi:advocacy_targets": {
            "href": "https://osdi-sample-system.org/api/v1/lists/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:volunteers": {
            "href": "https://osdi-sample-system.org/api/v1/lists/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:events": {
            "href": "https://osdi-sample-system.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
        },
        "osdi:phone_bank_results": {
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/phone_bank_results"
        }
    }
}
```


_[Back to top...](#)_


### Scenario: Creating a new Phonebank resource (POST)

Posting to the effort collection endpoint will allow you to create a new Phonebank. The response is the new Phonebank resource that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/phone_bank/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "name": "Rally for Rivers",
    "title": "Rally for Rivers Team 1",
    "description": "Rally for Rivers phone bank for Team 1",
    "summary": "Rally for Rivers phone bank effort 1 for Team 1",
    "start_time": "2018-02-19T8:00:00Z",
    "end_time": "2018-02-20T8:00:00Z",
    "daily_start_hour": 9,
    "daily_stop_hour": 17,
    "type": "power",
    "caller_id": "18552345678",
    "voicemail_audio_url": "http://osdi-sample-system.org/audio-files/rally-voicemail.mp3",
    "_links": {
        "osdi:script": {
            "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
        },
        "osdi:target_list": {
            "href": "https://osdi-sample-system.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
        },
        "osdi:volunteers": {
            "href": "https://osdi-sample-system.org/api/v1/lists/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
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
    "created_date": "2017-03-20T21:04:31Z",
    "modified_date": "2017-03-20T21:04:31Z",
    "name": "Rally for Rivers",
    "title": "Rally for Rivers Team 1",
    "description": "Rally for Rivers phone bank for Team 1",
    "summary": "Rally for Rivers phone bank effort 1 for Team 1",
    "start_time": "2018-02-19T8:00:00Z",
    "end_time": "2018-02-20T8:00:00Z",
    "type": "power",
    "daily_start_hour": 9,
    "daily_stop_hour": 17,
    "caller_id": "18552345678",
    "status": "pending",
    "administrative_url": "http://osdi-sample-system.org/pb-campaigns/rally-v1/manage",
    "browser_url": "http://osdi-sample-system.org/pb-campaigns/rally-v1",
    "voicemail_audio_url": "http://osdi-sample-system.org/audio-files/rally-voicemail.mp3",
    "total_completed": 0,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:script" : {
            "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
        },
        "osdi:target_list": {
            "href": "https://osdi-sample-system.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
        },
        "osdi:volunteers": {
            "href": "https://osdi-sample-system.org/api/v1/lists/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:phone_bank_results": {
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/phone_bank_results"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a Phonebank resource (PUT)

You can update a phonebank resource by calling a PUT operation on that phone bank's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0baa

Header:
OSDI-API-Token:[your api key here]

{
    "name": "Rally for Mountains",
    "title": "Rally for Mountains Team 2",
    "description": "Rally for Mountains phone bank for Team 2",
    "summary": "Rally for Mountains phone bank effort 1 for Team 2",
    "status": "started"
}

```

#### Response
```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate
{
    "identifiers": [
        "osdi_sample_system:a91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bca",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Sample System",
    "created_date": "2017-03-20T21:04:31Z",
    "modified_date": "2017-03-20T21:04:31Z",
    "name": "Rally for Mountains",
    "title": "Rally for Mountains Team 2",
    "description": "Rally for Mountains phone bank for Team 2",
    "summary": "Rally for Mountains phone bank effort 1 for Team 2",
    "start_time": "2018-02-19T8:00:00Z",
    "end_time": "2018-02-20T8:00:00Z",
    "type": "power",
    "daily_start_hour": 9,
    "daily_stop_hour": 17,
    "caller_id": "18552345678",
    "status": "started",
    "administrative_url": "http://osdi-sample-system.org/pb-campaigns/rally-v1/manage",
    "browser_url": "http://osdi-sample-system.org/pb-campaigns/rally-v1",
    "voicemail_audio_url": "http://osdi-sample-system.org/audio-files/rally-voicemail.mp3",
    "total_completed": 100,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:script" : {
            "href": "https://osdi-sample-system.org/api/v1/script/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0ba3"
        },
        "osdi:target_list": {
            "href": "https://osdi-sample-system.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
        },
        "osdi:advocacy_targets": {
            "href": "https://osdi-sample-system.org/api/v1/lists/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:volunteers": {
            "href": "https://osdi-sample-system.org/api/v1/lists/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:events": {
            "href": "https://osdi-sample-system.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
        },
        "osdi:phone_bank_results": {
            "href": "https://osdi-sample-system.org/api/v1/phone_bank/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/phone_bank_results"
        }
    }
}
```


_[Back to top...](#)_


### Scenario: Deleting a Phonebank Resource (DELETE)

You may delete an effort by calling the DELETE command on the Phonebank's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/phone_bank/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This phonebank was successfully deleted."
}
```

_[Back to top...](#)_
