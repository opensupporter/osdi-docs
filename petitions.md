# Petitions

This page defines Petitions, Petition Signatures

## Petitions

| Name		| Type		| Description
|-----------|-----------|------------------
| identifiers	| Identifier[]	| A collection of identifiers the provider has determined to be associated with the petition
| created_at	| datetime	| Date and Time of creation
| modified_at	| datetime	| Date and Time of last modification
| summary	| string	| title / summary of petition
| description	| string/html string	| description of the petition, optionally an HTML string
| petition_text	| string	| Text of the petition, to be delivered to the target
| url	| string	| A URL string pointing to the publicly available petition page on the web
| total_signatures	| integer	| Read-only computed property representing the current count of petition signatures
| target	| Target[]	| A collection of hashes representing the target(s) of the petition
| .name	| string	| The name of the target
| creator	| Person*	| A single embedded instance of a person representing the creator of the petition
| signatures	| Signatures[]| A Collection of Signature resources

## Signatures

| Name		| Type		| Description
|-----------|-----------|------------------
| identifiers	| Identifier[]	| A collection of identifiers the provider has determined to be associated with the petition
| created_at	| datetime	| Date and Time of creation
| modified_at	| datetime	| Date and Time of last modification
| comments	| string	| The comments left when the signature was created
| person	| Person*	| An embedded person that signed the referenced petition
| petition	| Petition*	| An embedded  reference to the petition this signature is related to


# Retrieving Resources (GET)

## Default embed policy

When retreiving a petition resource, the creator can be embededed, but the signatures collection should only be linked.

When retreiving a signature or list of signatures, both the person and the petition related to the signature can be embedded.

## A list of petitions

Only two shown for brevity.

```
GET /api/v1/petitions/
200 OK
```

```javascript
{
  "total_pages": 6,
  "per_page": 25,
  "page": 1,
  "total_records": 139,
  "_links": {
    "next": {
      "href": "https://api.opensupporter.org/api/v1/petitions?page=2"
    },
    "self": {
      "href": "https://api.opensupporter.org/api/v1/petitions"
    },
    "items": [
      {
        "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
      },
      {
        "href": "https://api.opensupporter.org/api/v1/petitions/7580ac3e-9a72-11e3-a2e9-12313d316c29"
      },
      ...
    ],
    "curies": [
      {
        "name": "osdi",
        "href": "http://api.opensupporter.org/docs/v1/{rel}",
        "templated": true
      }
    ]
  },
  "_embedded": {
    "items": [
      {
        "identifier": [
          "osdi_provider:9b385f65-23b3-47a4-a4b5-9abd537b37a7"
        ],
        "created_at": "2014-02-20T21:30:55Z",
        "modified_at": "2014-02-21T15:36:34Z",
        "summary": "Stop doing the bad thing",
        "description": "<p>Please sign this petition to stop John Smith from doing the bad thing.</p>",
        "petition_text": "John Smith, please stop doing the bad thing now.",
        "url": "https://api.opensupporter.org/petitions/stop-doing-the-bad-thing",
        "total_signatures": 100,
        "target": [
          {
            "name": "John Smith"
          }
        ],
        "_embedded": {
          "osdi:creator": {
            "given_name": "Jane",
            "family_name": "Doe",
            "identifiers": [
              "osdi_provider:c945d6fe-929e-11e3-a2e9-12313d316c29"
            ],
            "email_addresses": [
              {
                "primary": true,
                "address": "jane.doe@gmail.com"
              }
            ],
            "postal_addresses": [
              {
                "primary": true,
                "address_lines": [
                  "123 Something Rd."
                ],
                "locality": "Washington",
                "region": "DC",
                "postal_code": "20009",
                "country": "US",
                "language": "en",
                "location": {
                  "latitude": 38.919,
                  "longitude": -72.6375,
                  "accuracy": "Approximate"
                }
              }
            ],
            "_links": {
              "self": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
              },
              "osdi:signatures": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures"
              },
              ...
            }
          }
        },
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
          },
          "osdi:signatures": {
            "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures"
          },
          "osdi:creator": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
          }
        }
      },
      {
        "identifier": [
          "osdi_provider:7580ac3e-9a72-11e3-a2e9-12313d316c29"
        ],
        "created_at": "2014-02-14T15:35:59Z",
        "modified_at": "2014-02-14T15:39:12Z",
        "summary": "Bring back the thing we love today!",
        "description": "<p>It's time for Amy Sue to bring back the thing we love. Sign now!</p>",
        "petition_text": "Amy Sue, bring back the thing we love.",
        "url": "https://api.opensupporter.org/petitions/bring-back-the-thing-we-love-today",
        "total_signatures": 4829,
        "target": [
          {
            "name": "Mayor Amy Sue"
          }
        ],
        "_embedded": {
          "osdi:creator": {
            "given_name": "Tom",
            "family_name": "Jones",
            "identifiers": [
              "osdi_provider:c945d6fe-929e-11e3-a2e9-12313d316c29"
            ],
            "email_addresses": [
              {
                "primary": true,
                "address": "tom.jones@gmail.com"
              }
            ],
            "postal_addresses": [
              {
                "primary": true,
                "locality": "New York City",
                "region": "NY",
                "postal_code": "10001",
                "country": "US",
                "language": "en",
                "location": {
                  "latitude": 33.123,
                  "longitude": -76.5432,
                  "accuracy": "Approximate"
                }
              }
            ],
            "_links": {
              "self": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
              },
              "osdi:signatures": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures"
              },
              ...
            }
          }
        },
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/petitions/7580ac3e-9a72-11e3-a2e9-12313d316c29"
          },
          "osdi:signatures": {
            "href": "https://api.opensupporter.org/api/v1/petitions/7580ac3e-9a72-11e3-a2e9-12313d316c29/signatures"
          },
          "osdi:creator": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
          }
        }
      },
      ...
    ]
  }
}
```


