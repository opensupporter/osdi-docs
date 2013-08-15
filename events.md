# Events

This page defines Events, EventRSVPS

## Events

| Name		| Type		| Description
|-----------|-----------|------------------
| id		| string	| Identifier of the event
| status	| string	| Status of the event.  Possible values are:
|			|			| "confirmed" The Event is confirmed (Default)
|			|			| "tentative"
|			|			| "cancelled"
| created	| datetime	| Date and Time of creation
| updated	| datetime	| Date and Time of update
| summary	| string	| title / summary of event
| description| string	| description of the event
| location	| Address	| A single instance of Address representing the location of the event
| creator	| Person	| A single instance of Person representing the creator of the event
| organizer | Person	| A single instance of Person representing the organizer of the event
| start		| datetime	| start time for the event
| end		| datetime	| end time for the event
| all_day_date| date	| date only for all day events
| all_day	| boolean	| true if the event is an all day event
| recurrence| TBD		| TBD
| transparence| string	| Whether the event blocks time on the calendar. Optional. Possible values are:
|			|			| "opaque" - The event blocks time on the calendar. This is the default value.
|			|			| "transparent" - The event does not block time on the calendar.
| visibility| string	| Visibility of the event.  Possible values are
|			|			| "public" visible on public web interfaces
|			|			| "private" not visible on public web interfaces
| attendees	| Attendance[]| A Collection of Attendance resources
| guestsCanInviteOthers | boolean | Attendees can invite guests to the event
| reminders | list		| a list of reminder elements
| .method	| string	| "email", "sms"
| .minutes	| integer	| number of minutes before the start of the event to send reminder

## Attendance

| Name		| Type		| Description
|-----------|-----------|------------------
| id		| string	| Identifier
| event		| Event*	| Event that this attendance refers to
| person	| Person*	| Person that is attending the referenced event
| status	| string	| The attendee's response status. Possible values
| 			|			| "declined" The attendee declined
|			|			| "tentative" The attendee tentatively accepted
|			|			| "accepted" The attendee accepted
|			|			| "no show" The attendee did not show up
|			|			| "needs action" The attendee needs help
| comment	| string	| An optional comment from the attendee
|

# JSON

	{
	  "id": string,
	  "status": string,
	  "created": datetime,
	  "updated": datetime,
	  "summary": string,
	  "description": string,
	  "_embedded" : {
			"location" : {
				"address1": "430 Erwin Stream",
	            "city": "Altheastad",
	            "state": "FL",
	            "postal_code": "87210-9039",
	            "country_code": "UK",
	            "address_type": "Home",
	            "lat": 44,
	            "lng": 40,
	            "accuracy": "Rooftop",
	            "address_status": "Verified",
	            "primary": true,
	            "_links": {
	              "self": {
	                "href": "http://api.opensupporter.org/api/v1/addresses/42"
	              },
	              "person": {
	                "href": "http://api.opensupporter.org/api/v1/people/21"
	              }
	            }
	  "_embedded" : {
		"creator" :   {
            {
	        "first_name": "Lurline",
	        "last_name": "Glover",
	        "middle_name": "Titus",
	        "email": "test-1@example.com",
	        "gender": "Male",
	        "sex": "Female",
	        "twitter_handle": "@Lurline_Glover",
	        "guid": "c199e4a0-b562-0130-dc7c-168c51e904de",
	        "_embedded": {
	          "primary_address": {
	            "address1": "430 Erwin Stream",
	             ...
	          },
      "_embedded" : {
		"organizer" :   {
            {
	        "first_name": "Lurline",
	        "last_name": "Glover",
	        "middle_name": "Titus",
	        "email": "test-1@example.com",
	        "gender": "Male",
	        "sex": "Female",
	        "twitter_handle": "@Lurline_Glover",
	        "guid": "c199e4a0-b562-0130-dc7c-168c51e904de",
	        "_embedded": {
	          "primary_address": {
	            "address1": "430 Erwin Stream",
	             ...
	          },
	  "start": datetime,
	  "end" : datetime,
      "all_day" : boolean,
      "all_day_date" : date,

	  "transparency": string,
	  "visibility": string,
	  "_embedded" : {
	       "attendance": [
                {
					"_links" : { 
						"event" : {"href" : uri }
					},
					"_embedded" : {
						"person": {
							
			            
				        "first_name": "Lurline",
				        "last_name": "Glover",
				        "middle_name": "Titus",
				        "email": "test-1@example.com",
				        "gender": "Male",
				        "sex": "Female",
				        "twitter_handle": "@Lurline_Glover",
				        "guid": "c199e4a0-b562-0130-dc7c-168c51e904de",
				        "_embedded": {
				          "primary_address": {
				            "address1": "430 Erwin Stream",
				             ...
				          }
		        
              			}
					}
					]
	  "guestsCanInviteOthers": boolean,
	  "privateCopy": boolean,
	  "locked": boolean,
	  "reminders": [
			{
				method : "email",
				minutes : "1440"
	        },
			{
				method : "sms",
				minutes : "120"
	        }

	    ],
	  },
	  "_links" : {
       "self": { "href" : uri },
       "attendance" : { "href" : uri }
       "location" : { "href" : uri } 
      }

	}
	

