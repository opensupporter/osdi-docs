---
layout: default
title: Person
---

# People

This page defines the Person resource and several related objects: EmailAddress, PhoneNumber, Profile, PostalAddress.

## Person

| Name          | Type      | Description
|-----------    |-----------|--------------
|family_name      |string     |Last name
|given_name     |string     |First name
|additional_name    |string     |An additional name not included in family or given. Usually a middle name.
|honorific_prefix           | string    |An honorific prefix like "Dr", "Mr" etc. Free-form field
|honorific_suffix           | string    |An honorific suffix like "Jr.", "Ph.D" Free-form field
|gender         |string     |The gender binary with which a person most closely identifies, or "Other" if the person identifies with neither. One of "Female", "Male", "Other".
|gender_identity|string     |The self-described gender with which a person identifies. Free-form field. While this field is free-form, data should still follow standardized forms whenever possible (i.e. use "Female" and not "female" or "F"). _Examples: If a person self-identifies as "Female", both_ `gender` _and_ `gender_identity` _fields should have a value of "Female". If a person self-identifies as "Transgender Female",_ `gender` _should have a value of "Female" and_ `gender_identity` _should have a value of "Transgender Female"._
|party_identification_identification          |string     |Flexnum describing the person's politcal party_identification. Values: "None", "Democratic", "Republican", "Independent"
|source         |string     |Information about the source where this person record was acquired.  Eg "Ref74"
|birthdate      |hash       | A hash representing the birth date
|birthdate.month|integer    | integer representing the month of the birth date
|birthdate.day  |integer    | integer representing the day of the birth date
|birthdate.year|integer     | integer representing the 4 digit year of the birth date
|ethnicities|string[]   | An array containing a person's ethinicities
|languages_spoken|string[]      | Unique string array of languages spoken by the person. Values should be two-letter ISO 639 codes. 
|employer|string    |The name of the person's employer
|employer_address|PostalAddress    |The postal address of the person's employer
|occupation|string  |The occupation of the person.
|identifiers    |Identifier[]| A collection of identifiers the provider has determined to be associated with the person
|postal_addresses      |PostalAddress[]  |An array of postal addresses associated with the person
|email_addresses         |EmailAddress[]    |An array of email addresses associated with the person
|phone_numbers         |PhoneNumber[]   |An array of phone numbers associated with the person
|profiles       | Profile[] | An array of profiles for online services
|donations      |Donation[]* |A collection of donations associated with the person
|question_answers|QuestionAnswer[]*|A collection of answers to questions from surveys
|event_attendance |Attendance[]*|A collection of attendance records for a person
|interactions   |Interaction[]*|A collection of outreach interactions for a person, eg Volunteer Joe called voter  Sam F. Bar
|taggings | Tagging[]*|A collection of taggings for a person

# Email Address

| Name          | Type      | Description
|----------------|-----------|----------------
| primary       | boolean   |Denotes if this is the primary address.  A person can have only one primary address
| address       | string    | The actual email address according to RFC822
| address_type  | string    | Flexenum of Personal, Work, Other

# Phone Number

| Name          | Type      | Description
|----------------|-----------|----------------
| primary       | boolean   |Denotes if this is the primary phone number.  A person can have only one primary number
| number        | string    | The actual phone number which MUST including country code and MUST be numeric characters only 
| extension     | string    | Optional associated extension
| description   | string    | Optional Free form additional text description
| number_type   | string    | flexnum of Home, Work, Mobile, Other, Daytime, Evening, Fax
| operator      | string    | Optional: Operator/Carrier associated with number, eg "Verizon"
| country       | string    | Country code according to ISO 3166-1 Alpha-2
| sms_capable   | boolean   | True if the number can accept sms text messages
| do_not_call   | boolean   | True if this number is registered on the US FCC Do Not Call Registry

# Profile

Profiles correspond to a person's accounts on online services like Facebook, Twitter, etc.

| Name          | Type      | Description
|----------------|-----------|----------------
| provider      | string    | The provider name, eg "Facebook"
| id            | string    | The unique identifier provided by the provider, eg "135165"
| url           | string    | The URL to the user's web viewable profile, eg "http://facebook.com/johnqpublic"
| handle        | string    | The handle name, eg "johnqpublic." Twitter handles should not include the "@"


