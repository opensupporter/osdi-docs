# Person
## Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
|family_name      |string     |Last name
|given_name     |string     |First name
|additional_name	|string     |An additional name not included in family or given. Usually a middle name.
|honorific_prefix			| string	|An honorific prefix like "Dr", "Mr" etc. Free-form field
|honorific_suffix			| string	|An honorific suffix like "Jr.", "Ph.D" Free-form field
|gender			|string		|The gender binary with which a person most closely identifies, or "Other" if the person identifies with neither. One of "Female", "Male", "Other".
|gender_identity|string     |The self-described gender with which a person identifies. Free-form field. While this field is free-form, data should still follow standardized forms whenever possible (i.e. use "Female" and not "female" or "F"). _Examples: If a person self-identifies as "Female", both_ `gender` _and_ `gender_identity` _fields should have a value of "Female". If a person self-identifies as "Transgender Female",_ `gender` _should have a value of "Female" and_ `gender_identity` _should have a value of "Transgender Female"._
|party_identification          |string     |Flexnum describing the person's politcal party. Values: "None", "Democratic", "Republican", "Independent"
|source         |string     |Information about the source where this person record was acquired.  Eg "Ref74"
|birthdate		|hash		| A hash representing the birth date
|birthdate.month|integer	| integer representing the month of the birth date
|birthdate.day	|integer	| integer representing the day of the birth date
|birthdate.year|integer		| integer representing the 4 digit year of the birth date
|ethnicity|string	|A person's ethinicity
|languages_spoken|string[]      | Unique string array of languages spoken by the person. Values should be two-letter ISO 639 codes. 
|employer|string	|The name of the person's employer
|occupation|string	|The occupation of the person.
|identifiers    |Identifier[]| A collection of identifiers the provider has determined to be associated with the person
|postal_addresses      |PostalAddress[]  |A collection of postal addresses associated with the person
|email_addresses         |EmailAddress[]    |A collection of email addresses associated with the person
|phone_numbers         |PhoneNumber[]	|A collection of phone numbers associated with the person
|profiles		| Profile[]	| A collection of profiles for online services
|custom_fields		| CustomFields[]	| A collection of user-created key/value pairs associated with the person

## Resource Collections (post developer preview)
| Name          | Type      | Description
|-----------    |-----------|--------------
|donations      |Donation[] |A collection of donations associated with the person
|question_answers|QuestionAnswer[]|A collection of answers to questions from surveys
|event_attendance |Attendance[]|A collection of attendance records for a person
|interactions   |Interaction[]|A collection of outreach interactions for a person, eg Volunteer Joe called voter Sam F. Bar


# Email Address
| Name          | Type      | Description
|----------------|-----------|----------------
| primary		| boolean	|Denotes if this is the primary address.  A person can have only one primary address
| address		| string	| The actual email address according to RFC822
| address_type	| string	| Flexenum of Personal, Work, Other

# Phone Number
| Name          | Type      | Description
|----------------|-----------|----------------
| primary		| boolean	|Denotes if this is the primary phone number.  A person can have only one primary number
| number		| string	| The actual phone number which MUST including country code and MUST be numeric characters only 
| extension		| string	| Optional associated extension
| description	| string	| Optional Free form additional text description
| number_type	| string	| flexnum of Home, Work, Mobile, Other, Daytime, Evening, Fax
| operator		| string	| Optional: Operator/Carrier associated with number, eg "Verizon"
| country		| string	| Country code according to ISO 3166-1 Alpha-2
| sms_capable	| boolean	| True if the number can accept sms text messages
| do_not_call	| boolean	| True if this number is registered on the US FCC Do Not Call Registry

# Profile
Profiles correspond to a person's accounts on online services like Facebook, Twitter, etc.

| Name          | Type      | Description
|----------------|-----------|----------------
| provider		| string	| The provider name, eg "Facebook"
| id			| string	| The unique identifier provided by the provider, eg "135165"
| url			| string	| The URL to the user's web viewable profile, eg "http://facebook.com/johnqpublic"
| handle		| string	| The handle name, eg "johnqpublic." Twitter handles should not include the "@"