## A single petition
```
GET /api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/
200 OK
```

```javascript
{
  {
    "identifier": [
      "osdi_provider:9b385f65-23b3-47a4-a4b5-9abd537b37a7"
    ],
    "created_at": "2014-02-20T21:30:55Z",
    "modified_at": "2014-02-21T15:36:34Z",
    "summary": "Stop doing the bad thing",
    "description": "<p>Please sign this petition to stop John Smith from doing the bad thing.</p>",
    "petition_text": "John Smith, please stop doing the bad thing now.",
    "url": "https://api.opensupporter.org/petitions/stop-doing-the-bad-thing",
    "total_signatures": 100,
    "target": [
      {
        "name": "John Smith"
      }
    ],
    "_embedded": {
      "osdi:creator": {
        "given_name": "Jane",
        "family_name": "Doe",
        "identifiers": [
          "osdi_provider:c945d6fe-929e-11e3-a2e9-12313d316c29"
        ],
        "email_addresses": [
          {
            "primary": true,
            "address": "jane.doe@gmail.com"
          }
        ],
        "postal_addresses": [
          {
            "primary": true,
            "address_lines": [
              "123 Something Rd."
            ],
            "locality": "Washington",
            "region": "DC",
            "postal_code": "20009",
            "country": "US",
            "language": "en",
            "location": {
              "latitude": 38.919,
              "longitude": -72.6375,
              "accuracy": "Approximate"
            }
          }
        ],
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
          },
          "osdi:signatures": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures"
          },
          ...
        }
      }
    },
    "_links": {
      "self": {
        "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
      },
      "osdi:signatures": {
        "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures"
      },
      "osdi:creator": {
        "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
      }
    }
  }
}
```

## A list of signatures on a petition

Only two shown for brevity.

```
GET /api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures
200 OK
```