# Custom Fields
Custom fields are arbitrary key/value pairs associated with the person that are created by a user, *not* created by the server or vendor. For example, custom fields are appropriate to store information a user decided to collect on a particular form, like whether the person filling out a form wants to volunteer. They are not appropriate for storing extra information the server or vendor has on this person that doesn't fit into the OSDI spec, such as a person's modeling score. In this way, custom fields are designed to be a more flexible and lightweight version of [Survey Questions and Answers](questions.md).

| Name          | Type      | Description
|----------------|-----------|----------------
| [key]     | string    | The key associated with this custom field, with a corresponding value as a string. May be prefixed by servers based on naming conventions they document to control how collisions across systems and data sets occur.


# Postal Address

| Name          | Type      | Description
|----------------|-----------|----------------
| primary       | boolean   |Denotes if this is the primary address.  A person can have only one primary address
|address_type   |string     |Type of address "Home","Work","Mailing"
|venue | string | Optional venue name at the address, useful for events. (ex: Smith Hall)
|address_lines       |string[]     |Address lines 1 - n
|locality           |string     |A locality or other local administrative area
|region          |string     |region / subdivision codes according to ISO 3166-2 (Final 2 alpha digits)
|postal_code    |string     |Region specific postal code
|country    |string     |Country code according to ISO 3166-1 Alpha-2
|language   |string     |Language in which the address is recorded -- language code according to ISO 639
|location       |hash       | Location information for the address
|.lattitude     |string     |Geolocation latitude
|.longitude     |string     |Geolocation longitude
|.accuracy      |string     |One of "Rooftop", "Approximate"
|status |string     |One of "Potential", "Verified", "Bad".

