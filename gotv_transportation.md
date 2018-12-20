---
layout: default
title: "Rides"
---
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

GOTV Transportation represents the collection of types used to describe and satisfy specific demands for transportation to a voting or registration location. The model consists of Riders, Demands, Vehicles, Drivers, as well as other supporting types.

Demands represent a demand for transportation to a voting location by one or more Riders. Each rider may be a single voter, and demands might be associated with more than one rider, representing a group of voters or, in some cases, a group of voters as well as non-voters. As an example of this last category, consider the combination of a voter and his fulltime healthcare worker, or a voting parent and a minor child. Demands indicate the set of locations which could satisfy them, as well as the times during which they are valid and other constraints on how it could be solved. A constraint might be, for instance, wheelchair accessibility, or the rider's preferred language.

Vehicles are used to transport riders, and have an associated driver. Vehicles and drivers both have various state capabilities and capacities. For example, an SUV may have capacity for 4 riders and be wheelchair accessible. It's driver may be a Spanish speaker and male. In some cases, a vehicle may be operated by more than one person, such as when two people volunteer to share the load of driving, or to feel more comfortable in picking up and traveling with strangers. In these cases, we do not attempt to model the pair of drivers, but do expect the driver to adjust the decrement by one the capacity of the vehicle in order to account for the extra driver.

Applications built atop these types will attempt to match Demands with Vehicles and Drivers to make Assignments.

## Fields

### Demand Fields

| Name  | Type  | Description
|-----  |-----  |------
| availability  | Interval[]  | The Intervals during which this Demand can be satisfied
| locations | [PostalAddress](people.html#postal-addresses)[]  | The locations to which the associated Riders may be transported
| riders  | Rider[] | The Riders generating this Demand
| coordinating_rider | Rider* | If set, then communications about an assigned Ride should be directed towards this Rider. It is an error if this value is set but is not associated with an element of `riders`

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

#### VehicleSeat

| Name | Type | Description
|------|--------|------
| type | enum | A value indicating the type of seat. Known values include `standard`, indicating that the seat is suitable for an able-bodied adult; `middle` indicating that the seat is a middle seat, and `wheelchair`, indicating that the seat is intended to be occupied directly by a lockable, electric wheelchair and nothing else.

Note that this type only has a single field at the moment, but we choose to model it as a structured type with one field rather than embedding the enumerated field directly where this type is used, to allow for the possibility of adding new, optional fields in the future.

### Assignment Fields

An Assignment indicates a specific matching between a Vehicle and a Demand.

| Name | Type | Description
|------|--------|------
| id | string | This Assignment's ID
| vehicle_id | string | The Vehicle to which this Assignment is made
| demand_id | string | The Demand to which this Assignment is made
| pick_up_at_time | datetime | The time at which this assigned ride is estimated to begin
| pick_up_at_location | [PostalAddress](people.html#postal-addresses) | The location at which this assigned will begin
| drop_off_at_time | datetime | The time at which this assigned ride is estimated to end
| drop_off_at_location | [PostalAddress](people.html#postal-addresses) | The specific location at which this assigned ride will end
| return_assignment_id | string* | If set, the ID of the Assignment which will return the demanding riders to their next location. Typically the next location will be the same one from which the riders departed, but it may be different (example: voter departs from home but is returned after voting to their place of work or school).

### Interval Fields

| Name | Type | Description
|------|--------|------
| start | datetime | The time at which this interval begins (inclusive)
| end | datetime | The time at which this interval ends (exclusive)

Intervals determine a discrete and continuous amount of time during which a ride can occur (or more generally, when a thing can occur). Intervals are valid if and only if `start < end`.
