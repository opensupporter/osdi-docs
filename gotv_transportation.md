---
layout: default
title: "GOTV Transportation"
---

{% include experimental.html %}

# GOTV Transportation

### Sections

* [Fields](#fields)
    * [Demand Fields](#demand-fields)
    * [Rider Fields](#rider-fields)
      * [RiderRestriction Fields](#riderrestriction-fields)
        * [Standard Values](#standard-values)
          * [Language](#language)
          * [Accessibility](#accessibility)
    * [Vehicle Fields](#vehicle-fields)
      * [VehicleSeat](#vehicle-seat)
    * [Assignment Fields](#assignment-fields)
    * [Interval Fields](#interval-fields)
    * [Location Fields](#location-fields)
* [Scenarios](#scenarios)
    * [Scenario A centrally implemented, web-based GOTV system](#scenario-a-centrally-implemented-web-based-gotv-system)
    * [Scenario: A federated implementation](#scenario-a-federated-implementation)

GOTV Transportation represents the collection of types used to describe and satisfy specific demands for transportation to a voting or registration location. The model consists of Riders, Demands, Vehicles, Drivers, and Assignments, as well as other supporting types. At the highest level, the goal of a GOTV Transportation system is to match drivers and vehicles with riders' demands, making as many assignments as possible to drive turnout.

Demands represent a demand for transportation to a voting location by one or more Riders. Each rider may be a single voter, and demands might be associated with more than one rider, representing a group of voters or, in some cases, a group of voters as well as non-voters. As an example of this last category, consider the combination of a voter and his fulltime healthcare worker, or a voting parent and a minor child. Demands indicate the set of locations which could satisfy them, as well as the times during which they are valid and other constraints on how it could be solved. A constraint might be, for instance, wheelchair accessibility, or the rider's preferred language.

Vehicles are used to transport riders, and have an associated driver. Vehicles and drivers both have various state capabilities and capacities. For example, an SUV may have capacity for 4 riders and be wheelchair accessible. It's driver may be a Spanish speaker and male. In some cases, a vehicle may be operated by more than one person, such as when two people volunteer to share the load of driving, or to feel more comfortable in picking up and traveling with strangers. In these cases, we do not attempt to model the pair of drivers, but do expect the driver to adjust the seating capacity of the vehicle in order to account for the extra driver.

For more details on how a system might be built on the data types proposed here, see the [Scenarios](#scenarios).

## Fields

### Demand Fields

| Name  | Type  | Description
|-----  |-----  |------
| availability  | Interval[]  | The Intervals during which this Demand can be satisfied
| locations | Location[] | The locations to which the associated Riders may be transported
| riders  | Rider[] | The Riders generating this Demand
| coordinating_rider | Rider* | If set, then communications about an assigned Ride should be directed towards this Rider. It is an error if this value is set but is not associated with an element of `riders`
| external_coordinator | Person* | If set, this person is not a rider but should receive communications about this Demand and, if appropriate, its Assignment. For example, this could be a staff member at a senior center coordinating rides for a resident and helping load that resident into and out of a vehicle.


Systems may reject creation of demands which would result in a rider being associated with multiple demands.

### Rider Fields

| Name | Type | Description
|------|--------|------
| id | string | The unique ID for this Rider
| person | Person* | If set, then this Rider is associated with a known [Person](people.html).
| assistant | Person* | If set, then this Rider is not the principal source of the associated Demand, but requires transport along with the one who is in order to help that person through the voting or transportation process. Examples might include healthcare or nursing aides or translators.
| minor | int* | If set, the Rider is a minor accompanying another Rider in the group, and has the age indicated. As this Rider is a minor, the system has no expectation or desire that they be personally identified as an instance of `Person`.
| restrictions | RiderRestriction[] | Any Rider restrictions which should be considered when creating an Assignment for this Rider

Note that of the fields `person`, `assistant`, and `minor`, exactly one must be set in each instance.

### RiderRestriction Fields

| Name | Type | Description
|------|--------|------
| key | string | The well-known key to the system identifying the nature of this restriction.
| value | object | The value expressing the specifics of the restriction, as appropriate for its type.

Restrictions are loosely typed and specific to the system responsible for making Assignments. This specification may evolve to provide some basic suggested restrictions which could be broadly useful, but there would be no requirement that implementations express semantically equivalent restrictions in the same way. The values for `key` are intended to be globally unique, and should be namespaced in such a way that they will not collide with restrictions from other providers. For instance, good keys might take the form of `osdi:rider_restriction_language` or `acme:requires_wheelchair_ramp`, whereas simply `requires_wheelchair_ramp` should be avoided as likely to collide.

#### Standard Values

We can imagine the following starting point of restrictions for use by systems that find them useful. In each case below, we provide a type definition for the object passed as the `value` for the restriction, as well as provide a suggested value for `key`.

##### Language

Keyed as `osdi:rider_restriction_language`:

| Name | Type | Description
|------|--------|------
| iana_codes | string[] | Language codes, as defined by [RFC 5646](https://tools.ietf.org/html/rfc5646), that the associated rider can speak. Examples would include `en/US` or `es/419`.

##### Accessibility

Keyed as `osdi:rider_restriction_accessibility`

| Name | Type | Description
|------|--------|------
| is_hearing_impaired | bool | Indicates that the Rider has a partial or total hearing impairment
| is_vision_impaired | bool | Indicates that the Rider has a partial or total vision impairment
| wheelchair_accessibility | enum* | If specified, one of `ramp`, indicating that the Rider requires a wheelchair ramp in order to enter or exit the Vehicle, or `collapsible` to indicate that no ramp is required, but that the associated Vehicle needs enough storage space to carry a collapsed wheelchair. Other variants may be added to this enum.

### Vehicle Fields

| Name | Type | Description
|------|--------|------
| id | string | The unique identifier for this vehicle
| drivers | string[] | The Person(s) who are responsible for communicating with Riders of this vehicle and for its operation. In most cases this will be a singleton array, but it is possible that groups of people will together fulfill the driver role (example: One drives while the other navigates)
| seating | VehicleSeat[] | An array of Seating values indicating how the passenger seating is configured
| availability | Interval[] | An array of times during which this vehicle is operational and can be assigned to Demands.
| range | Duration | The maximum amount of time this vehicle can travel for any particular ride. This value might be the minimum of the furthest the vehicle's driver is willing to travel, or of the maximum range of the vehicle itself, such as with an electric vehicle subject to frequent recharging stops.
| location | Location | This vehicle's location, from which it is assumed to begin or end with each availiability interval.
| user_description | string | A brief, human-readable description of the vehicle to assist riders. For example, "Black Honda Civic, License ABC123". Note that this description field may also give way to future, more structured fields ("Year", "Make", "Model", "License Plate", etc), but rather than diving into a potentially over-structured vehicle data model solely for the purposes of constructing a brief string message for users, we start with just this freeform field.

#### VehicleSeat

| Name | Type | Description
|------|--------|------
| type | enum | A value indicating the type of seat. Known values include `standard`, indicating that the seat is suitable for an able-bodied adult; `middle` indicating that the seat is a middle seat, and `wheelchair`, indicating that the seat is intended to be occupied directly by a lockable, electric wheelchair and nothing else.

Note that this type only has a single field at the moment, but we choose to model it as a structured type with one field rather than embedding the enumerated field directly where this type is used, to allow for the possibility of adding new, optional fields in the future.

### Assignment Fields

An Assignment indicates a specific matching between a Vehicle and a Demand.

An implementation supporting the APIs here would employ some matching and scheduling algorithm to pair Demands with Drivers and Vehicles in order to make specific Assignments, in which a vehicle is expected to satisfy a Rider's Demand by picking up and dropping off at a specified time and place. Assignments may be removed, such as by the cancellation by a Rider, Coordinator, Driver, or Dispatcher. Doing so does not affect the underlying Demand, which may still be satisfied by the scheduling algorithm by making an alternate Assignment.

| Name | Type | Description
|------|--------|------
| id | string | This Assignment's ID
| vehicle_id | string | The Vehicle to which this Assignment is made
| demand_id | string | The Demand to which this Assignment is made
| pick_up_at_time | datetime | The time at which this assigned ride is estimated to begin
| pick_up_at_location | Location | The location at which this assigned will begin
| drop_off_at_time | datetime | The time at which this assigned ride is estimated to end
| drop_off_at_location | Location | The specific location at which this assigned ride will end
| return_assignment_id | string* | If set, the ID of the Assignment which will return the demanding riders to their next location. Typically the next location will be the same one from which the riders departed, but it may be different (example: voter departs from home but is returned after voting to their place of work or school).
| status | string | One of `scheduled`, `in-progress`, `completed`, or `canceled`. Implementations may prevent certain actions on assignments based on their status at the time (example: an implementation may disallow cancellation of an assigned ride which is `in-progress`).

### Interval Fields

| Name | Type | Description
|------|--------|------
| start | datetime | The time at which this interval begins (inclusive)
| end | datetime | The time at which this interval ends (exclusive)

Intervals determine a discrete and continuous amount of time during which a ride can occur (or more generally, when a thing can occur). Intervals are valid if and only if `start < end`.

### Location Fields

| Name | Type | Description
|------|--------|------
| address | [PostalAddress](people.html#postal-addresses) | The physical address for this location
| identifier | string | A unique identifier within the system for this location. Values may be meaningful to humans ("SC Polling station 1092") or fully opaque database identifiers ("pl2934jk239").
| availability | Interval[] | If non-empty, availability specifies the times at which this location is available to provide services. For example, a Location representing a polling location might list the hours during which voters are allowed to enter the line to vote.

## Scenarios

The primary motivation for this data model is to describe and accelerate the implementation of applications which provide for matching of drivers and riders, producing assignments. The APIs described here could be used in various ways to build these applications. In one configuration, we can imagine a lower-level routing, dispatch, and scheduling system which is used by API clients to populate their specific rider and driver details, and which provides to those callers a scheduled and on-demand routing and dispatch system. Further, we can imagine that third-parties working as clients to these APIs, but representing neither the specific data owners nor the scheduler's implementation, could build role-specific apps, including mobile apps ("mobile" includes both smartphone as well as SMS/Telephone based) for drivers or riders, or web-based dispatch and assistance tools for coordinating teams.

While there are any number of ways to factor these various pieces, we present below a small motivating example.

### Scenario: A centrally implemented, web-based GOTV system

In this example, we can imagine a single software team that uses the APIs in this specification to build a self-contained ride coordination service, including:
  * A single web application and attending database to store the data model above, and which provides services to potential riders, drivers, and campaign coordinators to register, login, and view the system.
  * Depending on the user's role (driver, rider, administrator), the application presents different views of the data model:
    * Drivers would see their own ride assignments and upcoming schedule, as well as tools which they could use to update their availability or vehicle configuration.
    * Riders would see their currently specified demand(s) (multiple if they need to register during one ride and vote during another)
    * Administrators would have access to as much data as necesary, including all of it, in order to troubleshoot, specify manual overrides, and see system status and other dashboards.
  * Changes to factors which affect the schedule, such as demands, location or vehicle availabilities, or the addition of new vehicles and riders, might cascade into changes in any pre-existing assignments, or might open up opportunities for the system to make new assignments.

An application such as this might be built and operated by a single organization, and used to support individual campaigns. In this case, the campaign staff themselves, in coordination with the implementing software team, might comprise the set of administrators and coordinators, and the campaign staff themselves would recruit and help populate the system with demands and drivers to satisfy them. One motivating example of such an approach is [Drive the Vote](https://www.drive.vote/), built by a software team at [Ragtag](https://ragtag.org/).

### Scenario: A federated implementation

In this example, we extend the one above and assume that different organizations are responsible for each of its principal components. In particular, we could imagine:
  * A scheduling, routing, and dispatching engine is provided as a hosted solution by a central team, which uses the data model in this specification to expose operations for client applications to read and update information about riders, demands, drivers, and all other elements of the system. Additionally, this hosted system provides primary registration and authentication services to its API clients, and enforces permissions inherent in the system. (example: API calls made on behalf of a driver may only view or manipulate that drivers; API calls made to add or update polling station location must be made by an user with those specific -- and rare -- permissions).
  * A set of web-based tools are built atop this UI for use by campaigns and advocacy organizations which allows them to invite users to the system in any number of roles (rider, driver, polling place data editor, dispatcher, etc). Campaigns would use this web-based tool to seed the system with their supporters who they feel are most likely to contribute to or benefit from its operation. In all likelihood, this tool would also use OSDI or other vendor APIs to help sync this data directly from the campaign's existing databases (such as NGP-VAN).
  * A mobile and web app would be provided to riders and drivers, allowing them to fill out their respective profiles with demand or availability data, respectively, and to update and view their upcoming appointments. The apps would function in a way similar to those of many popular ride-hailing and taxi apps, both for riders and drivers.
  * A web-based dispatch and support system would call the scheduling system's APIs to retrieve status on rides in the near-future or in realtime, and provide tools for providing rider and driver support and for scheduling overrides or manually making or breaking assignments. This tool might be used directly by campaign staff, or could be operated by a dedicated set of volunteers providing support service, potentially from anywhere.

The examples above are just a loose shape of what such a system would actually require, but illustrate that the APIs in this specification could, in theory, allow separate engineering and volunteering teams to each work on individual subsystems as described above, and to, as a result, bring forth a highly scalable, supportable, and sophisticated nationwide GOTV Transporation system.
