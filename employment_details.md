
#Employment

This page defines Employment objects.  

This is not to be conflated with the `employer` field defined on the person object as the `Employment` object serves a different purpose.  The `employer` string defined on a person object is used primarily to track where a person works for FEC reporting purposes.  

Employment objects are designed to carry very detailed information about a persons employment information.  In practice, the use case for this object is largely limited to labor organizations which need to know much more about a persons employment than simply the name of their employer and occupation. The Employment object seeks to provide a standard for transmitting this information between systems which support detailed employment information. 

A person may have multiple `Employment` resources attached to them.  Generally, there should only be one resource for each unique parent employer.  For example, if a person works for two different employers it is possible that they will have two different `Employment` resources attached to them.  

Given that it is fairly common for a person to work for the same employer but in multiple locations, such as a professor who teaches at multiple campuses, the client should attempt to handle this by creating additional `Worksite` objects under the `Employment` object. 

However,  if the same professor teachers for two different universities, this professor should have two seperate `Employment` objects, one for each university. 

## Employment

| Name		| Type		| Description
|-----------|-----------|------------------
| identifiers	| Identifier[]	| An array of identifiers the provider has determined to be associated with this employment.
| created_at	| datetime	| Date and Time of creation
| modified_at	| datetime	| Date and Time of last modification
| origin_system | string  | Human readable identifier of the system where this information originated.
| parent_employer | string  | Human readable name of the parent employer. An example of a parent employer might be "American University"
| worksites  | Worksite[]  | A collection of worksites at which this person works. 
| employment_status	| flexenum	| Provides a repesentation of the person's employment status at this employer. A value of "Part Time", "Full Time", "LOA"
| shift	| Shift	| An object representing the shift a person works.
| departments	| string[]	| A human readable list of departments in which this person works.
| job_title	| string	| A human readable name of the job title a person holds with this employer. IE "Department Manager"
| terminated	| bool	| If a persons employment with this employer has been terminated this value shall be true.
| start_date	| datetime	| The date a person started employment with this employer.
| termination_date	| DateTime	| The date that their employment was terminated. 

## Worksite

| Name		| Type		| Description
|-----------|-----------|------------------
| identifiers	| Identifier[]	| An array of identifiers the provider has determined to be associated with this worksite
| created_date	| datetime	| Date and Time of creation
| modified_date	| datetime	| Date and Time of last modification
| address	| Address	| The physical address of this worksite.

## Shift

| Name		| Type		| Description
|-----------|-----------|------------------
| identifiers	| Identifier[]	| An array of identifiers the provider has determined to be associated with this shift
| created_date	| datetime	| Date and Time of creation
| modified_date	| datetime	| Date and Time of last modification
| name	| string	| A human readable representation of the shift name, such as "Day"
| shift_starts | int | A value between 0-23 representing the hour at which this shift starts.
| shift_ends | int | A value between 0-23 representing the hour at which this shift ends.