# Custom Fields
Custom fields are arbitrary key/value pairs associated with the person that are created by a user, *not* created by the server or vendor. For example, custom fields are appropriate to store information a user decided to collect on a particular form, like whether the person filling out a form wants to volunteer. They are not appropriate for storing extra information the server or vendor has on this person that doesn't fit into the OSDI spec, such as a person's modeling score. In this way, custom fields are designed to be a more flexible and lightweight version of [Survey Questions and Answers](questions.md).

| Name          | Type      | Description
|----------------|-----------|----------------
| [key]		| string	| The key associated with this custom field, with a corresponding value as a string. May be prefixed by servers based on naming conventions they document to control how collisions across systems and data sets occur.


# Postal Address
## Attributes

| Name          | Type      | Description
|----------------|-----------|----------------
| primary		| boolean	|Denotes if this is the primary address.  A person can have only one primary address
|address_type   |string     |Type of address "Home","Work","Mailing"
|address_lines       |string[]     |Address lines 1 - n
|locality           |string     |A city or other local administrative area
|region          |string     |State / subdivision codes according to ISO 3166-2 (Final 2 alpha digits)
|postal_code    |string     |Region specific postal code
|country	|string		|Country code according to ISO 3166-1 Alpha-2
|language	|string		|Language in which the address is recorder -- language code according to ISO 639
|location		|hash		| Location information for the address
|.lattitude		|string		|Geolocation latitude
|.longitude		|string		|Geolocation longitude
|.accuracy		|string		|One of "Rooftop", "Approximate"
|status	|string		|One of "Potential", "Verified", "Bad".

