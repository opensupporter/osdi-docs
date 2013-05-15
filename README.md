#Open Supporter Data Interface


# Overview
This specification defines a common HTTP based REST protocol and data model for accessing supporter data.  The data model includes persons, events, donations, general advocacy actions and is extensible for future needs.

[Read our full charter](/skydrive/osdi-charter.v2.htm)

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
