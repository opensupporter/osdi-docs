---
layout: default
title: Section Helper
---

# Section Helper

This document defines the Section Helper resource. 

The Section Helper is a helper endpoint that configures a section -- like a pair of keyword and auto response, for a [Message](messages.html).

The Section Helper POST body contains two string fields for the pair of keyword and auto response for the message to be sent, and the DELETE body is empty.

Typically, the response to a successful Schedule Helper POST or DELETE is a confirmation message and a 200 server code. Some servers may only allow you to configure keyword and auto response (or section) for messages after some conditions are met (such as the message has a target list). Errors should be returned if your POST or DELETE is not successful.



### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Schedule Helper Fields](#schedule-helper-fields)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Creating a Section that is added to Message (POST)](#scenario-creating-a-section-message-post)
    * [Scenario: Updating a Section already added to Message (PUT)](#scenario-editing-a-section-message-put)
    * [Scenario: Deleting a Section from the Message (DELETE)](#deleting-a-section-message-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for the Send Helper is ```osdi:section_helper```.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}


### Schedule Helper Fields

A list of fields specific for POSTing via the Schedule Helper.

| Name          | Type      | Description
|-----------    |-----------|-----------
|keyword			|string		|String representing the keyword. Will contain text such as "YES", STOP", "APPLE". (ex: APPLE can possible reply from target to mass communication)
|auto_response		|string		|The content of the message. May contain text and/or HTML. (ex: email type messages will put the HTML content of the email here)

_[Back to top...](#)_


## Related Resources

* [Message](messages.html)

_[Back to top...](#)_


## Scenarios

{% include scenarios_helper_intro.md %}


### Scenario: Creating a Section that is added to Message (POST)

Posting to the section helper endpoint with a blank body will allow you to configure a section for the message to be sent.

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/section

Header:
OSDI-API-Token:[your api key here]

{
    "keyword": "LEMON",
 	"auto_response":    
}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "Your section has been craeted and added to message."
}
```

_[Back to top...](#)_

### Scenario: Updating a Section already added to Message (PUT)

Posting to the section helper endpoint with a blank body will allow you to configure a section for the message to be sent.

#### Request

```javascript
PUT https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/section

Header:
OSDI-API-Token:[your api key here]

{
    "keyword": "LEMON",
 	"auto_response": "Lemon is not a bad choice at all"   
}
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "Your section has been updated and added to message."
}
```

_[Back to top...](#)_

### Scenario: Deleting a Section from the Message (DELETE)

Sending a DELETE to the schedule helper endpoint with a blank body will cancel the scheduling for the message.


#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/messages/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/section

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
    "notice": "Your section has been removed from the message."
}
```

_[Back to top...](#)_