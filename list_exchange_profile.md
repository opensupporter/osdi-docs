---
layout: default
title: List Exchange Profile
---

# List Exchange Profile
This document describes the integration profile for exchanging lists and tags between systems. 

### Sections


* [Scenario Overview](#scenario-overview)
* [Related Resources](#related-resources)
* [API Exchanges](#api-exchanges)
    * [Exchange Example: Get list of lists](#exchange-example-get-list-of-lists)
    * [Exchange Example: Import people from list](#exchange-example-import-people-from-list)
    * [Exchange Example: Tag person with tagging](#exchange-example-tag-person-with-tagging)

## Scenario Overview

The List Exchange Integration Profile assumes a common pattern where an OSDI compliant application pulls a list of people from another OSDI compliant application. The first OSDI application then performs some action on those people (say, sending them a text message or an email) and send data back to the second OSDI application in the form of tags.

The steps in this scenario, are loosely:

1. API Exchange: The first application queries the lists collection in the second application to find available lists to import.
2. Choose list: A user of the first application chooses a list to import.
3. API Exchange: The first application imports people on the list from the second application by paging through the items collection of the list and following links to the associated person.
4. Actions happen: Actions happen in the first system on the imported people, such as sending them a text message or an email.
5. API Exchange: The first system sends back tag information to the second system, storing results of the action on the people in the first system in the second system as taggings.

_[Back to top...](#)_

## Related Resources

* [List](lists.html)
* [Item](items.html)
* [Person](people.html)
* [Tagging](taggings.html)

_[Back to top...](#)_

## API Exchanges

### Exchange Example: Get list of lists

#### Request

```javascript
GET https://osdi-application-two.org/api/v1/lists/

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
            "href": "https://osdi-application-two.org/api/v1/lists?page=2"
        },
        "osdi:lists": [
            {
                "href": "https://osdi-application-two.org/api/v1/lists/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-application-two.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
            },
            //(truncated for brevity)
        ],
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-application-two.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": "https://osdi-application-two.org/api/v1/lists"
        }
    },
    "_embedded": {
        "osdi:lists": [
            {
                "identifiers": [
                    "osdi_application_two:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "Main Email List Subscribers",
                "summary": "The main email list.",
                "browser_url": "http://osdi-application-two.org/lists/main-email-list",
                "total_items": 1748920,
                "_links": {
                    "self": {
                        "href": "https://osdi-application-two.org/api/v1/lists/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:items": {
                        "href": "https://osdi-application-two.org/api/v1/lists/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/items"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-application-two.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-application-two.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_application_two:1efc3644-af25-4253-90b8-a0baf12dbd1e"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T20:44:13Z",
                "modified_date": "2014-03-20T20:44:13Z",
                "title": "Membership List",
                "browser_url": "http://osdi-application-two.org/lists/members",
                "total_results": 108273,
                "_links": {
                    "self": {
                        "href": "https://osdi-application-two.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:items": {
                        "href": "https://osdi-application-two.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e/items"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-application-two.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-application-two.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```

_[Back to top...](#)_


### Exchange Example: Import people from list

#### Request

```javascript
GET https://osdi-application-two.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items

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
            "href": "https://osdi-application-two.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items?page=2"
        },
        "osdi:items": [
            {
                "href": "https://osdi-application-two.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-application-two.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/1efc3644-af25-4253-90b8-a0baf12dbd1e"
            },
            //(truncated for brevity)
        ],
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-application-two.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": "https://osdi-application-two.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items"
        }
    },
    "_embedded": {
        "osdi:items": [
            {
                "identifiers": [
                    "osdi_application_two:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "item_type": "osdi:person",
                "_links": {
                    "self": {
                        "href": "https://osdi-application-two.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:list": {
                        "href": "https://osdi-application-two.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:person": {
                        "href": "https://osdi-application-two.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_application_two:1efc3644-af25-4253-90b8-a0baf12dbd1e"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T20:44:13Z",
                "modified_date": "2014-03-20T20:44:13Z",
                "item_type": "osdi:event",
                "_links": {
                    "self": {
                        "href": "https://osdi-application-two.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:list": {
                        "href": "https://osdi-application-two.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:event": {
                        "href": "https://osdi-application-two.org/api/v1/events/adb951cb-51f9-420e-b7e6-de953195ec86"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

This items import process would then continue, using the paging links provided. So the first application would then visit ```https://osdi-application-two.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29/items?page=2``` to download the second page of items, and so on.

Then, the first application would visit the ```osdi:person``` links for each item downloaded to download person data, like this:

#### Request

```javascript
GET https://osdi-application-two.org/api/v1/people/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
        "osdi_application_two:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
        "foreign_system:1"
    ],
    "origin_system": "OSDI Application Two",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "given_name": "John",
    "family_name": "Smith",
    "honorific_prefix": "Mr.",
    "honorific_suffix": "Ph.D",
    "additional_name": "Scott",
    "gender": "Male",
    "gender_identity": "Male",
    "party_identification": "Democratic",
    "birthdate": {
        "month": 6,
        "day": 2,
        "year": 1973
    },
    "ethnicities": [
        "African American"
    ],
    "languages_spoken": [
        "en",
        "fr"
    ],
    "employer": "Acme Corp",
    "employer_address": {
        "venue": "Bull Hall",
        "address_lines": [
            "123 Acme Street",
            "Suite 400"
        ],
        "locality": "New Yorkhaven",
        "region": "NY",
        "postal_code": "10001",
        "country": "US",
        "language": "en",
        "location": {
            "latitude": 38.9382,
            "longitude": -77.3349,
            "accuracy": "Rooftop"
        },
        "status": "Verified"
    },
    "occupation": "Accountant",
    "postal_addresses": [
        {
            "primary": true,
            "address_type": "Home",
            "address_lines": [
                "1900 Pennsylvania Ave"
            ],
            "locality": "Washington",
            "region": "DC",
            "postal_code": "20009",
            "country": "US",
            "language": "en",
            "location": {
                "latitude": 38.919,
                "longitude": -77.0379,
                "accuracy": "Rooftop"
            }
        }
    ],
    "email_addresses": [
        {
            "primary": true,
            "address": "johnsmith@mail.com",
            "address_type": "personal",
            "status": "subscribed"
        }
    ],
    "phone_numbers": [
        {
            "primary": true,
            "number": "11234567890",
            "extension": "432",
            "description": "Worksite line",
            "number_type": "Work",
            "operator": "ATT",
            "country": "US",
            "sms_capable": false,
            "do_not_call": true
        }
    ],
    "profiles": [
        {
            "provider": "Facebook",
            "id": "john.doe.1234",
            "url": "https://facebook.com/john.doe"
        },
        {
            "provider": "Twitter",
            "id": "eds34d8j2kddfd45",
            "url": "https://twitter.com/johndoe",
            "handle": "johndoe"
        }
    ],
    "custom_fields": {
        "is_volunteer": "true",
        "most_important_issue": "Equal pay",
        "union_member": "true"
    },
    "_links": {
        "self": {
            "href": "https://osdi-application-two.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:answers": {
            "href": "https://osdi-application-two.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/answers"
        },
        "osdi:attendance": {
            "href": "https://osdi-application-two.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendance"
        },
        "osdi:signatures": {
            "href": "https://osdi-application-two.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
        },
        "osdi:submissions": {
            "href": "https://osdi-application-two.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
        },
        "osdi:donations": {
            "href": "https://osdi-application-two.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
        },
        "osdi:outreaches": {
            "href": "https://osdi-application-two.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/outreaches"
        },
        "osdi:taggings": {
            "href": "https://osdi-application-two.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
        },
        "osdi:items": {
            "href": "https://osdi-application-two.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/items"
        },
        "osdi:record_canvass_helper": {
            "href": "https://osdi-application-two.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/record_canvass_helper"
        }
    }
}
```

_[Back to top...](#)_	


### Exchange Example: Tag person with tagging

#### Request

```javascript
POST https://osdi-application-two.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/

Header:
OSDI-API-Token:[your api key here]

{
    "_links" : {
        "osdi:person" : { 
            "href" : "https://osdi-application-two.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f" 
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
        "osdi_application_two:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "item_type": "osdi:person",
    "_links": {
        "self": {
            "href": "https://osdi-application-two.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29/taggings/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
        },
        "osdi:tag": {
            "href": "https://osdi-application-two.org/api/v1/tags/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:person": {
            "href": "https://osdi-application-two.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        }
    }
}
```

_[Back to top...](#)_