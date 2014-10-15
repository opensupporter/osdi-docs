---
layout: default
title: Person
---

# People

This document defines the Person resource. 

People are individual users who are stored in the OSDI system's database in some way.

People have names, email addresses, and other information, and they have associated action histories recording the actions they've taken on the system, such as a list of their signatures on various petitions.


### Sections:

* Endpoints and URL structures
* Field names and descriptions
* Links
* Scenario: Retrieving a collection of person resources (GET)
* Scenario: Retrieving an individual person resource (GET)
* Scenario: Creating a new person (POST)
* Scenario: Modifying a person (PUT)
* Scenario: Deleting a person (DELETE)

## Endpoints and URL structures

While OSDI does not specify specific endpoints and link structures for compliant systems to use, commonly used conventions are shown below. The links section of each resource or collection, described more fully below, should be your cononical source for the exact URLs pointing to specific other resources or collections.

**Endpoints:**

`https://osdi-sample-system.org/api/v1/people`

People resources live exclusively at the above endpoint. The endpoint returns a collection of all the people in the OSDI system's database associated with the given API key.

**URL Structures:**

`https://osdi-sample-system.org/api/v1/people/[id]`

To address a specific person, use their identifier without the system prefix to construct a URL, like https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3


## Field names and descriptions

The field names for a person, with standard names, punctuation and capitalization, and values where appropriate. 

**Note:** As with the entire OSDI specification, the specific fields a compliant system implements will vary between each system, as will the fields each system requires when creating or updating resources, which fields are writeable, and the operations you are allowed to perform on each resource.


