
#Employment

This page defines Employment objects.

Employment objects are designed to carry detailed information about a persons employment information.  This is particularly useful for labor organizations and services that need to track detailed information about where a person works, their shift, job title, employment status, etc. 

## Employment

| Name		| Type		| Description
|-----------|-----------|------------------
| identifiers	| Identifier[]	| An array of identifiers the provider has determined to be associated with this employment.
| created_at	| datetime	| Date and Time of creation
| modified_at	| datetime	| Date and Time of last modification
| origin_system | string  | Human readable identifier of the system where this information originated.
| parent_employer | string  | Human readable name of the parent employer. An example of a parent employer might be "Kroger"
| worksites  | Worksite[]  | A collection of worksites that this person works at.
| employment_status	| enum	| Provides a repesentation of the person's employment status at this employer. "full_time", "part_time", "loa"
| terminated	| bool	| If a persons employment with this employer has been terminated this value shall be true.
| shift	| Shift	| An object representing the shift a person works. 
| work_area	| string[]	| A human readable list of work areas in which this person works.
| departments	| string[]	| A human readable list of departments in which this person works.
| job_title	| string	| A human readable name of the job title a person holds with this employer. An example would be "Department Manager"
| start_date	| datetime	| The date a person started employment with this employer.
| end_date	| datetime	| The date a person terminated employment with this employer.

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
