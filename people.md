# Person
## Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
|last_name      |string     |Last name
|first_name     |string     |First name
|middle_name	|string     |Middle name
|sex            |string     |A person's gender, one of "Male", "Female", "Other"
|guid           |string     |A globally unique identifier (GUID) for a person
|party          |string     |Party affiliation "democrat", "republican", "independent", "none"
|primary_address|Address    |A single instance of an address reflecting the person's primary address
|primary_phone  |string     |The person's primary phone number
|primary_email  |string     |A person's primary email address
|source         |string     |Information about the source where this person record was acquired.  Eg "Ref74"

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

In the United States, state abbreviations should conform to [ISO 3166-1 Alpha-2](http://en.wikipedia.org/wiki/ISO_3166-2:US) but using only the final two alphanumeric characters

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
## Get a list of people

    GET /api/v1/people

    200 OK
    Content-Type: application/json

    {
      "_embedded": {
        "people": [
          {
            "first_name": "Casey",
            "last_name": "Senger",
            "middle_initial": "W",
            "email": "test-1@example.com",
            "gender": "Male",
            "party": "Democrat",
            "source": "consequatur",
            "source_details": "Et iusto ea et blanditiis debitis aut at aspernatur.",
            "twitter_handle": "@Casey_Senger",
            "dwid": "qrbqa0eswt",
            "primary_address" : {
                  "primary" : true,
                  "address1": "8923 Imogene Knolls",
                  "city": "Vandervortfort",
                  "state": "Washington",
                  "postal_code": "36397-7686",
                  "country": "Martinique"
            }
            "_embedded": {
              "addresses": [
                {
                  "primary" : true,
                  "address1": "8923 Imogene Knolls",
                  "city": "Vandervortfort",
                  "state": "Washington",
                  "postal_code": "36397-7686",
                  "country": "Martinique",
                  "_links": {
                    "self": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses/1"
                    },
                    "person": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/people/1"
                    }
                  }
                },
                {
                  "address1": "1371 Matt Stravenue",
                  "city": "West Emelymouth",
                  "state": "Indiana",
                  "postal_code": "44088",
                  "country": "Austria",
                  "_links": {
                    "self": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses/2"
                    },
                    "person": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/people/1"
                    }
                  }
                }
              ]
            },
            "_links": {
              "addresses": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/1/addresses"
              },
              "question_answers": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/1/question_answers"
              },
              "self": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/1"
              }
            }
          },
          {
            "first_name": "Edyth",
            "last_name": "Torphy",
            "middle_initial": "5",
            "email": "test-2@example.com",
            "gender": "Male",
            "party": "Democrat",
            "source": "nisi",
            "source_details": "Expedita officiis sed consectetur qui.",
            "twitter_handle": "@Edyth_Torphy",
            "dwid": "zs2qemlwqg",
            "primary_address":  {
                  "primary" : true,
                  "address1": "5806 Elmira Throughway",
                  "city": "Port Sandrineport",
                  "state": "California",
                  "postal_code": "68579",
                  "country": "Georgia",
            }
            "_embedded": {
              "addresses": [
                {
                  "primary" : true,
                  "address1": "5806 Elmira Throughway",
                  "city": "Port Sandrineport",
                  "state": "California",
                  "postal_code": "68579",
                  "country": "Georgia",
                  "_links": {
                    "self": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses/3"
                    },
                    "person": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/people/2"
                    }
                  }
                },
                {
                  "address1": "242 Ora Mill",
                  "city": "Ziemeland",
                  "state": "Louisiana",
                  "postal_code": "35127",
                  "country": "Tokelau",
                  "_links": {
                    "self": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/addresses/4"
                    },
                    "person": {
                      "href": "http://osdi-prototype.herokuapp.com/api/v1/people/2"
                    }
                  }
                }
              ]
            },
            "_links": {
              "addresses": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/2/addresses"
              },
              "question_answers": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/2/question_answers"
              },
              "self": {
                "href": "http://osdi-prototype.herokuapp.com/api/v1/people/2"
              }
            }
          },