|Name          |Type      |Description
|-----------    |-----------|--------------
|identifiers	|array[]	|A unique string array of identifiers in the format `[system name]:[id]`. See the general concepts document for more information about identifiers.
|origin_system	|string		|A human readable string identifying where this person originated. May be used in the user interface for this purpose.
|created_date	|datetime	|The date and time the resource was created on the local system.
|modified_date	|datetime	|The date and time the resource was last modified on the local system.
|modified_by	|osdi:person	|An embedded person resource representing the last editor of this person resource.
|family_name      |string     |The person's last name.
|given_name     |string     |The person's first name.
|additional_name    |string     |An additional name not included in family or given. Usually a middle name.
|honorific_prefix           |string    |An honorific prefix like "Dr", "Mr", etc...
|honorific_suffix           |string    |An honorific suffix like "Jr.", "Ph.D", etc...
|gender         |enum     |The gender binary with which a person most closely identifies, or "Other" if the person identifies with neither. One of "Female", "Male", or "Other".
|gender_identity|string     |The self-described gender with which a person identifies. While this field is free-form, data should still follow standardized forms whenever possible (i.e. use "Female" and not "female" or "F"). _Examples: If a person self-identifies as "Female", both_ `gender` _and_ `gender_identity` _fields should have a value of "Female". If a person self-identifies as "Transgender Female",_ `gender` _should have a value of "Female" and_ `gender_identity` _should have a value of "Transgender Female"._
|party_identification          |flexenum     |Flexenum describing the person's politcal party_identification. One of "None", "Democratic", "Republican", "Independent", or another free-form string.
|source         |string     |Information about the source where this person record was acquired.   _Example: "facebook-ad-october"_
|birthdate      |hash       |A hash representing the birth date of the person.
|birthdate.month|integer    |An integer representing the month of the birth date of the person.
|birthdate.day  |integer    |An integer representing the day of the birth date of the person.
|birthdate.year|integer     |An integer representing the 4 digit year of the birth date of the person.
|ethnicities|array[]   |A unique string array representing a person's ethinicities.
|languages_spoken|array[]      | Unique string array of languages spoken by the person. Values should be two-letter ISO 639 codes. 
|employer|string    |The name of the person's employer.
|employer_address|hash    |A hash representing the postal address of the person's employer.
|employer_address.venue	|string	|Optional venue name at the employer address, useful for names of buildings. (ex: Smith Hall)
|employer_address.address_lines	|array[]	|An array of strings representing the employer's street address.
|employer_address.locality	|string	|A city or other local administrative area.
|employer_address.region	|string	|State or subdivision codes according to ISO 3166-2 (Final 2 alpha digits).
|employer_address.postal_code	|string	|The region specific postal code, such as a zip code.
|employer_address.country	|string	|The country code according to ISO 3166-1 Alpha-2.
|employer_address.language	|string	|Language in which the address is recorded -- language code according to ISO 639.
|employer_address.location	|hash	|A hash representing the geocoded location information for the address.
|employer_address.location.latitude	|float	|A positive or negative float number representing the latitude of the address.
|employer_address.location.longitude	|float	|A positive or negative float number representing the longitude of the address.
|employer_address.location.accuracy	|enum	|A value representing the accuracy of the geocode. One of "Rooftop" or "Approximate".
|employer_address.status	|enum	|A value representing the status of the address. One of "Potential", "Verified", or "Bad".
|occupation	|string  |The occupation of the person.
|postal_addresses      |array[]  |An array of postal address hashes associated with the person.
|postal_addresses.primary	|boolean	|Denotes if this is the primary address. A person can have only one primary address.
|postal_addresses.address_type	|enum	|The type of address. One of "Home", "Work", or "Mailing".
|postal_addresses.venue	|string	|Optional venue name at the address, useful for names of buildings. (ex: Smith Hall)
|postal_addresses.address_lines	|array[]	|An array of strings representing the person's street address.
|postal_addresses.locality	|string	|A city or other local administrative area.
|postal_addresses.region	|string	|State or subdivision codes according to ISO 3166-2 (Final 2 alpha digits).
|postal_addresses.postal_code	|string	|The region specific postal code, such as a zip code.
|postal_addresses.country	|string	|The country code according to ISO 3166-1 Alpha-2.
|postal_addresses.language	|string	|Language in which the address is recorded -- language code according to ISO 639.
|postal_addresses.location	|hash	|A hash representing the geocoded location information for the address.
|postal_addresses.location.latitude	|float	|A positive or negative float number representing the latitude of the address.
|postal_addresses.location.longitude	|float	|A positive or negative float number representing the longitude of the address.
|postal_addresses.location.accuracy	|enum	|A value representing the accuracy of the geocode. One of "Rooftop" or "Approximate".
|postal_addresses.status	|enum	|A value representing the status of the address. One of "Potential", "Verified", or "Bad".
|email_addresses	|array[]    |An array of email address hashes associated with the person.
|email_addresses.primary	|boolean	|Denotes if this is the primary address. A person can have only one primary address.
|email_addresses.address	|string	|The email address for the person.
|email_addresses.address_type	|flexenum	|The type of email address. One of "Personal", "Work", "Other", or another value.
|phone_numbers	|array[]   |An array of phone number hashes associated with the person.
|phone_numbers.primary	|string   |Denotes if this is the primary phone number. A person can have only one primary number.
|phone_numbers.number	|string   |The phone number of the person. Must including country code and must be numeric characters only.
|phone_numbers.extension	|string   |An optional associated extension for the number.
|phone_numbers.description	|string   |A freeform description of the phone number.
|phone_numbers.number_type	|flexenum   |The type of phone number. One of "Home", "Work", "Mobile", "Other", "Daytime", "Evening", "Fax", or another value.
|phone_numbers.operator	|string   |The operator or carrier associated with the number. _Example: "Verizon"_
|phone_numbers.country	|string   |The country code according to ISO 3166-1 Alpha-2.
|phone_numbers.sms_capable	|boolean   |True if the number can accept SMS text messages.
|phone_numbers.do_not_call	|boolean   |True if this number is registered on the US FCC Do Not Call Registry.
|profiles       | array[] |An array of profile hashes for online services related to the person.
|profiles.provider       | string |The provider name of the profile. _Example: "Facebook"_
|profiles.id       | string |The unique identifier provided by the provider for the profile. _Example: "135165"_
|profiles.url       | string |The URL to the person's web viewable profile. _Example: "http://facebook.com/john.doe"_
|profiles.handle       | string |The handle name of the profile. Twitter handles should not include the "@" _Example: "johndoe"_
|custom_fields	|hash	|A hash of key/value pairs associated with the person created by a user rather than a service or vendor.
|custom_fields.[key]	|string	|The key associated with this custom field, with a corresponding value as a string. May be prefixed by servers based on naming conventions they document to control how collisions across systems and data sets occur.

## Links

The links associated with this person, available in the links section of the resource. 

**Note:** As with the entire OSDI specification, the specific links a compliant system supplies will vary between each system. In addition, systems may choose to embed a linked resource directly in the response in addition to linking to it in the links section, using the standard `_embedded` syntax described in the general overview documentation.

|Name          |Description
|-----------   	|--------------

|donations      |A link to the collection of donations associated with the person.
|submissions      |A link to the collection of form submissions associated with the person.
|attendance      |A link to the collection of event attendances associated with the person.
|signatures      |A link to the collection of petition signatures associated with the person.
|question_answers	|A link to the collection of answers to questions associated with the person.
|taggings 	|A link to the collection of taggins associated with the person.


