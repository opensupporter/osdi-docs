#People
##Attributes

| Name          | Type      | Description
|-----------    |-----------|--------------
|last_name      |string     |Last name
|first_name     |string     |First name
|middle_initial |string     |Middle Initial
|sex            |string     |A person's gender
|guid           |string     |A globally unique identifier (GUID) for a person
|party          |string     |Party affiliation "democrat", "republican", "independent", "none"
|primary_address|Address    |A single instance of an address reflecting the person's primary address
|primary_phone  |string     |The person's primary phone number
|primary_email  |string     |A person's primary email address
|source         |string     |Information about the source where this person record was acquired.  Eg "Ref74"

##Collections
| Name          | Type      | Description
|-----------    |-----------|--------------
|addresses      |Address[]  |A collection of addresses associated with the person
|emails         |Email[]    |A collection of email addresses associated with the person
|phones         |Phone
|donations      |Donation[] |A collection of donations associated with the person
|question_answers|QuestionAnswer[]|A collection of answers to questions from surveys
|eventAttendance |Attendance[]|A collection of attendance records for a person
|interactions   |Interaction[]|A collection of outreach interactions for a person, eg Volunteer Joe called voter Sam