### Region and Country codes
Country Codes should conform to [ISO 3166-1 Alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

Examples:

|Country        |Code
|---------------|----------------------
|United regions |US
|Canada         |CA
|Cyprus         |CY

In the United regions, region abbreviations should conform to [ISO 3166-2:US](http://en.wikipedia.org/wiki/ISO_3166-2:US) but using only the final two alphanumeric characters

Examples:

|region         |Code
|---------------|----------------------
|New Jersey     |NJ
|California     |CA
|New York       |NY
|Washington     |WA

# Identifier

- Any OSDI entity may generate an identifier to refer to a real person.

- Identifiers are composed of two segments:

        <issuer-id>:<person-id>

    The `issuer-id` must be a unique string that identifies the issuer and has been registered by the issuer with OSDI. Valid characters for `issuer-id` are any printable US-ASCII character other than `:` and `SPACE`. 

    The `person-id` should be a unique string within the namespace of `issuer-id` that identifies the person. Valid characters for `person-id` are any printable US-ASCII character other than `SPACE`.

    _Example: The company "Voter Labs" registers their `issuer-id` as "`voterlabs`" with OSDI. Their internal database id for Jane Doe is `123456`. Jane's OSDI identifier is: `voterlabs:123456`._ 

- Identifiers are __not__ associated with a particular representation of a person record. When a person record is updated, the identifier should not change as a result.

- An OSDI entity __must__ retain any identifiers it previously issued to refer to this person in the `identifiers` collection.

- The `identifiers` collection does not prescribe how an OSDI consumer should utilize the collection for merging or updating their own person records. It's only purpose is to communicate that a real person has been referred to by those identifiers and that the OSDI provider believes those identifiers to all be associated with the same real person.

- Identifiers __must__ be persistent and consumers of a provider's OSDI API should always be able to request a person record by any `identifier` the provider previously used as their canonical `identifier`. If an `identifier` is no longer the canonical `identifier` for the requested person record, the response should be an HTTP 301 redirect to the new record for that real person. The new record should have the new canonical identifier in the `identifier` field and all previously issued identifiers in the `identifiers` collection.

## Merging Records

Determining how, when, and whether two person records should be merged, and then determining which record is more authoritative for each data element of a record is a very difficult task. Automating that process is highly error prone and defining a standard process for merging records goes beyond the scope of OSDI's charter. OSDI is only responsible for establishing a standard for how OSDI entities communicate with each other that they have merged records by whatever internal processes they have defined.

### Example

Voter Labs is a data provider who provides OSDI-formatted data. Voter Labs identifies a new supporter. They create a new person record for this supporter and assign them a new identifier:

__Figure 1.__

    {
        "given_name": "Edwin",
        "family_name": "Labadie"
        "email_addresses": ["edwin.labadie@example.com"],
        "identifiers": [
            "voterlabs:1234"
        ]
    }

Voter Labs also has an existing record in their database that looks like this:

__Figure 2.__

    {
        "given_name": "Edwin",
        "family_name": "Labadie"
        "additional_name": "Marques"
        "email_addresses": ["edwin@example-old.com"],
        "identifiers": [
            "voterlabs:5678"
        ]
    }

Through some internally-defined process, Voter Labs decides the two records represent the same person and should be merged. Also through some internally-defined process, they determine which record should be trusted for which fields and determine which record's identifier is the new canonical identifier. The resulting merged record would look like this:

__Figure 3.__

    {
        "given_name": "Edwin",
        "family_name": "Labadie"
        "additional_name": "Marques"
        "email_addresses": ["edwin.labadie@example.com"],
        "identifiers": [
            "voterlabs:1234",
            "voterlabs:5678"
        ]
    }

What this new record means is that `voterlabs:1234` is the new id by which Voter Labs refers to this real person and that `voterlabs:5678` is another id by which this real person has previously been referred to.

"Jane Doe For Congress" is a consumer of the Voter Labs API. They have a locally cached representation of both records before Voter Labs merged the two records. When "Jane Doe For Congress" requests the record `voterlabs:5678` from the Voter Labs API, they should get a 301 redirect to the newly merged record seen above (Figure 3).

# Scenarios / Examples

> JSON respresenations below are provided as an informative reflection of what the wire format would look like.  
> The tables above are the authoritative specification of the attributes.  Any discrepancy should defer to the above tables.

## Person Signup Helper
The Person Signup Helper provides a simple method for adding a new person to a collection.  It also supports adding tags and list membership info.

The Person Signup helper can be determined in the AEP with the "osdi:person_signup_helper" link relation

The response to a Person Signup Helper is the full representation of the person.

Some initial implementations may only support helpers, direct RESTful access may not be supporter.  In those cases,_links may be omitted in responses.

### Parameters
The Person Signup Helper takes the following parameters in its body
* Inlined Person - A "person" attribute conaining any valid attributes of a person resource are valid in the input representation
* add_tags - a collection of tag names
* add_lists - an array of list names

### Example

#### Request
```
POST /api/v1/person_signup_helper

{
    "person" : {
        "family_name": "Edwin",
        "given_name": "Labadie",
        "additional_name": "Marques",
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
    "add_tags" : [ "volunteer", "donor" ],
    "add_lists" : [ "supporters" ]
}
```

#### Response
    
```
    200 OK

    {
        "family_name": "Edwin",
        "given_name": "Labadie",
        "additional_name": "Marques",
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
        "_embedded" : {
            "osdi:taggings" : { .... }
            "osdi:lists" : { .... }
        }
    }

```


## Get a list of people with pagination

    GET /api/v1/people?per_page=2&page=1

    200 OK
    Content-Type: application/json

    {
        "total_pages": 1,
        "page": 1,
        "total_records": 2,
        "people": [
            {
                "family_name": "Edwin",
                "given_name": "Labadie",
                "additional_name": "Marques",
                "identifiers": [
                    "osdi:23"
                ],
                "email_addresses": [
                    {
                        "address":"test-3@example.com",
                        "primary": true,
                        "address_type": "Personal"
                    }
                ],
                "phone_numbers": [
                    {
                        "primary": true,
                        "number": 19876543210,
                        "number_type": "Mobile",
                        "sms_capable": true
                    }
                ],
                "gender": "Male",
                "gender_identity": "Male",
                "party_identification": "Democrat",
                "source": "sed",
                "ethnicities": ["Caucasian"],
                "profiles": [
                    {
                        "provider": "Twitter",
                        "id": "Edwin_Labadie",
                        "url": "http://twitter.com/Edwin_Labadie",
                        "handle": "Edwin_Labadie"
                     }
                ],
                "birth_date" : {
                    "month" : 1,
                    "day" : 1,
                    "year" : 1970
                },
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
                        "location" : {
                            "longitude" : "40.1",
                            "latitude" : "44.5",
                            "accuracy": "Rooftop"
                        },
                        "status": "Verified"
                    },
                    {
                        "address_lines": [
                             "28160 Wiegand Divide",
                             "Apt 1"
                        ],
                        "locality": "Lake Amarimouth",
                        "region": "GA",
                        "postal_code": "27585-7257",
                        "country": "US",
                        "address_type": "Work",
                        "location" : {
                            "longitude" : "40.1",
                            "latitude" : "44.5",
                            "accuracy": "Rooftop"
                        },
                        "status": "Verified",
                        "primary": false
                    }
                ],
                "_links": {
                    "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
                    "osdi:question_answers": {
                        "href": "http://osdi-prototype.herokuapp.com/api/v1/people/23/question_answers"
                    },
                    "self": {
                        "href": "http://osdi-prototype.herokuapp.com/api/v1/people/23"
                    }
                }
            },
            {
                "family_name": "Parker",
                "given_name": "Walker",
                "additional_name": "Jannie",
                "identifiers": [
                    "osdi:24"
                ],
                "email_addresses": [
                    {
                        "address":"test-4@example.com",
                        "primary": true,
                        "address_type": "Work"
                    }
                ],
                "gender": "Male",
                "gender_identity": "Male",
                "party_identification": "Democrat",
                "source": "architecto",
                "ethnicities": ["African American", "Hispanic"],
                "profiles": [
                    {
                        "provider": "Twitter",
                        "id": "Parker_Walker",
                        "url": "http://twitter.com/Parker_Walker",
                        "handle": "Parker_Walker"
                    }
                ],
                "birth_date" : {
                    "month" : 1,
                    "day" : 1,
                    "year" : 1970
                },
                "postal_addresses": [
                    {
                        "primary": true,
                        "address_lines": [
                            "22184 Vernie Cove",
                            "Apt 1"
                        ],
                        "locality": "Rowemouth",
                        "region": "JP",
                        "postal_code": "74895",
                        "country": "RU",
                        "address_type": "Home",
                        "location" : {
                            "longitude" : "40.1",
                            "latitude" : "44.5",
                            "accuracy": "Rooftop"
                        },
                        "status": "Verified"
                    },
                    {
                        "address_lines": [
                            "7485 Rashad Pine"
                        ],
                        "locality": "Brandynview",
                        "region": "PR",
                        "postal_code": "76221-3163",
                        "country": "US",
                        "address_type": "Work",
                        "location" : {
                            "longitude" : "40.1",
                            "latitude" : "44.5",
                            "accuracy": "Rooftop"
                        },
                        "status": "Verified",
                        "primary": false
                    }
                ],
                "_links": {
                     "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
                     "osdi:question_answers": {
                        "href": "http://osdi-prototype.herokuapp.com/api/v1/people/24/question_answers"
                     },
                     "self": {
                        "href": "http://osdi-prototype.herokuapp.com/api/v1/people/24"
                     }
                }
            }
        ],
        "osdi:taggings": [
              {
                "added_at":"2014-03-01 00:00:00",
                "tag":
                  {
                    "name":"labor",
                    "description":"this person is a labor supporter",
                    "created_at":"2014-01-01 00:00:00",
                    "modified_at":"2014-02-28 11:23:23",
                    "originating_system":"Voter Labs",
                    "_links" : {
                      "items" : {
                        "href" : "api/v1/people/tag/labor",
                      }
                    }
                  }
                },
                {
                  "added_at":"2014-03-01 00:00:00",
                  "tag":
                  {
                    "name":"reproductive-rights",
                    "description":"this person supports a right to reproductive choice",
                    "description":"this person supports a right to reproductive choice",
                    "created_at":"2014-01-01 00:00:00",
                    "modified_at":"2014-02-28 11:23:23",
                    "originating_system":"Voter Labs",
                    "_links" : {
                      "items" : {
                        "href" : "api/v1/people/tag/reproductive-rights"
                      }
                    }
                  }
                }
              ],
            },
        "_links": {
            "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
            "self": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people"
            },
            "osdi:question_answers": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/question_answers"
            },
            "osdi:find": {
                "href": "http://api.opensupporter.org/api/v1/people?$filter={odata_query}",
                "templated": true
            }
        }
    }
