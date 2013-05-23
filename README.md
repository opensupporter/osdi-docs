
#Open Supporter Data Interface

# Overview
The Open Supporter Data Interface (OSDI) is an effort to reduce customer costs related to moving data between different systems by defining a common API for products in the non-profit and campaign space.  We are a team of vendors (competitors and partners) and customers who are making customer cost reduction and interoperability the top priority.

# Problem Space
Today, customers often seek to use a variety of digital tools from different vendors to build their optimal solution.  Systems such as CRMs, email blasters, donation management systems, social media tools, voter engagement, and volunteer management may come from different vendors.  However, in order to keep the data consistent, customers often need to do frequent, manual imports and exports of CSV files.  Sometimes the options are unavailable or so complex that the systems remain inconsistent and valuable information is lost.

Systems typically contain a common set of resources, including but not limited to people (supporters), addresses, donations, events, or social actions. For example, each product typically represents a person differently.  How addresses are handled varies and even the field names are different.

There is no competitive advantage for vendors to model a person differently.  The difference merely serve as a cost to customers in the form of complexity, data loss during transfer, staff & volunteer time and accelerated hair loss.
# Goal
## Summary
OSDI aims to define a common commodity API interface for these resources.   The API will cover the common use cases that customers need served.
The API will define interfaces including by not limited to resources representing Persons, Donations, Survey Questions, Tags, Events.
The group will determine the order in which to define resource models and which version of the API to include them in.
## Maintain Customer Focus
The OSDI team will solicit feedback from customers to review uses cases and technical designs to make sure that we are building something that is cost-effective to implement, and solves the problems customers care about.

## Allow Vendor differentiation
The core API will also allow for proprietary extensions to be built on top of it.  These extensions may represent vendor specific features, innovations, or differentiations.  They may also be special purpose features that are not relevant to the wider market.  They may be ideas where it is too early for the industry to come to consensus on today.  Over time, these may be integrated into the common API.

By using such a layered model, customer integration costs are reduced by ensuring that as much common code may be reused as possible.  For resources defined by the core there should be very little differential integration code necessary to work with products from different vendors.  Even when using a vendor or community specific feature extension, the core elements and concepts can be reused leaving only the extension as conditional code.

## Accelerate Innovation
The common API can also accelerate innovation in multiple ways.

1.	Reduce duplicate work by each vendor.  They can focus on new customer features rather than solving the same problems, but in different ways than other vendors

2.	Provide a common Application Platform that allows entrepreneurs, startups, and consultancies to build applications that can run across all vendor platforms that support OSDI rather than having to spend development resources writing individual connectors for each vendor platform.

# Current Deliverables
## Requirements
Requirements document which outlines the "use cases" aka "user stories" and resource data models.  Use cases or "user stories" are examples of tasks customers need to do.  Example: Query new supporter signups from today that wish to volunteer

## V1 API Specification
Resource data models define the fields and operations of a given object.  Example:  A Person resource has fields like first_name, last_name, zip etc
API specification which defines the common operations and resources to allow reading, updating and querying.

## Prototype
A prototype implementation useful for customers to experiment, exercise scenarios, and prototype client implementations

# Authors
Josh Cohen, Washington United For Marriage
Topper Bowers, Amicus
Erik Lukoff, Change.org
Tim Anderegg, New Organizing Institute (NOI)
Charles Parsons, Salsa

## Scenarios

## API Data Model

* People and Addresses
* Survey Questions

# Core Technology

## Basic Resource Access
### Common CRUD operations
#### Creating a Resource
Creating a new resource involves adding a new item to a collection.  To create a new resource, an HTTP POST message is sent to the URI for a collection.

    POST <addURI> HTTP/1.1
    Host: ...
    Accept: application/...
    Content-Type: application/...

    <serialization of request to create a new resource>

    HTTP/1.1 201 Created
    Location: ...
    Content-Type: application/...

    <serialization of new resource>

#### Retrieving a Resource
Retrieving a resource gets a representation of a resource instance or resource collection.  The retrieval is performed with an HTTP GET sent to the URI of the resource.

    GET <ResourceURI> HTTP/1.1
    Host: ...
    Accept: application/...

    HTTP/1.1 200 OK
    Content-Type: application/...

    <serialization of resource>

#### Updating a Resource
Updating a resource instance is accomplished by the use of an HTTP PUT sent to the URI of a given resource.  Due to the complexity of full-resource updates involving read-only properties, out-of-date data, and the need to know all properties (which one may not), this specification focuses on the ability to make partial updates to resources.

To make an update to a resource, the client sends an HTTP PUT to the URI of a resource instance.  The body of the put contains a partial resource representation including the attributes to update.  Missing attributes are left unchanged on the Provider side.

Clients may set an attribute to nil by including the attribute using ‘nil’ for JSON.

Updating Collections with PUT is not supported.

    PUT <editURI> HTTP/1.1
    Host: ...
    Accept: application/...
    Content-Type: application/...

    <serialization of request to update a resource>

    HTTP/1.1 200 OK
    Content-Type: application/...

    <serialization of updated resource>

    The HTTP response body shall contain the serialization of the updated resource

## Selecting Results
### Filtering Collections
When retrieving representations of a collection, clients may include filters expressed as query parameters.  The $filter query parameter is used for this purpose.  The $filter parameter value shall contain an expression using the following operators:

        '<', '<=', '=', '>=', ">', '!=' : Integer and date value/attribute
        '=', '!='                       : String value/attribute

Example:
Assuming a resource of ‘Person’ which has an attribute named ‘firstName’, the following filter would return resources with first name of ‘Jon’

        $filter=firstName=’Jon’

### Expand / Mixins
In order to optimize access, the $expand query parameter can be used to expand collections within resources.  Normally when retrieving a resource instance, subordinate collections are returned as references.

When the $expand parameter is used, the collection corresponding to the parameter value shall be expanded to represent the collection of instances.

When this parameter is used in requests for Collections, the value applies to the resources enclosed in the collection rather than the collection itself.

Example

Assuming a resource of Person with a collection of addresses, $expand=addresses would cause the collection of instances of addresses to be returned rather than a reference.

### Subsetting Results
The $first and $last parameters signify 1-based ordinal positions in a result set.

## HAL
Resources contained in server responses shall be serialized with the Hypertext Application Language [HAL](http://stateless.co/hal_specification.html)
By default, server responses should expand first level instances.  For example, in a response for a collection of resources, those resources should be embedded.


## Notational Conventions

In this specification, when defining models, the following notational conventions are used.

|Convention	|Description
|:-----------:|--------------
|type[]     | A reference to a collection of resources of type 'type'
|	type*	| A reference to a single resource of type 'type'
|	string	| A string
|	datetime| A date and time representation.  In JSON this is a string.  The contents of this attribute shall be  ISO 8601 
