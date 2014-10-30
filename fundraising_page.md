---
layout: default
title: "Donations"
---

# FundraisingPage
This page defines the resources FundraisingPage

## Fields

| Name          | Type      | Description
|-----------    |-----------|--------------
|identifiers    |Identifier[] |The OSDI identifiers of this page
|created_date	|datetime	|Date and Time of creation
|modified_date	|datetime	|Date and Time of last modification
|origin_system	|string		|Human readable text identifying where this page originated
|name			|string		|The name of the page
|title			|string		|The title of the page
|summary 		|string		|The summary of the page
|description 	|string		|The description of the page
|browser_url	|string	 	|A URL string pointing to the publicly available fundraising page on the web
|total_donations|int		|Computed count of total donations made to the page
|total_revenue	|decimal	|Computed value of total donation revenue made to this page
|currency		|string		|ISO 4217 designation of currency. Example: USD, JPY

## Links

| Name          | Type      | Description
|-----------    |-----------|--------------
|modified_by	|Person*	|The Person who last modified the resource.
|creator		|Person*	|The person representing the creator of the fundraising page
|donations		|Donation[]* |Collection of donations made from this page


# Related Resources

* [Donation](donations.md)
* [Person](people.md)


# Scenarios

## Scenario: Retrieving a fundraising page

### Request

```
GET /fundraising_pages/E15E88FB-36F5-423A-9CEE-E4C7ACF1C92B
```

### Response

```javascript
200 OK
Content-Type: application/hal+json

{
    "identifiers": ["actblue:E15E88FB-36F5-423A-9CEE-E4C7ACF1C92B"],
	"created_date": "2013-04-12T20:44:55",
	"modified_date": "2013-04-12T21:42:34",
	"origin_system": "ActBlue",
	"name": "BobAndFriends",
	"title": "Raise for Bob and his Friends",
	"summary": "Raise for Bob and his friends.",
	"description": "<p>Contribute to Bob and his friends.</p> <p>Contribute today!</p>",
	"browser_url": "htts://actblue.com/page/BobsCandidates",
	"total_donations": 19,
	"total_revenue": 550.00,
	"currency": "USD",
    "_links" : {
        "_self": "/fundraising_pages/E15E88FB-36F5-423A-9CEE-E4C7ACF1C92B",
		"osdi:modified_by": "/people/c8f802c7-29a6-467c-929e-36b7230a77ab"
		"osdi:creator": "/people/55c25b3c-3b31-4bef-8adc-0023cbac20b3"
        "osdi:donations": "/fundraising_pages/E15E88FB-36F5-423A-9CEE-E4C7ACF1C92B/donations"
    }
}
```