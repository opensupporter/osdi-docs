#### Return Response

> see issue [325](https://github.com/opensupporter/osdi-docs/issues/325)

When mapping OSDI to certain systems, an extra proprietary API call may be necessary to return the resource representation when doing an OSDI POST, PUT, PATCH, Helper or other function.  An OSDI client that does not need the representation can set this as false so a proxy or middleware server can avoid this extra call.

While OSDI clients may be uninterested in the attribute vvalues, the clients may be interested in navigating links to related collections.  Therefore, instead of the representation, the proxy may return the self link, related links, and identifiers, or an empty response.

##### Request

````
POST https://osdi-sample-system.org/api/v1/people/

Header:
OSDI-API-Token:[your api key here]

{
   "osdi:control": {
      "return_response": false  /* default is true if not specified */
   },
    "identifiers": [
        "foreign_system:1"
    ],
    "family_name": "Edwin",
    "given_name": "Labadie",
    "additional_name": "Marques",
    "origin_system": "OpenSupporter",
````

##### Response

````
200 OK

Content-Type: application/hal+json
Cache-Control: max-age=0, private, must-revalidate

{
    "identifiers": [
        "osdi_sample_system:d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        ],
    "_links": {
        "self": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3"
        },
        "osdi:attendances": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/attendances"
        },
        "osdi:donations": {
            "href": "https://osdi-sample-system.org/api/v1/people/d91b4b2e-ae0e-4cd3-9ed7-d0ec501b0bc3/donations"
            }
        }
    }
}
````
