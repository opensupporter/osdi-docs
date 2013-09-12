# Person
## Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
|last_name      |string     |Last name
|first_name     |string     |First name
|middle_name	|string     |Middle name
| prefix		| string	|Prefix like "Dr", "Mr" etc. Free-form field
| suffix		| string	|Suffix like "Jr.", "Ph.D" Free-form field
|sex            |string     |A person's biological sex, one of "Male", "Female", "Other"
|gender			|string		|The gender with which a person identifies. Free-form field
|guid           |string     |A globally unique identifier (GUID) for a person
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
|addresses      |Address[]  |A collection of addresses associated with the person
|emails         |Email[]    |A collection of email addresses associated with the person
|phones         |Phone[]
|donations      |Donation[] |A collection of donations associated with the person
|question_answers|QuestionAnswer[]|A collection of answers to questions from surveys
|event_attendance |Attendance[]|A collection of attendance records for a person
|interactions   |Interaction[]|A collection of outreach interactions for a person, eg Volunteer Joe called voter Sam F. Bar

# Address
## Attributes

| Name          | Type      | Description
|----------------|-----------|----------------
| primary		| boolean	|Denotes if this is the primary address.  A person can have only one primary address
|address_type   |string     |Type of address "Home","Work",'Mailing'
|address1       |string     |Address line 1
|address2       |string     |Address line 2
|addressN       |string     |Additional address lines
|city           |string     |City
|state          |string     |State abbreviation according to ISO 3166-2 (Final 2 alpha digits)
|postal_code    |string     |Region specific postal code
|country_code	|string		|Country code according to ISO 3166-1 Alpha-2
|lat			|float		|Geolocation latitude
|lng			|float		|Geolocation longitude
|accuracy		|string		|One of "Rooftop", "Approximate"
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
            "sex": "Female",
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
                "lat": 44,
                "lng": 40,
                "accuracy": "Rooftop",
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
                  "lat": 44,
                  "lng": 40,
                  "accuracy": "Rooftop",
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
                  "lat": 44,
                  "lng": 40,
                  "accuracy": "Rooftop",
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
            "sex": "Female",
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
                "lat": 44,
                "lng": 40,
                "accuracy": "Rooftop",
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
                  "lat": 44,
                  "lng": 40,
                  "accuracy": "Rooftop",
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
                  "lat": 44,
                  "lng": 40,
                  "accuracy": "Rooftop",
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