```javascript
{
  "total_pages": 4,
  "per_page": 25,
  "page": 1,
  "total_records": 100,
  "_links": {
    "self": {
      "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures"
    },
    "next": {
      "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures/?page=2"
    },
    "items": [
      {
        "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures/25d2d08f-7c3a-4bdc-8329-815aa5117d54"
      },
      {
        "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures/13d2d08f-6c3a-3bec-8628-515aa5147e57"
      },
      ...
    ],
    "curies": [
      {
        "name": "osdi",
        "href": "http://api.opensupporter.org/docs/v1/{rel}",
        "templated": true
      }
    ]
  },
  "_embedded": {
    "items": [
      {
        "identifier": [
          "osdi_provider:25d2d08f-7c3a-4bdc-8329-815aa5117d54"
        ],
        "created_at": "2014-02-20T21:32:56Z",
        "modified_at": "2014-02-20T21:32:56Z",
        "comments": "Stop the bad thing, please!",
        "_embedded": {
          "osdi:person": {
            "given_name": "Ellen",
            "family_name": "Omonaria",
            "identifiers": [
              "osdi_provider:c945d6fe-929e-11e3-a2e9-12313d316c29"
            ],
            "created_at": "2013-03-14T13:03:25Z",
            "modified_at": "2014-02-26T21:01:52Z",
            "email_addresses": [
              {
                "primary": true,
                "address": "ellen.omonaria@gmail.com"
              }
            ],
            "postal_addresses": [
              {
                "primary": true,
                "locality": "Washington",
                "region": "DC",
                "postal_code": "20009",
                "country": "US",
                "language": "en",
                "location": {
                  "latitude": 33.333,
                  "longitude": -77.7777,
                  "accuracy": "Approximate"
                }
              }
            ],
            "_links": {
              "self": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
              },
              "osdi:signatures": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures"
              }
              ...
            }
          },
          "osdi:petition": {
            "identifier": [
		      "osdi_provider:9b385f65-23b3-47a4-a4b5-9abd537b37a7"
		    ],
		    "created_at": "2014-02-20T21:30:55Z",
		    "modified_at": "2014-02-21T15:36:34Z",
		    "summary": "Stop doing the bad thing",
		    "description": "<p>Please sign this petition to stop John Smith from doing the bad thing.</p>",
		    "petition_text": "John Smith, please stop doing the bad thing now.",
		    "url": "https://api.opensupporter.org/petitions/stop-doing-the-bad-thing",
		    "total_signatures": 100,
		    "target": [
		      {
		        "name": "John Smith"
		      }
		    ],
		    "_embedded": {
		      "osdi:creator": {
		        "given_name": "Jane",
		        "family_name": "Doe",
		        "identifiers": [
		          "osdi_provider:c945d6fe-929e-11e3-a2e9-12313d316c29"
		        ],
		        "email_addresses": [
		          {
		            "primary": true,
		            "address": "jane.doe@gmail.com"
		          }
		        ],
		        "postal_addresses": [
		          {
		            "primary": true,
		            "address_lines": [
		              "123 Something Rd."
		            ],
		            "locality": "Washington",
		            "region": "DC",
		            "postal_code": "20009",
		            "country": "US",
		            "language": "en",
		            "location": {
		              "latitude": 38.919,
		              "longitude": -72.6375,
		              "accuracy": "Approximate"
		            }
		          }
		        ],
		        "_links": {
		          "self": {
		            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
		          },
		          "osdi:signatures": {
		            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures"
		          },
		          ...
		        }
		      }
		    },
		    "_links": {
		      "self": {
		        "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
		      },
		      "osdi:signatures": {
		        "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures"
		      },
		      "osdi:creator": {
		        "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
		      }
		    }
          }
        },
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures/25d2d08f-7c3a-4bdc-8329-815aa5117d54"
          },
          "osdi:petition": {
            "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
          },
          "osdi:person": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
          }
        }
      },
      {
        "identifier": [
          "osdi_provider:13d2d08f-6c3a-3bec-8628-515aa5147e57"
        ],
        "created_at": "2014-02-20T21:32:56Z",
        "modified_at": "2014-02-20T21:32:56Z",
        "comments": "Please don't do it.",
        "_embedded": {
          "osdi:person": {
            "given_name": "James",
            "family_name": "Gonter",
            "identifiers": [
              "osdi_provider:35ad5d6ed-913e-12e6-a2e8-11673r314c14"
            ],
            "created_at": "2013-03-14T13:03:25Z",
            "modified_at": "2014-02-26T21:01:52Z",
            "email_addresses": [
              {
                "primary": true,
                "address": "james.gonter@gmail.com"
              }
            ],
            "postal_addresses": [
              {
                "primary": true,
                "locality": "Washington",
                "region": "DC",
                "postal_code": "20009",
                "country": "US",
                "language": "en",
                "location": {
                  "latitude": 33.332,
                  "longitude": -77.7177,
                  "accuracy": "Approximate"
                }
              }
            ],
            "_links": {
              "self": {
                "href": "https://api.opensupporter.org/api/v1/people/35ad5d6ed-913e-12e6-a2e8-11673r314c14"
              },
              "osdi:signatures": {
                "href": "https://api.opensupporter.org/api/v1/people/35ad5d6ed-913e-12e6-a2e8-11673r314c14/signatures"
              }
              ...
            }
          },
          "osdi:petition": {
            "identifier": [
		      "osdi_provider:9b385f65-23b3-47a4-a4b5-9abd537b37a7"
		    ],
		    "created_at": "2014-02-20T21:30:55Z",
		    "modified_at": "2014-02-21T15:36:34Z",
		    "summary": "Stop doing the bad thing",
		    "description": "<p>Please sign this petition to stop John Smith from doing the bad thing.</p>",
		    "petition_text": "John Smith, please stop doing the bad thing now.",
		    "url": "https://api.opensupporter.org/petitions/stop-doing-the-bad-thing",
		    "total_signatures": 100,
		    "target": [
		      {
		        "name": "John Smith"
		      }
		    ],
		    "_embedded": {
		      "osdi:creator": {
		        "given_name": "Jane",
		        "family_name": "Doe",
		        "identifiers": [
		          "osdi_provider:c945d6fe-929e-11e3-a2e9-12313d316c29"
		        ],
		        "email_addresses": [
		          {
		            "primary": true,
		            "address": "jane.doe@gmail.com"
		          }
		        ],
		        "postal_addresses": [
		          {
		            "primary": true,
		            "address_lines": [
		              "123 Something Rd."
		            ],
		            "locality": "Washington",
		            "region": "DC",
		            "postal_code": "20009",
		            "country": "US",
		            "language": "en",
		            "location": {
		              "latitude": 38.919,
		              "longitude": -72.6375,
		              "accuracy": "Approximate"
		            }
		          }
		        ],
		        "_links": {
		          "self": {
		            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
		          },
		          "osdi:signatures": {
		            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures"
		          },
		          ...
		        }
		      }
		    },
		    "_links": {
		      "self": {
		        "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
		      },
		      "osdi:signatures": {
		        "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures"
		      },
		      "osdi:creator": {
		        "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
		      }
		    }
          }
        },
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures/13d2d08f-6c3a-3bec-8628-515aa5147e57"
          },
          "osdi:petition": {
            "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
          },
          "osdi:person": {
            "href": "https://api.opensupporter.org/api/v1/people/35ad5d6ed-913e-12e6-a2e8-11673r314c14"
          }
        }
      },
      ...
    ]
  }
}
```


