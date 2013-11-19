# Person
## Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
|last_name      |string     |Last name
|first_name     |string     |First name
|middle_name	|string     |Middle name
|prefix			| string	|Prefix like "Dr", "Mr" etc. Free-form field
|suffix			| string	|Suffix like "Jr.", "Ph.D" Free-form field
|gender			|string		|The gender binary with which a person most closely identifies, or "Other" if the person identifies with neither. One of "Female", "Male", "Other".
|gender_identity|string     |The self-described gender with which a person identifies. Free-form field. While this field is free-form, data should still follow standardized forms whenever possible (i.e. use "Female" and not "female" or "F"). _Examples: If a person self-identifies as "Female", both_ `gender` _and_ `gender_identity` _fields should have a value of "Female". If a person self-identifies as "Transgender Female",_ `gender` _should have a value of "Female" and_ `gender_identity` _should have a value of "Transgender Female"._
|identifier     |string     |The provider's current canonical identifier for a person. Identifier should comply with the format `<provider-name>:<id>`. See below for more details. 
|party          |string     |Party affiliation "democrat", "republican", "independent", "none"
|primary_address|Address    |A single instance of an address reflecting the person's primary address
|primary_phone  |string     |The person's primary phone number
|primary_email  |string     |A person's primary email address
|source         |string     |Information about the source where this person record was acquired.  Eg "Ref74"
|birthdate		|hash		| A hash representing the birth date
|birthdate.month|integer	| integer representing the month of the birth date
|birthdate.day	|integer	| integer representing the day of the birth date
|birthdate.year|integer		| integer representing the 4 digit year of the birth date

## Collections
| Name          | Type      | Description
|-----------    |-----------|--------------
|identifiers    |identifiers[]| A collection of identifiers the provider has determined to be associated with the person
|addresses      |Address[]  |A collection of addresses associated with the person
|emails         |Email[]    |A collection of email addresses associated with the person
|phones         |Phone[]	|A collection of phone numbers associated with the person
|donations      |Donation[] |A collection of donations associated with the person
|question_answers|QuestionAnswer[]|A collection of answers to questions from surveys
|event_attendance |Attendance[]|A collection of attendance records for a person
|interactions   |Interaction[]|A collection of outreach interactions for a person, eg Volunteer Joe called voter Sam F. Bar
|profiles		| Profile[]	| A collection of profiles for online services

# Email Addresses
| Name          | Type      | Description
|----------------|-----------|----------------
| primary		| boolean	|Denotes if this is the primary address.  A person can have only one primary address
| address		| string	| The actual email address according to RFC822
| address_type	| string	| Flexenum of Home, Work, Other

# Phone Numbers
| Name          | Type      | Description
|----------------|-----------|----------------
| primary		| boolean	|Denotes if this is the primary phone number.  A person can have only one primary number
| number		| string	| The actual phone number which MUST including country code and MUST be numeric characters only 
| extension		| string	| Optional associated extension
| description	| string	| Optional Free form additional text description
| phone_type	| string	| flexnum of Home, Work, Mobile, Other, Daytime, Evening, Fax
| operator		| string	| Optional: Operator/Carrier associated with number, eg "Verizon"
| country		| string	| Country code according to ISO 3166-1 Alpha-2
| sms_capable	| boolean	| True if the number can accept sms text messages
| do_not_call	| boolean	| True if this number is registered on the US FCC Do Not Call Registry

# Profiles
Profiles correspond to a person's accounts on online services like Facebook, Twitter, etc.

| Name          | Type      | Description
|----------------|-----------|----------------
| provider		| string	| The provider name, eg "Facebook"
| id			| string	| The unique identifier provided by the provider, eg "135165"
| url			| string	| The URL to the user's web viewable profile, eg "http://facebook.com/johnqpublic"
| handle		| string	| The handle name, eg "johnqpublic"

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
		"identifier": "voterlabs:5678"
		"first_name": "Edwin",
		"last_name": "Labadie"
		"email": "edwin.labadie@example.com"
		"_embedded": {
			"identifiers": [
				"voterlabs:12bd9f4e-cc98-44aa-b741-fe52dc2af93d"
			]
		}
	}

Voter Labs also has an existing record in their database that looks like this:

__Figure 2.__

	{
		"identifier": "voterlabs:1234"
		"first_name": "Edwin",
		"last_name": "Labadie"
		"middle_name": "Marques"
		"email": "edwin@example-old.com",
		"_embedded": {
			"identifiers": [
				"voterlabs:e2cdf524-15fc-48b4-8261-b905e91de954"
			]
		}
	}

Through some internally-defined process, Voter Labs decides the two records represent the same person and should be merged. Also through some internally-defined process, they determine which record should be trusted for which fields and determine which record's identifier is the new canonical identifier. The resulting merged record would look like this:

__Figure 3.__

	{
		"identifier": "voterlabs:1234"
		"first_name": "Edwin",
		"last_name": "Labadie"
		"middle_name": "Marques"
		"email": "edwin.labadie@example.com",
		"_embedded": {
			"identifiers": [
				"voterlabs:1234",
				"voterlabs:5678"
			]
		}
	}

What this new record means is that `voterlabs:1234` is the new id by which Voter Labs refers to this real person and that `voterlabs:5678` is another id by which this real person has previously been referred to.

"Jane Doe For Congress" is a consumer of the Voter Labs API. They have a locally cached representation of both records before Voter Labs merged the two records. When "Jane Doe For Congress" requests the record `voterlabs:5678` from the Voter Labs API, they should get a 301 redirect to the newly merged record seen above (Figure 3).


# Address
## Attributes

| Name          | Type      | Description
|----------------|-----------|----------------
| primary		| boolean	|Denotes if this is the primary address.  A person can have only one primary address
|address_type   |string     |Type of address "Home","Work",'Mailing'
|address_lines       |string[]     |Address lines 1 - n
|city           |string     |City
|state          |string     |State abbreviation according to ISO 3166-2 (Final 2 alpha digits)
|postal_code    |string     |Region specific postal code
|country_code	|string		|Country code according to ISO 3166-1 Alpha-2
|location		|hash		| Location information for the address
|.lattitude		|string		|Geolocation latitude
|.longitude		|string		|Geolocation longitude
|.accuracy		|string		|One of "Rooftop", "Approximate"
|address_status	|string		|One of "Potential", "Verified", "Bad".

### State and Country codes
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



## Links
| Name          | Type      | Description
|-----------    |-----------|--------------
|person      |Person*       |A link to the person associated with the address

# Scenarios
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
            "guid": "c1d9c510-b562-0130-dc7c-168c51e904de",
			"birth_date" : {
				"month" : 1,
				"day" : 1,
				"year" : 1970
				},
            "_embedded": {
              "primary_address": {
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
              "addresses": [
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
              "addresses": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/23/addresses"
              },
              "question_answers": {
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
            "twitter_handle": "@Parker_Walker",
            "guid": "c1e1d0d0-b562-0130-dc7c-168c51e904de",
			"birth_date" : {
				"month" : 1,
				"day" : 1,
				"year" : 1970
				},
            "_embedded": {
              "primary_address": {
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
              "addresses": [
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
              "addresses": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/24/addresses"
              },
              "question_answers": {
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
        "self": {
          "href": "http://osdi-prototype.herokuapp.com/api/v1/people"
        },
        "addresses": {
          "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses"
        }
      }
    }