## Scenario: Retrieving a collection of person resources (GET)

Person resources are sometimes presented as collections of people. For example, calling the people endpoint will return a collection of all the people stored in the system's database associated with your api key.

**Request**

```javascript
GET https://osdi-sample-system.org/api/v1/people/

Header:
OSDI-API-Token:[your api key here]
```

**Response**

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "total_pages": 88,
  "per_page": 25,
  "page": 1,
  "total_records": 2188,
  "_links": {
    "next": {
      "href": "https://osdi-sample-system.org/api/v1/people?page=2"
    },
    "osdi:people": [
      {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
      },
      {
        "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e"
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
      "href": "https://osdi-sample-system.org/api/v1/people"
    }
  },
  "_embedded": {
    "osdi:people": [
      {
	    "identifiers": [
          "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3",
          "foreign_system:1"
        ],
        "origin_system": "OSDI Sample System",
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
        "source": "october_canvass",
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
            "address_type": "Personal"
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
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
          },
          "osdi:question_answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/question_answers"
          },
          "osdi:attendance": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendance"
          },
          "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
          },
          "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
          },
          "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
          },
          "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
          }
        }
      },
      {
        "given_name": "Jane",
        "family_name": "Doe",
        "identifiers": [
          "osdi_sample_system:1efc3644-af25-4253-90b8-a0baf12dbd1e"
        ],
        "origin_system": "OSDI Sample System",
        "created_date": "2014-03-20T20:44:13Z",
        "modified_date": "2014-03-20T20:44:13Z",
        "email_addresses": [
          {
            "primary": true,
            "address": "janedoe@mail.com"
          }
        ],
        "postal_addresses": [
          {
            "primary": true,
            "locality": "Washington",
            "region": "DC",
            "postal_code": "20009",
            "country": "US",
            "language": "en",
            "location": {
              "latitude": 38.919,
              "longitude": -77.0379,
              "accuracy": "Approximate"
            }
          }
        ],
        "_links": {
          "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e"
          },
          "osdi:question_answers": {
            "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/question_answers"
          },
          "osdi:attendance": {
            "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/attendance"
          },
          "osdi:signatures": {
            "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/signatures"
          },
          "osdi:submissions": {
            "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/submissions"
          },
          "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/donations"
          },
          "osdi:taggings": {
            "href": "https://osdi-sample-system.org/api/v1/people/1efc3644-af25-4253-90b8-a0baf12dbd1e/taggings"
          }
        }
      },
      //(truncated for brevity)
    ]
  }
}
```			

## Scenario: Scenario: Retrieving an individual person resource (GET)

Calling an individual person resource will return the resource directly, along with all associated fields and appropriate links to additional information about the person.

**Request**

```javascript
GET https://osdi-sample-system.org/api/v1/people/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

**Response**

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
  "given_name": "John",
  "family_name": "Smith",
  "honorific_prefix": "Mr.",
  "honorific_suffix": "Ph.D",
  "additional_name": "Scott",
  "gender": "Male",
  "gender_identity": "Male",
  "party_identification": "Democratic",
  "source": "october_canvass",
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
      "address_type": "Personal"
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
      "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
    },
    "osdi:question_answers": {
      "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/question_answers"
    },
    "osdi:attendance": {
      "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendance"
    },
    "osdi:signatures": {
      "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/signatures"
    },
    "osdi:submissions": {
      "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/submissions"
    },
    "osdi:donations": {
      "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
    },
    "osdi:donations": {
      "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/taggings"
    }
  }
}
```

## Scenario: Creating a new person (POST)

You can create a new person directly by posting to the person signup helper endpoint defined on the AEP and potentially in other places. Systems may also allow you to create new people by posting an action they've taken either on an existing action resource or a new one you create with the API. See the documentation describing each action type (petitions, events, forms, fundraising pages) and each individual action record (signatures, attendance, submissions, donations) for details.

The person signup helper provides a simple method for adding a new person to a collection. It also supports adding tags and list membership info.

The response to a person signup helper post is the full representation of the person that was created.

Some initial implementations may only support helpers, direct RESTful access may not be supported. In those cases, the _links section may be omitted in responses.

When you post to the person signup helper, include a person hash describing the person with the spec defined above, and arrays of strings corresponding to the tags and lists you want to add in the "add_tags" and "add_lists" arrays.

**Request**

```javascript
POST https://osdi-sample-system.org/api/v1/people/person_signup_helper

Header:
OSDI-API-Token:[your api key here]

