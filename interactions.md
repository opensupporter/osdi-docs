---
layout: default
title: "Canvassing Interactions"
---
# Interactions

Interactions are instances of one person engaging another person. An example of this would be as follows.  Alice makes a telephone call to Bob.  On that call she asks Bob a question and records his response.  The Interaction is primarily associated with Alice via the person attribute as she is the one who took action.  Bob answered the question and is considered the prospect.  The Interaction is secondarily associated with Bob via the prospect attribute.  

# Attributes

| Name			| Type 		| Description
|-----------	|-----------|-----------------------
| created_date	| datetime	| Date and Time of creation
| modified_date	| datetime	| Date and Time of last modification
| action_date | datetime    | Date and Time the interaction was made with the prospect
| canvasser		| Person*	| Reference to the person who completed this interaction, eg the person who asked the question
| prospect		| Person*	| Reference to the person the canvasser interacted with.  eg, the person who was asked the question
| attempt_type	| string	| One of "Call", "Email","Canvass","Web", "Other"
| attempt_result| string	| One of "Completed", "Unreachable", "Left Message"
| donations		| Donation[]* | Associated donations
| attendances 	| Attendance[]*| Associated event attendances
| question_answers| QuestionAnswer[]*| Associated answered questions
| foos			| Foo[]*		| There may be additonal collections of objects associated with an interaction
