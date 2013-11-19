# Employer
Employers is a collection of employer detail objects.  These contain various details for labor.

## Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
| name			| string	| The name of the employer, eg "ACME Widgets"
| id			| guid		| Unique Identifier for the employer
| worksites		| hash[]		| Worksite information
| .id			| guid		| Unique Identifier
| .name			| string	| Name of worksite, eg "Store 10"
| .location		| Address	| The address of the worksite
| .buildings	| hash[]	| Buildings associated with worksite
| ..id			| guid		| Unique Identifier
| ..name		| string	| Name of building "5W"
| .departments	| hash[]	| Departments associated with worksite
| ..id			| guid		| Unique Identifier
| ..name		| string	| Name of building "Manufacturing"
| .bargaining_units| hash[] | Bargaining Units associated with worksite
| ..id			| guid		| Unique Identifier
| ..name		| string	| Name of building "United Widget Makers"
| ..union_local | hash		| Local division of union
| ...id			| guid		| Unique Identifier
| ...name		| string	| Name of building "Local 1"

## JSON Representation

    {
      "id": "guid",
      "name":"ACME Widgets",      
      "worksites":[{
         "id":"guid",
         "name":"West Campus",
         "location":"same as address spec",
         "buildings":[
            {
               "id":"guid",
               "name":"5W"
            },
            {
               "id":"guid",
               "name":"6W"
            }
         ],
         "departments":[
            {
               "id":"guid",
               "name":"Manufacturing"
            },
            {
               "id":"guid",
               "name":"Human Resources"
            }
         ],
         "bargaining_units":[
            {
               "name":"United Widget Makers",
               "id":"guid",
               "union_local":{
                  "name":"Local 1",
                  "id":"guid"
               }
            }
         ]
      ]}
    }