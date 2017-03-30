---
layout: default
title: Schedule Helper
---

# Schedule Helper

This document defines the Schedule Helper resource. 

The Schedule Helper is a helper endpoint that schedules a [Message](messages.md) to be sent at a later time via POST or cancels the scheduling via DELETE.

The Schedule Helper POST body contains a datetime field for the time you want to schedule the message to be sent, and the DELETE body is empty.

Typically, the response to a successful Schedule Helper POST or DELETE is a confirmation message and a 200 server code. Some servers may only allow you to schedule messages after some conditions are met (such as the message has a target list). Errors should be returned if your POST or DELETE is not successful.



### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Schedule Helper Fields](#schedule-helper-fields)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Scheduling a Message (POST)](#scenario-scheduling-a-message-post)
    * [Scenario: Canceling a Scheduled Message (DELETE)](#scenario-canceling-a-scheduled-message-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for the Send Helper is ```osdi:schedule_helper```.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}


### Schedule Helper Fields

A list of fields specific for POSTing via the Schedule Helper.

| Name          | Type      | Description
|-----------    |-----------|-----------
|scheduled_start_date		|datetime	|The date and time the message should be scheduled to to start sending text to the targets.
|scheduled_stop_date		|datetime	|The date and time the message is scheduled to be stopped.

_[Back to top...](#)_


## Related Resources

* [Message](messages.md)

_[Back to top...](#)_


## Scenarios

{% include scenarios_helper_intro.md %}


### Scenario: Scheduling a Message (POST)

Posting to the schedule helper endpoint with a blank body will allow you to schedule a message to be sent.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/schedule

Header:
OSDI-API-Token:[your api key here]

{
    "scheduled_start_date": "2015-03-14T12:00:00Z",
    "scheduled_end_date": "2015-03-17T12:00:00Z",
}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "Your message has been scheduled."
}
```

_[Back to top...](#)_

### Scenario: Canceling a Scheduled Message (DELETE)

Sending a DELETE to the schedule helper endpoint with a blank body will cancel the scheduling for the message.


#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/schedule

Header:
OSDI-API-Token:[your api key here]

{}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "Your message scheduling has been canceled."
}
```

_[Back to top...](#)_