### Region and Country codes
Country Codes should conform to [ISO 3166-1 Alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

Examples:

|Country		|Code
|---------------|----------------------
|United States	|US
|Canada			|CA
|Cyprus			|CY

In the United States, state abbreviations should conform to [ISO 3166-2:US](http://en.wikipedia.org/wiki/ISO_3166-2:US) but using only the final two alphanumeric characters

Examples:

|State			|Code
|---------------|----------------------
|New Jersey		|NJ
|California		|CA
|New York		|NY
|Washington		|WA

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

## Get a list of people with pagination

    GET /api/v1/people?per_page=2&page=1

    200 OK
    Content-Type: application/json

    {
      "total_pages": 1,
      "page": 1,
      "total_records": 2,
      "_embedded": {
        "people": [
          {
            "first_name": "Edwin",
            "last_name": "Labadie",
            "middle_name": "Marques",
            "email": "test-3@example.com",
            "gender": "Male",
            "gender_identity": "Male",
            "party": "Democrat",
            "source": "sed",
            "source_details": "Delectus rerum autem mollitia sit asperiores odit hic cum.",
            "twitter_handle": "@Edwin_Labadie",
            "custom_fields": {
	            "volunteer": "true",
	            "team_captain": "true",
	            "suppression_list": "1"
            },
            "guid": "c1d9c510-b562-0130-dc7c-168c51e904de",
			"birth_date" : {
				"month" : 1,
				"day" : 1,
				"year" : 1970
				},
            "_embedded": {
              "osdi:primary_address": {
                "address1": "935 Ed Lock",
                "city": "New Dudley",
                "state": "MN",
                "postal_code": "17678",
                "country_code": "RU",
                "address_type": "Home",
                "location" : {
             		"longitude" : "40.1",
             		"latitude" : "44.5"4,
             		"accuracy": "Rooftop"
             		},
                "address_status": "Verified",
                "primary": true,
                "_links": {
                  "self": {
                    "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses/46"
                  },
                  "person": {
                    "href": "http://osdi-prototype.herokuapp.com/api/v1/people/23"
                  }
                }
              },
              "osdi:addresses": [
                {
                  "address1": "28160 Wiegand Divide",
                  "city": "Lake Amarimouth",
                  "state": "GA",
                  "postal_code": "27585-7257",
                  "country_code": "US",
                  "address_type": "Work",
                  "location" : {
             		"longitude" : "40.1",
             		"latitude" : "44.5"4,
             		"accuracy": "Rooftop"
             		},
                  "address_status": "Verified",
                  "primary": false,
                  "_links": {
                    "self": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses/45"
                    },
                    "person": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/people/23"
                    }
                  }
                },
                {
                  "address1": "935 Ed Lock",
                  "city": "New Dudley",
                  "state": "MN",
                  "postal_code": "17678",
                  "country_code": "RU",
                  "address_type": "Home",
                  "location" : {
             		"longitude" : "40.1",
             		"latitude" : "44.5"4,
             		"accuracy": "Rooftop"
             		},
                  "address_status": "Verified",
                  "primary": true,
                  "_links": {
                    "self": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses/46"
                    },
                    "person": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/people/23"
                    }
                  }
                }
              ]
            },
            "_links": {
              "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
              "osdi:addresses": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/23/addresses"
              },
              "osdi:primary_address": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/23/addresses/1"
              },
              "osdi:question_answers": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/23/question_answers"
              },
              "self": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/23"
              }
            }
          },
          {
            "first_name": "Parker",
            "last_name": "Walker",
            "middle_name": "Jannie",
            "email": "test-4@example.com",
            "gender": "Male",
            "gender_identity": "Male",
            "party": "Democrat",
            "source": "architecto",
            "source_details": "Itaque et reprehenderit rerum ea quis.",
            "custom_fields": {
	            "volunteer": "true",
	            "suppression_list": "0"
            },
            "twitter_handle": "@Parker_Walker",
            "guid": "c1e1d0d0-b562-0130-dc7c-168c51e904de",
			"birth_date" : {
				"month" : 1,
				"day" : 1,
				"year" : 1970
				},
            "_embedded": {
              "osdi:primary_address": {
                "address1": "22184 Vernie Cove",
                "city": "Rowemouth",
                "state": "GA",
                "postal_code": "74895",
                "country_code": "JP",
                "address_type": "Home",
                "location" : {
             		"longitude" : "40.1",
             		"latitude" : "44.5"4,
             		"accuracy": "Rooftop"
             		},
                "address_status": "Verified",
                "primary": true,
                "_links": {
                  "self": {
                    "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses/48"
                  },
                  "person": {
                    "href": "http://osdi-prototype.herokuapp.com/api/v1/people/24"
                  }
                }
              },
              "osdi:addresses": [
                {
                  "address1": "7485 Rashad Pine",
                  "city": "Brandynview",
                  "state": "PR",
                  "postal_code": "76221-3163",
                  "country_code": "US",
                  "address_type": "Work",
                  "location" : {
             		"longitude" : "40.1",
             		"latitude" : "44.5"4,
             		"accuracy": "Rooftop"
             		},
                  "address_status": "Verified",
                  "primary": false,
                  "_links": {
                    "self": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses/47"
                    },
                    "person": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/people/24"
                    }
                  }
                },
                {
                  "address1": "22184 Vernie Cove",
                  "city": "Rowemouth",
                  "state": "GA",
                  "postal_code": "74895",
                  "country_code": "JP",
                  "address_type": "Home",
                  "location" : {
             		"longitude" : "40.1",
             		"latitude" : "44.5"4,
             		"accuracy": "Rooftop"
             		},
                  "address_status": "Verified",
                  "primary": true,
                  "_links": {
                    "self": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses/48"
                    },
                    "person": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/people/24"
                    }
                  }
                }
              ]
            },
            "_links": {
                
              "osdi:addresses": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/24/addresses"
              },
              "osdi:question_answers": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/24/question_answers"
              },
              "self": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/24"
              }
            }
          }
        ]
      },
      "_links": {
        "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
        "self": {
          "href": "http://osdi-prototype.herokuapp.com/api/v1/people"
        },
        "osdi:addresses": {
          "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses"
        },
        "osdi:find": {
            "href": "http://api.opensupporter.org/api/v1/people?$filter={odata_query}",
            "templated": true
        }
      }
    }
