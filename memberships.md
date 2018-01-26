---
layout: default
title: Memberships
---

# Memberships

This document defines the Membership resource.

Memberships are entities linking individuals to organized groups.

Memberships can be either be administrators or not, and have dates that someone became
a member or left an Organization, as well as links to their corresponding Organization
and People resources.

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
|administrator  |boolean    |Whether this Membership is an administrative membership.
|ended          |boolean    |Whether this Membership has ended (the Person has left the organization).
|ended_at       |boolean    |The date that this Membership ended, or empty if person is still a member.

_[Back to top...](#)_

### Links

{% include links_intro.md %}

|Name          	|Type		|Description
|-----------    |-----------|--------------
|self			      |[Membership*](memberships.html)	   |A self-referential link to the membership.
|organization   |[Organization*](organizations.html) |A link to the Organization that the membership is with respect to.
|person         |[People*](people.html)              |A link to the People resource that is the member of the Organization.

_[Back to top...](#)_

## Related Resources

* [Person](people.html)
* [Organization](organizations.html)

_[Back to top...](#)_
