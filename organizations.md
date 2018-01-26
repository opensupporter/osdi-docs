---
layout: default
title: Organizations
---

# Organizations

This document defines the Organization resource.

Organizations are entities representing organized groups of individuals.

Organizations have names, locations, legal statuses, administrators, memberships,
parent organizations, partner organizations, and associated action histories
recording the actions users have taken in the system on their behalf.

### Sections:

* [Endpoints and URL structures](#endpoints-and-url-structures)
* [Fields](#fields)
    * [Common Fields](#common-fields)
    * [People Fields](#people-fields)
    * [Related Objects](#related-objects)
    * [Links](#links)
* [Helpers](#helpers)
* [Related Resources](#related-resources)
* [Scenarios](#scenarios)
    * [Scenario: Retrieving a collection of Organization resources (GET)](#scenario-retrieving-a-collection-of-person-resources-get)
    * [Scenario: Retrieving an individual Organization resource (GET)](#scenario-scenario-retrieving-an-individual-person-resource-get)
    * [Scenario: Creating a new person (POST)](#scenario-creating-a-new-person-post)
    * [Scenario: Modifying a person (PUT)](#scenario-modifying-a-person-put)
    * [Scenario: Deleting a person (DELETE)](#scenario-deleting-a-person-delete)


{% include endpoints_and_url_structures.md %}

The link relation label for a Organization resource is ```osdi:organization``` for a single Organization
resource or ```osdi:organization``` for a collection of Organization resources.

_[Back to top...](#)_


## Fields

{% include fields_intro.md %}

{% include global_fields.md %}

_[Back to top...](#)_


### Organization Fields

A list of fields specific to the Organization resource.

|Name          |Type      |Description
|-----------    |-----------|--------------
|name         |string     |The organization's name.
|legal_status |flexenum   |The organizations legal status, or "unofficial" if the organization does not have a corresponding legal entity.
|location     |Location(#location) |A location hash describing where this organization is based.
|contact      |Contact(#contact)  |A contact hash representing how one should get in contact with the organization.

_[Back to top...](#)_

### Related Objects

These JSON hashes included in the table above are broken out into their own tables for readability, rather than independent resources with their own endpoints.

#### Contact

|Name          |Type      |Description
|-----------    |-----------|--------------
|contact.name	|string	|Name of the host or contact person for organization (e.g., Jane Doe)
|contact.email_address	|string	|Email address of the organization (jane.doe@hotmail.co.uk)
|contact.phone_number	|string	|Phone number of the organization (214-555-0869)
|contact.additional_info |string  |Free form place for information about how to contact the organization
|contact.public|boolean |Whether the organization's info should be shared publicly (if false, should only be shared with members)

#### Location

|Name          |Type      |Description
|-----------    |-----------|--------------
|location.venue	|string	|Optional venue name at the event address, useful for names of buildings. (ex: Smith Hall)
|location.address_lines	|strings[]	|An array of strings representing the event's street address.
|location.locality	|string	|A city or other local administrative area.
|location.region	|string	|State or subdivision codes according to ISO 3166-2 (Final 2 alpha digits).
|location.postal_code	|string	|The region specific postal code, such as a zip code.
|location.country	|string	|The country code according to ISO 3166-1 Alpha-2.
|location.language	|string	|Language in which the address is recorded -- language code according to ISO 639.
|location.location	|object	|An object hash representing the geocoded location information for the address.
|location.location.latitude	|float	|A positive or negative float number representing the latitude of the address.
|location.location.longitude	|float	|A positive or negative float number representing the longitude of the address.
|location.location.accuracy	|enum	|A value representing the accuracy of the geocode. One of "Rooftop" or "Approximate".
|location.public |boolean |Whether the venue's location should be shared publicly, or if false, only shared with RSVPs (for example, someone's house)

### Links

{% include links_intro.md %}

|Name          	|Type		|Description
|-----------    |-----------|--------------
|self			|[Organization*](organizations.html)	|A self-referential link to the organization.
|events   |[Events*](events.html)               |A link to the collection of events associated with the organization.
|administrators |[Memberships*](memberships.html) |A link to the collection of membership resources that link an organization to its administrators.
|memberships |[Memberships*](memberships.html)  |A link to the collection of memberships resources linking an organization to its members.
|modified_by		|[Person*](people.html)  	|A link to a Person resource representing the last editor of this person.

_[Back to top...](#)_

## Related Resources

* [Person](people.html)
* [Event](events.html)
* [Membership](membership.html)

_[Back to top...](#)_
