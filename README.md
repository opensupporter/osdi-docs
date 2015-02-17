---
layout: default
title: "OSDI"
permalink: index.html
---

![Logo](http://opensupporter.org/wp-content/themes/osdiv2/images/site/osdi-logo.png)

The Open Supporter Data Interface (OSDI) effort seeks to define an API and data structures for interoperability among products in the **progressive** cause-based, campaign and non-profit marketplace. The existence of a common API will reduce customer costs related to moving data between different systems, lower integration costs and enhance the ability of innovators to create products for the marketplace.

OSDI membership is made up of progressive vendors and organizations as well as invited non-partisan and mainstream industry vendors.

More Information about OSDI can be found at the website [opensupporter.org](http://opensupporter.org)

[The Github source for these documents can be found at: https://github.com/opensupporter/osdi-docs](https://github.com/opensupporter/osdi-docs)

[The GitHub pages (prettier) can be found at:http://opensupporter.github.io/osdi-docs/](http://opensupporter.github.io/osdi-docs/)

[Experiment with our prototype server http://api.opensupporter.org](http://api.opensupporter.org)


### Sections

* [API Overview and Structure](#api-overview-and-structure)
    * [REST + HAL](#rest--hal)
    * [Helpers](#helpers)
    * [API Entry Point and Linking](#api-entry-point-and-linking)
    * [Curies](#curies)
    * [Collections and Navigation](#collections-and-navigation)
    * [Filtering Collections](#filtering-collections)
    * [Encryption](#encryption)
    * [Authentication](#authentication)
    * [Mime Types](#mime-types)
    * [Error Handling](#error-handling)
    * [Flexibility and Server Behavior](#flexibility-and-server-behavior)
    * [Notational Conventions](#notational-conventions)
* [Authors and Leadership](#authors-and-leadership)
* [Contributing and Contact](#contributing-and-contact)

_[Back to top...](#)_
    
    
## API Overview and Structure

OSDI used a combination of approaches to provide flexible reading of data, simple operations for simple scenarios, and general purpose CRUD access.


### REST + HAL

Generally, OSDI follows traditional RESTful practices for accessing resources and collections of resources as well as creating, editing, updating, and deleting resources. 

OSDI also implements the [JSON+HAL spec](http://tools.ietf.org/html/draft-kelly-json-hal-05) hypermedia standard, providing links to associated collections and resources. JSON+HAL specifies a simple way to embed linking into APIs.  The combination of linking and a specification allows generic clients to be written and, indeed, [many languages have HAL clients](http://stateless.co/hal_specification.html).  Linking itself makes it easier to both reason about and write clients for an API.

By default, server responses should expand first level instances unless otherwise specified.  For example, in a response for a collection of resources, those resources should be embedded.

Finally, OSDI implements the OData query language for filtering collections.

_[Back to top...](#)_


### Helpers
OSDI also allows a client to perform a number of operations at once that in a traditionally RESTful API would take multiple requests through the use of helpers. For example, helpers can be used to create a new Person resource *and* register that this new person also signed a petition at the same time, something that with REST would require two operations (first creating the person, then associating them with the petition). 

_[Back to top...](#)_


### API Entry Point and linking

All access through OSDI starts at the [API Entry Point (AEP)](aep.html).  The AEP is a resource that acts like a directory of the types of resources available on a server. It also includes capability information like the maximum query pagesize and links to helper endpoints.

Your service provider can tell you what the AEP URL is for your account.

You can explore the AEP with a user-friendly interface by visiting our [prototype endpoint](http://api.opensupporter.org).

_[Back to top...](#)_


### Curies

You may have noticed that most links are prefaced with a name space "osdi" and that in the _links section there is a key labeled "curies." The link section defines links to *relationships* between objects and curies define those relationships. You will find documentation on the particular relationship by using the templated curie link.  For example, given the following links section:

```javascript
"_links": {
    "curies": [{ "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true }],
    "self": {
        "href": "http://api.opensupporter.org/api/v1/answers/46"
    },
    "osdi:question": {
        "href": "http://api.opensupporter.org/api/v1/questions"
    }
}
```
    
In order to fetch documentation on the question relationship, you would visit the following url: ```http://api.opensupporter.org/docs/v1/question```

Any links not prefaced with a curie name space are defined [here](http://www.iana.org/assignments/link-relations/link-relations.xml).

Vendors who add their own vendor-specific relationships must defined their own curie and preface their relationships with their own curie namespace.  For example,

```
"_links": {
    "curies": [
        { "name": "osdi", "href": "http://api.opensupporter.org/docs/v1/{rel}", "templated": true },
        { "name": "fb", "href": "http://facebook.com/docs/v1/{rel}", "templated": true }
    ],
    "self": {
        "href": "http://api.opensupporter.org/api/v1/question_answers/46"
    },
    "osdi:question": {
        "href": "http://api.opensupporter.org/api/v1/questions"
    },
    "fb:profile": {
        href: "http://facebook.com/profiles/1234"
    }
}
```

_[Back to top...](#)_


### Collections and Navigation

When retrieving collections, the response representation will include some common attributes.

| Name  | Type | Description
|-------|-------------------------------|-------------------------------
| total_pages    | integer                  | The number of pages applicable to this collection.
| total_records    | integer         | The total number of resources matching this collection.
| page    | integer                  | The page number of this response.


Collection responses may include additional links for navigation to previous and next pages.

|Name		| Description
|-----------|------------------------
|next		|The link for the next page of results.
|previous	|The link for the previous page of results.

The parameters ```per_page``` and ```page``` control pagination.

* ```?per_page``` specifies how many results to return per page.
* ```?page``` specifies the starting page to start with.

_[Back to top...](#)_


### Filtering Collections

When retrieving collections, a client may request that the server filter the results according to a query.  OSDI makes use of a subset of the OData query language to accomplish this.  The filter string is the value of the 'filter' query parameter.

See [OData Filter Query](http://www.odata.org/documentation/odata-v2-documentation/uri-conventions/#45_Filter_System_Query_Option_filter) for more information. 

General information can be found at [odata.org](http://odata.org).

#### Conventions

* String literals are enclosed in single quotes, eg: 'Jon'
* Integers are not quoted, eg: 5
* The whole query string is not enclosed in any quotes

#### Operators

OSDI supports the following OData operators:

| Name  | Description | Example
|-------|-------------------------------|-------------------------------
| eq    | Exact match                   | first_name eq 'John'
| ne    | Not Equal exact match         | first_name ne 'John'
| gt    | Greater than                  | birthdate.month gt 1980
| ge    | Greater or equal than         | created gt '2013-11-17T18:27:35-05'
| lt    | Less than                     | birthdate.year lt 1980
| le    | Less or equal than            | created le '2013-11-17T18:27:35-05'
| or    | Logical OR                    | first_name eq 'John' or first_name eq 'Jon'
| and   | Logical AND                   | first_name eq 'John' and last_name eq 'Doe'
    
OSDI defines the following OPTIONAL extension operators:

| Name  | Description | Example
|-------|-------------------------------|------------------------------
| like  | Case insensitive match        | first_name like 'john'       # returns John or john
| re    | Matches a regular expression  | first_name regexp '/[Rr]ob/' # Returns robert, Robert, rob, roberto 

#### Functions

OSDI defines the following OPTIONAL extension functions:


| Name  | Description | Example
|-------|-------------|-----------------------------------------------
| near  | Returns entries near a location within a radius   | gender eq 'Female' and near('10011', '5 miles')

#### Examples

Find all males in a given ZIP code: ```GET /api/v1/people?filter=gender eq 'Male' and address.postal_code eq '10011'```
    
Find new signups on or since a date and time (Eastern Time) ```GET /api/v1/people?filter=created ge '2013-11-17T18:27:35-05'```

_[Back to top...](#)_


###	Encryption

Providers may support secure HTTP connections using TLS. TLS 1.0, which shall be implemented, is specified in [RFC2246], and the TLS 1.1 and TLS 1.2 should be implemented as specified in [RFC4346] and [RFC5246], respectively.

Providers may support non-secure HTTP connections in addition or instead.

_[Back to top...](#)_


###	Authentication

Clients and providers may use a variety of mechanisms to authenticate and authorize operations.  The specification does not currently require supporting a specific method.  However, there are many choices which can work with this specification.  

* Cookie-Based Authentication
* HTTP Basic
* HTTP Digest
* Token-Based Authentication
* OAuth and OAuth 2.0
* OpenID

Future versions of this specification may officially support one or more of these methods, or provide standard ways of implementing various methods, or may in other ways be more specific about security and authentication.


#### Token Based Authentication

While OSDI does not currently mandate implementation of token-based authentication, for those that do implement this method of authentication the following standard should be followed. 

For header-based token authentication, the header should be named `OSDI-API-Token` (case sensitive), as in this example:

```
OSDI-API-Token: [your token here]
```

For URL query string-based token authentication, the query parameter should be named `osdi-api-token` (case insensitive), as in this example:

```
https://api.opensupporter.org/api/v1/?osdi-api-token=[your token here]
```

_[Back to top...](#)_



### Mime Types
When sending requests or responses, the preferred mime type is ```application/json```.

Servers and clients are __strongly__ encouraged to be liberal in accepting entities with a missing or incorrect mime type.

_[Back to top...](#)_


### Error Handling

If the attempt to access, update, or create the a resource or collection fails, the server shall return the appropriate HTTP error code representing the failure.

Within the response body, the server shall include descriptive information on the nature of the  failure.

_[Back to top...](#)_



### Flexibility and Server Behavior

Not all systems that implement OSDI will implement all aspects of the specification. 

There are no required fields in OSDI, and many relations are left up to each individual system and server.

Some servers may support some or all of the different resource collections.  For example, a peer to peer donation system might support Donations and People but not events. In order to find out what resources are available and what URIs to use to access them, do a GET on the AEP URL.

Some servers may support certain helpers and not others. The AEP and associated resources also includes links to the  helper endpoints available.

Similarly, matching behavior will be determined by each implementing system. For example, some systems may match people based on email address or other information.

_[Back to top...](#)_




### Notational Conventions

In this specification, when defining models, the following notational conventions are used.

|Convention	|Description
|:-----------:|--------------
|Type[]    | An array of objects of type 'type'
|Type[]*    | A reference to a collection of resources of type 'type'
|	Type*	| A reference to a single resource of type 'type'
|	string	| A string
|	datetime| A date and time representation.  In JSON this is a string.  The contents of this attribute shall be  ISO 8601 
| Object	| A complex attribute represented by a JSON object
| decimal	| A number in decimal notation such as 12.15. Used for currency.
| flexenum  | One of a list of values, or another value. For example, for party_identification on people, if the person is a Democrat they should be marked as "Democratic" with that exact spelling and casing, but if they are not one of the defined types then you can use another value instead, such as "Working Families".

In the description of string types, sometimes the specification will list a set of acceptable values such as

| Name		| Type		| Description
|-----------|-----------|------------------
| gender	| string	| one of "Male", "Female", "Other" |

In these cases, the string value should conform to one of the choices unless specified otherwise.

_[Back to top...](#)_

    

## Authors and Leadership

* Leo Aguayo, Organizer
* Tim Anderegg, New Organizing Institute (NOI)
* Topper Bowers, Independent
* Beth Becker, Indigo Strategies
* Gilbert Chan, Organizer
* Josh Cohen, Washington United For Marriage (Editor)
* Jeff Crigler, Catalist
* Gustavo Costa, The Action Network
* Michael Eskin, Blue State Digital
* Jascha Franklin-Hodge, Blue State Digital
* Abraham Godong, FasterCampaigns
* Tim Gutowski, Trilogy Interactive
* Chuck Hagenbuch, Blue State Digital
* Harlan Hill, Indigo Strategies
* Tim Holahan, BroadStripes
* Matt Klaber, Independent
* Ben Krokower, FasterCampaigns
* Eli Lee, The Quad
* Dave Leichtman, Microsoft Corporation
* Marc Love, Independent
* Walter Ludwig, Indigo Strategies
* Drew Miller, NGP VAN
* Joe McLaughlin, Citizen Action NY
* Mark Paquette, TheDataBank
* Charles Parsons, Salsa Labs
* Rich Ranallo, Revolution Messaging
* Jason Rosenbaum, The Action Network
* Ben Stein, Mobile Commons
* Ben Stroud, Targetsmart Communications
* Ray Suelzer, UFCW International Union
* Nate Thames, ActBlue
* Jim Pugh, ShareProgress
* Sylvia Rolle, Washington United for Marriage
* Chris Thomas, Sierra Club
* Brian Vallelunga, Trilogy Interactive (Editor)
* Sandra Wechsler, The Quad
* Nathan Woodhull, ControlShift Labs
* Ryan Zarkesh
* Misha Zhurkin, Catalist

### Additional Acknowledgments
* Reed Probus, Web, Logo & Graphic Design
* Nathan Tabak, Whitepaper writing and editing
* Anthony Whittaker, Evangelism and Booth Duty
* Scott Wooledge, V1 Logo

### Leadership
See our [governance committee members and executive officers](http://opensupporter.org/leadership).

_[Back to top...](#)_

## Contributing and Contact

Anyone is welcome to contribute by filing GitHub issues. To join our committees for specification discussion, please contact us at [http://opensupporter.org](http://opensupporter.org) or via email at [info@opensupporter.org](mailto:info@opensupporter.org).

_[Back to top...](#)_