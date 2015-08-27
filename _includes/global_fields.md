### Common Fields

A set of common fields that appear on all resources is included first, for reference.

| Name          | Type      | Description
|-----------    |-----------|-----------|--------------
|id 			| string    | A string representing a local identifier for the resource on the local system.  It may be a string, integer, guid, etc.  This value MUST be suitable for use in a helper function such as add_tags, add_lists to identify the corresponding resource
|identifiers	|strings[]	|A unique string array of identifiers in the format `[system name]:[id]`. See the general concepts document for more information about identifiers.
|created_date	|datetime   |A read-only property representing the date and time the resource was created on the local system.
|modified_date	|datetime	|A read-only property representing the date and time the resource was last modified on the local system.