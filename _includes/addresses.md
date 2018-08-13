#### Postal Addresses

|Name          |Type      |Description
|-----------    |-----------|--------------
|postal_addresses.primary	|boolean	|Denotes if this is the primary address. A person can have only one primary address.
|postal_addresses.address_type	|enum	|The type of address. One of "Home", "Work", or "Mailing".
|postal_addresses.venue	|string	|Optional venue name at the address, useful for names of buildings. (ex: Smith Hall)
|postal_addresses.address_lines	|strings[]	|An array of strings representing the person's street address.
|postal_addresses.locality	|string	|A city or other local administrative area.
|postal_addresses.region	|string	|State or subdivision codes according to ISO 3166-2 (Final 2 alpha digits).
|postal_addresses.postal_code	|string	|The region specific postal code, such as a zip code.
|postal_addresses.country	|string	|The country code according to ISO 3166-1 Alpha-2.
|postal_addresses.language	|string	|Language in which the address is recorded -- language code according to ISO 639.
|postal_addresses.location |object	|An object hash representing the geocoded location information for the address.
|postal_addresses.location.latitude	|float	|A positive or negative float number representing the latitude of the address.
|postal_addresses.location.longitude	|float	|A positive or negative float number representing the longitude of the address.
|postal_addresses.location.accuracy	|enum	|A value representing the accuracy of the geocode. One of "Rooftop" or "Approximate".
|postal_addresses.status	|enum	|A value representing the status of the address. One of "Potential", "Verified", "Bad", or "Past".
|postal_addresses.last_verified_date  |datetime   |A value representing the last verified date of the address.

#### Email Addresses

|Name          |Type      |Description
|-----------    |-----------|--------------
|email_addresses.primary	|boolean	|Denotes if this is the primary address. A person can have only one primary address.
|email_addresses.address	|string	|The email address for the person.
|email_addresses.address_type	|flexenum	|The type of email address. One of "personal", "work", "other", or another value.
|email_addresses.status	|enum	|Indicates whether this email address is subscribed to receive emails in the system, either on one or more email lists. One of "subscribed", "unsubscribed", "bouncing", "spam complaints".

#### Phone Numbers

|Name          |Type      |Description
|-----------    |-----------|--------------
|phone_numbers.primary	|string   |Denotes if this is the primary phone number. A person can have only one primary number.
|phone_numbers.number	|string   |The phone number of the person. Must including country code and must be numeric characters only.
|phone_numbers.extension	|string   |An optional associated extension for the number.
|phone_numbers.description	|string   |A freeform description of the phone number.
|phone_numbers.number_type	|flexenum   |The type of phone number. One of "Home", "Work", "Mobile", "Other", "Daytime", "Evening", "Fax", or another value.
|phone_numbers.operator	|string   |The operator or carrier associated with the number. _Example: "Verizon"_
|phone_numbers.country	|string   |The country code according to ISO 3166-1 Alpha-2.
|phone_numbers.sms_capable	|boolean   |True if the number can accept SMS text messages.
|phone_numbers.do_not_call	|boolean   |True if this number is registered on the US FCC Do Not Call Registry.