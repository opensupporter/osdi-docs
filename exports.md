---
layout: default
title: "ExportJobs"
---

# Export

This document defines the Export resource. 

Export resources are export jobs used to create downloadable file exports of lists and queries such as csv and tsv.  To have an export job created, an Export resource is created.  

Once created, the export workflow starts.  This workflow will proceed through states initializing, pending administrator approval, processing, and ready.  

Once created, a client may poll the status with GET requests and examining the status field.

When an export is ready, a link to a downloadable file is included in the export resource.

Once downloaded, or after a period of time, the export may have the status of expired, and is thus no longer active and the download file may be removed.

### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [Export Fields](#export-fields)  
    * [Links](#links)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Export resources (GET)](#scenario-retrieving-a-collection-of-export-resources-get)
    * [Scenario: Retrieving an individual Export resource (GET)](#scenario-scenario-retrieving-an-individual-export-job-get)
    * [Scenario: Creating a new export (POST)](#scenario-creating-a-new-export-post)
    * [Scenario: Modifying an export (PUT)](#scenario-modifying-an-export-put)
    * [Scenario: Deleting an export (DELETE)](#scenario-deleting-an-export-delete)

{% include endpoints_and_url_structures.md %}

The link relation label for a export resource is ```osdi:export``` for a single export resource or ```osdi:exports``` for a collection of export resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


## Export Fields

| Name          | Type      | Description
|-----------    |-----------|--------------
|origin_system	|string		| Human readable text identifying the system where this resource was created.
|action_date    |datetime   | Date the export was requested made.
|approved_date	|datetime	| Date the export was approved
|processed_date	|datetime	| Date the export completed processing
|name			|string		| A name for the export eg "People who love us"
|status			|Flexenum	| [ initalizing, pending_approval, rejected, queued, processing, ready, expired	]	|
|detail         | string | A string with additional details regarding the status
|download_link | string | A URL pointing to a file download such as csv
| export_template  | flexenum | A string representing the template name to be used when creating the exported file.  The template is assumed to specify which columns will be included and the file type (zip,csv,tsv)


## Links

| Name          | Type      | Description
|-----------    |-----------|--------------
|self			|[Export*](exports.html)	|A self-referential link to the export.
|resource		|Any OSDI*	| A link to the resource being exported such as a list or query


## Related Resources

* [Lists](lists.html)
* [Queries](queries.html)


## Scenarios

{% include scenarios_intro.md %}

### Scenario: Retrieving a collection of Export resources (GET)

The set of available export jobs on the system.

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/exports

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
            "href": "https://osdi-sample-system.org/api/v1/exports?page=2"
        },
        "osdi:exports": [
            {
                "href": "https://osdi-sample-system.org/api/v1/exports/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
            },
            {
                "href": "https://osdi-sample-system.org/api/v1/exports/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
            "href": "https://osdi-sample-system.org/api/v1/exports/c945d6fe-929e-11e3-a2e9-12313d316c29/exports"
        }
    },
    "_embedded": {
        "osdi:exports": [
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "action_date": "2014-03-18T11:02:15Z",
                "approved_date" :"2014-03-18T11:02:15Z",
                "processed_date" : "2014-03-18T11:02:15Z",
                "name" : "People who love us export"m
                "status" : "ready",
                "download_link" : "https://osdi-sample-system.org/downloads/jdiejdjdiejd.csv",
                "export_template" : "my_template_tsv",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/exports/c945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:resource": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/45d6fe-929e-11e3-a2e9-12313d316c29"
                    }
                }
            },
            {
                "identifiers": [
                    "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
                    "foreign_system:1"
                ],
                "origin_system": "OSDI Sample System",
                "created_date": "2014-03-20T21:04:31Z",
                "modified_date": "2014-03-20T21:04:31Z",
                "action_date": "2014-03-18T11:02:15Z",
                "name" : "Likely Hipsters export",
                "status" : "pending_approval",
                "export_template" : "my_template_tsv",
                "_links": {
                    "self": {
                        "href": "https://osdi-sample-system.org/api/v1/exports/d945d6fe-929e-11e3-a2e9-12313d316c29"
                    },
                    "osdi:resource": {
                        "href": "https://osdi-sample-system.org/api/v1/lists/45d6fe-929e-11e3-a2e9-12313d316c29"
                    }
                }
            },
            //(truncated for brevity)
        ]
    }
}
```	

_[Back to top...](#)_		

### Scenario: Scenario: Retrieving an individual Export Job (GET)

#### Request

```javascript
GET https://osdi-sample-system.org/api/v1/exports/d945d6fe-929e-11e3-a2e9-12313d316c29

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
    "action_date": "2014-03-18T11:02:15Z",
    "name" : "Likely Hipsters export",
    "status" : "rejected",
    "detail" : "Please ride your fixie to  campaign security, you are fired!",
    "export_template" : "my_template_tsv",
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/exports/d945d6fe-929e-11e3-a2e9-12313d316c29"
        },
        "osdi:resource": {
            "href": "https://osdi-sample-system.org/api/v1/lists/45d6fe-929e-11e3-a2e9-12313d316c29"
        }
    }
}

```

_[Back to top...](#)_


### Scenario: Creating a new Export (POST)

#### Request

```javascript
POST https://osdi-sample-system.org/api/v1/exports

Header:
OSDI-API-Token:[your api key here]

{
    "export_template" : "my_template_tsv",
    "name" : "People who love us",
    "_links" : {
        "osdi:resource" : {
            "href" : "https://osdi-sample-system.org/api/v1/lists/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        }
        
    }
 }

```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate


```

_[Back to top...](#)_


### Scenario: Modifying an Export (PUT)

Modifying an existing Export is not supported.  It may be DELETED (cancelled)

{% include array_warning.md %}

#### Not Supported

_[Back to top...](#)_


### Scenario: Deleting an Export (DELETE)

You may delete an export by calling the DELETE command on the export's endpoint.

#### Request

```javascript
DELETE https://osdi-sample-system.org/api/v1/exports/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]
```

#### Response

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "notice": "This export was successfully deleted."
}
```

_[Back to top...](#)_