---
layout: default
title: Message
---

# Message

This document defines the Message resource. 

Message resources represent a some type of mass communication -- a mass email to an email list, an SMS sent to an SMS list, etc... -- that is sent or otherwise communicated to to a list of people. Messages have fields to describe them such as names, subject lines, contents, statistics about delivery and engagement, and the like. Messages can also be linked to queries for targeting a list of people, lists for showing who received the message, and similar metadata. Messages can be one of two types, ```email``` or ```sms```, indicating how the message was delivered.


### Sections

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Message Fields](#message-fields)  
    * [Related Objects](#related-objects)
    * [Links](#links)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Message resources (GET)](#scenario-retrieving-a-collection-of-message-resources-get)
    * [Scenario: Retrieving an individual Message resource (GET)](#scenario-scenario-retrieving-an-individual-message-resource-get)
    * [Scenario: Creating a new message (POST)](#scenario-creating-a-new-message-post)
    * [Scenario: Modifying an message (PUT)](#scenario-modifying-an-message-put)
    * [Scenario: Adding queries to a message (POST)](#scenario-adding-queries-to-a-message-post)
    * [Scenario: Deleting an message (DELETE)](#scenario-deleting-an-message-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for an Message resource is ```osdi:message``` for a single Message resource or ```osdi:messages``` for a collection of Message resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Message Fields

A list of fields specific to the Message resource.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|origin_system		|string     |A human readable identifier of the system where this message was created. (ex: "OSDI System")
|name				|string		|The name of the message. Intended for administrative display rather than a public title, though may be shown to a user.
|subject			|string		|The subject of the message. (ex: email type messages will put the subject line of the email in this field)
|body				|string		|The content of the message. May contain text and/or HTML. (ex: email type messages will put the HTML content of the email here)
|from				|string		|The from line of the message. (ex: email messages can be from "John Doe" or "Progressives United". SMS messages can be from "202-123-4567")
|reply_to			|string		|The reply to field for the message. (ex: emails may have a reply_to of "info@progressivesunited.org")
|administrative_url		|string		|A URL string pointing to the message's administrative page on the web.
|browser_url		|string		|A URL string pointing to the message's public page on the web.
|type				|enum		|The type of message. One of "email" or "sms".
|total_targeted		|integer	|A read-only computed property representing the current count of the total number of people targeted to receive this message.
|status				|enum		|Status of the message.  Possible values are: "draft", "calculating", "scheduled", "sending", "stopped", or "sent".
|scheduled_date		|datetime	|The date and time the message is scheduled to be sent.
|sent_start_date	|datetime	|The date and time the message started sending.
|sent_end_date		|datetime	|The date and time the message finished sending.
|daily_start_hour	|integer	|The hour of the day messages should start sending. (ex: SMS campaigns may only be sent during certain hours of the day)
|daily_stop_hour	|integer	|The hour of the day messages should stop sending. (ex: SMS campaigns may only be sent during certain hours of the day)
|statistics			|[Statistics](#statistics)	|An object hash representing the engagement statistics for this message. (ex: open rate and unsubscribe rate)

_[Back to top...](#)_


### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Statistics

|Name          |Type      |Description
|-----------    |-----------|--------------
|statistics.sent	|integer    |A read-only computed property representing the total number of messages sent.
|statistics.opened	|integer    |A read-only computed property representing the total number of messages opened.
|statistics.clicked	|integer    |A read-only computed property representing the total number of messages where a link was clicked.
|statistics.actions	|integer    |A read-only computed property representing the total number of action taken by people after clicking links in this message.
|statistics.forwards	|integer    |A read-only computed property representing the total number of times this message was forwarded.
|statistics.unsubscribed	|integer    |A read-only computed property representing the total number of messages where the person receiving the message unsubscribed.
|statistics.bounced	|integer    |A read-only computed property representing the total number of messages that bounced or were otherwise undelivered.
|statistics.spam_reports	|integer    |A read-only computed property representing the total number of messages marked as spam by people receiving them.

_[Back to top...](#)_


### Links

{% include links_intro.md %}

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|self			|[Message*](messages.html)	|A self-referential link to the message.
|creator		|[Person*](people.html)  		|A link to a single Person resource representing the creator of the message.
|modified_by	|[Person* ](people.html) 		|A link to a Person resource representing the last editor of this message.
|queries	|[Queries[]*](queries.html)	|A link to the collection of Query resources that represent who this message was targeted to.
|list	|[List*](lists.html)	|A link to the List resource that represent who this message was sent to.
|wrapper	|[Wrapper*](wrappers.html)	|A link to the Wrapper resource that represent the wrapper that was used when sending this message.
|email_wrapper	|[Email Wrapper*](email_wrappers.html)	|A link to the Email Wrapper resource that represent the email wrapper that was used when sending this message.
|send_helper	|[Send Helper*](send.html)	|A link to the Send Helper resource endpoint for this message.
|schedule_helper	|[Schedule Helper*](schedule.html)	|A link to the Schedule Helper resource endpoint for this message.

_[Back to top...](#)_


## Related Resources

* [Query](queries.html)
* [List](lists.html)
* [Wrapper](wrappers.html)
* [Send Helper](send.html)
* [Schedule Helper](schedule.html)
* [Person](people.html)

_[Back to top...](#)_

## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Message resources (GET)

Message resources are sometimes presented as collections of message. For example, calling the messages endpoint will return a collection of all the messages stored in the system's database associated with your api key.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/messages/

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
            "href": "https://osdi-sample-system.org/api/v1/messages?page=2"
        },
        "osdi:messages": [
            {
                "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/messages/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/messages"
        }
    },
    "_embedded": {
        "osdi:messages": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "GOTV email version 1",
                "subject": "It's time to go vote!",
                "body": "<p>It's time to go vote!</p>",
                "from": "The Committee To Elect Jane Doe",
                "reply_to": "info@janedoe.com",
                "administrative_url": "http://osdi-sample-system.org/emails/gotv-v1/manage",
                "browser_url": "http://osdi-sample-system.org/emails/gotv-v1",
                "type": "email",
                "total_targeted": 14123,
                "status": "sent",
                "sent_start_date": "2015-03-14T12:00:00Z",
                "sent_end_date": "2015-03-14T13:00:00Z",
                "statistics": {
                    "sent": 14123,
                    "opened": 5637,
                    "clicked": 1753,
                    "actions": 253,
                    "forwards": 53,
                    "unsubscribed": 26,
                    "bounced": 58,
                    "spam_reports": 2
                },
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:queries": {
                        "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/queries"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:list": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:wrapper": {
                        "href": "https://osdi-sample-system.org/api/v1/wrappers/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:send_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/send"
                    },
                    "osdi:schedule_helper": {
                        "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/schedule"
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
                "name": "GOTV SMS",
                "body": "Don't forget to vote!",
                "from": "202-123-4567",
                "administrative_url": "http://osdi-sample-system.org/sms/gotv/manage",
                "type": "sms",
                "total_targeted": 2536,
                "status": "scheduled",
                "scheduled_date": "2015-03-14T12:00:00Z",
                "daily_start_hour": 9,
                "daily_stop_hour": 17,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/messages/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:queries": {
                        "href": "https://osdi-sample-system.org/api/v1/messages/1efc3644-af25-4253-90b8-a0baf12dbd1e/queries"
                    },
                    "osdi:creator": {
                        "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
                    },
                    "osdi:modified_by": {
                        "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:list": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/1efc3644-af25-4253-90b8-a0baf12dbd1e"
                    },
                    "osdi:wrapper": {
                        "href": "https://osdi-sample-system.org/api/v1/wrappers/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:send_helper": {
                        "href": "ttps://osdi-sample-system.org/api/v1/messages/1efc3644-af25-4253-90b8-a0baf12dbd1e/send"
                    },
                    "osdi:schedule_helper": {
                        "href": "ttps://osdi-sample-system.org/api/v1/messages/1efc3644-af25-4253-90b8-a0baf12dbd1e/schedule"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Message resource (GET)

Calling an individual Message resource will return the resource directly, along with all associated fields and appropriate links to additional information about the message.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/messages/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

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
    "name": "GOTV email version 1",
    "subject": "It's time to go vote!",
    "body": "<p>It's time to go vote!</p>",
    "from": "The Committee To Elect Jane Doe",
    "reply_to": "info@janedoe.com",
    "administrative_url": "http://osdi-sample-system.org/emails/gotv-v1/manage",
    "browser_url": "http://osdi-sample-system.org/emails/gotv-v1",
    "type": "email",
    "total_targeted": 14123,
    "status": "sent",
    "sent_start_date": "2015-03-14T12:00:00Z",
    "sent_end_date": "2015-03-14T13:00:00Z",
    "statistics": {
        "sent": 14123,
        "opened": 5637,
        "clicked": 1753,
        "actions": 253,
        "forwards": 53,
        "unsubscribed": "26",
        "bounced": 58,
        "spam_reports": 2
    },
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:queries": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/queries"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:list": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:wrapper": {
            "href": "https://osdi-sample-system.org/api/v1/wrappers/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:send_helper": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/send"
        },
        "osdi:schedule_helper": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/schedule"
        }
    }
}    
```

_[Back to top...](#)_


### Scenario: Creating a new message (POST)

Posting to the message collection endpoint will allow you to create a new message. Optionally adding a link to a Person resource will set the creator and adding a link to an Email Wrapper will set up that email wrapper to be used by the message. The response is the new message that was created. While each implementing system will require different fields, any optional fields not included in a post operation should not be set at all by the receiving system, or should be set to default values.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/messages/

Header:
OSDI-API-Token:[your api key here]

{
    "identifiers": [
        "foreign_system:1"
    ],
    "origin_system": "OpenSupporter",
    "name": "GOTV email version 1",
    "subject": "It's time to go vote!",
    "body": "<p>It's time to go vote!</p>",
    "from": "The Committee To Elect Jane Doe",
    "reply_to": "info@janedoe.com",
    "type": "email",
    "_links": {
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:wrapper": {
            "href": "https://osdi-sample-system.org/api/v1/wrappers/c945d6fe-929e-11e3-a2e9-12313d316c29"
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
    "origin_system": "OpenSupporter",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "GOTV email version 1",
    "subject": "It's time to go vote!",
    "body": "<p>It's time to go vote!</p>",
    "from": "The Committee To Elect Jane Doe",
    "reply_to": "info@janedoe.com",
    "type": "email",
    "status": "draft",
    "administrative_url": "http://osdi-sample-system.org/emails/gotv-v1/manage",
    "browser_url": "http://osdi-sample-system.org/emails/gotv-v1",
    "total_targeted": 0,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:queries": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/queries"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:list": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:wrapper": {
            "href": "https://osdi-sample-system.org/api/v1/wrappers/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:send_helper": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/send"
        },
        "osdi:schedule_helper": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/schedule"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Modifying a message (PUT)

You can update a message by calling a PUT operation on that message's endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

{% include array_warning.md %}

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "name": "GOTV email version 2"
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
    "origin_system": "OpenSupporter",
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "name": "GOTV email version 2",
    "subject": "It's time to go vote!",
    "body": "<p>It's time to go vote!</p>",
    "from": "The Committee To Elect Jane Doe",
    "reply_to": "info@janedoe.com",
    "type": "email",
    "status": "draft",
    "administrative_url": "http://osdi-sample-system.org/emails/gotv-v2/manage",
    "browser_url": "http://osdi-sample-system.org/emails/gotv-v2",
    "total_targeted": 0,
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:queries": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/queries"
        },
        "osdi:creator": {
            "href": "https://osdi-sample-system.org/api/v1/people/65345d7d-cd24-466a-a698-4a7686ef684f"
        },
        "osdi:modified_by": {
            "href": "https://osdi-sample-system.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:list": {
            "href": "https://osdi-sample-system.org/api/v1/lists/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:wrapper": {
            "href": "https://osdi-sample-system.org/api/v1/wrappers/c945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:send_helper": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/send"
        },
        "osdi:schedule_helper": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/schedule"
        }
    }
}
```

_[Back to top...](#)_


### Scenario: Adding queries to a message (POST)

You can add queries to a message by POSTing a link to the query to the message's queries collection. This action will typically cause the message's targets to be recalculated by the system, based on the query's parameters.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/queries

Header:
OSDI-API-Token:[your api key here]

{
    "_links": {
        "osdi:queries": {
            "href": "https://osdi-sample-system.org/api/v1/queries/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
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
    "total_pages": 1,
    "per_page": 25,
    "page": 1,
    "total_records": 1,
    "_links": {
        "osdi:queries": [
            {
                "href": "https://osdi-sample-system.org/api/v1/queries/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            }
        ],
        "curies": [
            {
                "name": "osdi",
                "href": "https://osdi-sample-system.org/docs/v1/{rel}",
                "templated": true
            }
        ],
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/queries"
        }
    },
    "_embedded": {
        "osdi:queries": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "name": "GOTV query",
                "browser_url": "http://osdi-sample-system.org/queries/gotv-query",
                "total_results": 26497,
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/queries/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
                    },
                    "osdi:results": {
                        "href": "https://osdi-sample-system.org/api/v1/queries/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/results"
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
```

_[Back to top...](#)_


### Scenario: Deleting a message (DELETE)

You may delete a message by calling the DELETE command on the event's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/messages/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This message was successfully deleted."
}
```

_[Back to top...](#)_