## A single signature on a petition

```
GET /api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures/25d2d08f-7c3a-4bdc-8329-815aa5117d54
200 OK
```
```javascript
{
  "_links": {
    "self": {
      "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures/25d2d08f-7c3a-4bdc-8329-815aa5117d54"
    },
    "curies": [
      {
        "name": "osdi",
        "href": "http://api.opensupporter.org/docs/v1/{rel}",
        "templated": true
      }
    ]
  },
  "_embedded": {
    "items": [
      {
        "identifier": [
          "osdi_provider:25d2d08f-7c3a-4bdc-8329-815aa5117d54"
        ],
        "created_at": "2014-02-20T21:32:56Z",
        "modified_at": "2014-02-20T21:32:56Z",
        "comments": "Stop the bad thing, please!",
        "_embedded": {
          "osdi:person": {
            "given_name": "Ellen",
            "family_name": "Omonaria",
            "identifiers": [
              "osdi_provider:c945d6fe-929e-11e3-a2e9-12313d316c29"
            ],
            "created_at": "2013-03-14T13:03:25Z",
            "modified_at": "2014-02-26T21:01:52Z",
            "email_addresses": [
              {
                "primary": true,
                "address": "ellen.omonaria@gmail.com"
              }
            ],
            "postal_addresses": [
              {
                "primary": true,
                "locality": "Washington",
                "region": "DC",
                "postal_code": "20009",
                "country": "US",
                "language": "en",
                "location": {
                  "latitude": 33.333,
                  "longitude": -77.7777,
                  "accuracy": "Approximate"
                }
              }
            ],
            "_links": {
              "self": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
              },
              "osdi:signatures": {
                "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures"
              }
              ...
            }
          },
          "osdi:petition": {
            "identifier": [
		      "osdi_provider:9b385f65-23b3-47a4-a4b5-9abd537b37a7"
		    ],
		    "created_at": "2014-02-20T21:30:55Z",
		    "modified_at": "2014-02-21T15:36:34Z",
		    "summary": "Stop doing the bad thing",
		    "description": "<p>Please sign this petition to stop John Smith from doing the bad thing.</p>",
		    "petition_text": "John Smith, please stop doing the bad thing now.",
		    "url": "https://api.opensupporter.org/petitions/stop-doing-the-bad-thing",
		    "total_signatures": 100,
		    "target": [
		      {
		        "name": "John Smith"
		      }
		    ],
		    "_embedded": {
		      "osdi:creator": {
		        "given_name": "Jane",
		        "family_name": "Doe",
		        "identifiers": [
		          "osdi_provider:c945d6fe-929e-11e3-a2e9-12313d316c29"
		        ],
		        "email_addresses": [
		          {
		            "primary": true,
		            "address": "jane.doe@gmail.com"
		          }
		        ],
		        "postal_addresses": [
		          {
		            "primary": true,
		            "address_lines": [
		              "123 Something Rd."
		            ],
		            "locality": "Washington",
		            "region": "DC",
		            "postal_code": "20009",
		            "country": "US",
		            "language": "en",
		            "location": {
		              "latitude": 38.919,
		              "longitude": -72.6375,
		              "accuracy": "Approximate"
		            }
		          }
		        ],
		        "_links": {
		          "self": {
		            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
		          },
		          "osdi:signatures": {
		            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29/signatures"
		          },
		          ...
		        }
		      }
		    },
		    "_links": {
		      "self": {
		        "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
		      },
		      "osdi:signatures": {
		        "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures"
		      },
		      "osdi:creator": {
		        "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
		      }
		    }
          }
        },
        "_links": {
          "self": {
            "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7/signatures/25d2d08f-7c3a-4bdc-8329-815aa5117d54"
          },
          "osdi:petition": {
            "href": "https://api.opensupporter.org/api/v1/petitions/9b385f65-23b3-47a4-a4b5-9abd537b37a7"
          },
          "osdi:person": {
            "href": "https://api.opensupporter.org/api/v1/people/c945d6fe-929e-11e3-a2e9-12313d316c29"
          }
        }
      }
    ]
  }
}
```


# Adding/Modifying/Removing Resources (POST/PATCH/PUT/DELETE)

>TBD