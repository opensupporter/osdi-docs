# Interactions

Interactions are instances of one person engaging another person. An example of this would be as follows.  Alice makes a telephone call to Bob.  On that call she asks Bob a question and records his response.  The Interaction is primarily associated with Alice via the person attribute as she is the one who took action.  Bob answered the question and is considered the prospect.  The Interaction is secondarily associated with Bob via the prospect attribute.  

# Attributes

| Name			| Type 		| Description
|-----------	|-----------|-----------------------
| contactedBy	| Person*	| Reference to the person who completed this interaction, eg the person who asked the question (null allowed)
| prospect		| Person*	| Reference to the person the canvasser interacted with.  eg, the person who was asked the question (null allowed)
| coder 		| Person*	| Reference to the person that entered the data about this interaction (null allowed)
| attempt_type	| string	| Flexenum of "Call", "Email","Canvass","Web", "Other"
| attempt_result| string	| Flexenum of "Completed", "Unreachable", "Left Message"
| retryable     | boolean   | Is this interaction retryable?
| donations		| Donation[] | Associated donations
| attendances 	| Attendance[]| Associated event attendances
| attempt_time  | DatTime   | The date this was attempted
| question_answers| QuestionAnswer[]| Associated answered questions
