---
layout: default
title: Send Helper
---

# Send Helper

This document defines the Send Helper resource. 

The Send Helper is a helper endpoint that sends a [Message](messages.html) via POST or stops an already sending [Message](messages.html) via DELETE.

The Send Helper POST and DELETE body is empty.

Typically, the response to a successful Send Helper POST or DELETE is a confirmation message and a 200 server code. Some servers may only allow you to send messages after some conditions are met (such as the message has a target list). Errors should be returned if your POST or DELETE is not successful.



### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Sending a Message (POST)](#scenario-sending-a-message-post)
    * [Scenario: Stopping a Message from sending (DELETE)](#scenario-stopping-a-message-from-sending-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for the Send Helper is ```osdi:send_helper```.

_[Back to top...](#)_




## Related Resources

* [Message](messages.html)

_[Back to top...](#)_


## Scenarios

{% include scenarios_helper_intro.md %}


### Scenario: Sending a Message (POST)

Posting to the send helper endpoint with a blank body will allow you to send a message.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/send

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
    "notice": "Your message has been sent."
}
```

_[Back to top...](#)_

### Scenario: Stopping a Message from sending (DELETE)

Sending a DELETE to the send helper endpoint with a blank body will stop the message from sending mid-send, if it hasn't already all gone out.


#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/send

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
    "notice": "Your message has been stopped."
}
```

_[Back to top...](#)_