{
    "person" : {
        "family_name": "Edwin",
        "given_name": "Labadie",
        "additional_name": "Marques",
        "origin_system": "OpenSupporter",
        "email_addresses": [
            {
                "address":"test-3@example.com",
                "primary": true,
                "address_type": "Personal"
            }
        ],
        "postal_addresses": [
            {
                "primary": true,
                "address_lines": [
                    "935 Ed Lock"
                ],
                "locality": "New Dudley",
                "region": "MN",
                "postal_code": "17678",
                "country": "RU",
                "address_type": "Home",
                "status": "Verified"
            },
        "phone_numbers": [
            {
                "primary": true,
                "number": 19876543210,
                "number_type": "Mobile",
                "sms_capable": true
            }
        ],
        "gender": "Male"
    }
    "add_tags" : [ 
    	"edsiek24d", 
    	"834kjd8830d" 
    ],
    "add_lists" : [ 
    	"uejd7623dd" 
    ]
}

```

**Response**

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
      "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "family_name": "Edwin",
    "given_name": "Labadie",
    "additional_name": "Marques",
    "origin_system": "OpenSupporter",
    "email_addresses": [
        {
            "address":"test-3@example.com",
            "primary": true,
            "address_type": "Personal"
        }
    ],
    "postal_addresses": [
        {
            "primary": true,
            "address_lines": [
                "935 Ed Lock"
            ],
            "locality": "New Dudley",
            "region": "MN",
            "postal_code": "17678",
            "country": "RU",
            "address_type": "Home",
            "status": "Verified"
        },
    "phone_numbers": [
        {
            "primary": true,
            "number": 19876543210,
            "number_type": "Mobile",
            "sms_capable": true
        }
    ],
    "gender": "Male",
    "_links": {
      "self": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
      },
      "osdi:question_answers": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/question_answers"
      },
      "osdi:attendance": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/attendance"
      },
      "osdi:signatures": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/signatures"
      },
      "osdi:submissions": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/submissions"
      },
      "osdi:donations": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/donations"
      },
      "osdi:donations": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/taggings"
      }
    }
}
```

## Scenario: Modifying a person (PUT)

You can updating a person by calling a PUT operation on that person's resource endpoint. Your PUT should contain fields that you want to update. Missing fields will be ignored by the receiving system. Systems may also ignore PUT values, depending on whether fields you are trying to modify are read-only or not. You may set an attribute to nil by including the attribute using `nil` for value.

**Note:** Modifying members of an array separately is not supported. To change the contents of an array, first GET the current contents and then PUT back only those you wish to keep.

**Request**

```javascript
PUT https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse

Header:
OSDI-API-Token:[your api key here]

{
    "family_name": "Ed",
    "email_addresses": [
        {
            "address":"test-new@example.com",
            "primary": true,
            "address_type": "Personal"
        }
    ]
}

```

**Response**
```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
      "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-de9uemdse",
    ],
    "created_date": "2014-03-20T21:04:31Z",
    "modified_date": "2014-03-20T21:04:31Z",
    "family_name": "Ed",
    "given_name": "Labadie",
    "additional_name": "Marques",
    "origin_system": "OpenSupporter",
    "email_addresses": [
        {
            "address":"test-new@example.com",
            "primary": true,
            "address_type": "Personal"
        }
    ],
    "postal_addresses": [
        {
            "primary": true,
            "address_lines": [
                "935 Ed Lock"
            ],
            "locality": "New Dudley",
            "region": "MN",
            "postal_code": "17678",
            "country": "RU",
            "address_type": "Home",
            "status": "Verified"
        },
    "phone_numbers": [
        {
            "primary": true,
            "number": 19876543210,
            "number_type": "Mobile",
            "sms_capable": true
        }
    ],
    "gender": "Male",
    "_links": {
      "self": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse"
      },
      "osdi:question_answers": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/question_answers"
      },
      "osdi:attendance": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/attendance"
      },
      "osdi:signatures": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/signatures"
      },
      "osdi:submissions": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/submissions"
      },
      "osdi:donations": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/donations"
      },
      "osdi:donations": {
        "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-de9uemdse/taggings"
      }
    }
}
```


## Scenario: Deleting a person (DELETE)

You may delete a person by calling the DELETE command on the person resource's endpoint.

**Request**

```javascript
DELETE https://osdi-sample-system.org/api/v1/people/d32fcdd6-7366-466d-a3b8-7e0d87c3cd8b

Header:
OSDI-API-Token:[your api key here]
```

**Response**

```javascript
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
  "notice": "This user was successfully deleted."
}
```