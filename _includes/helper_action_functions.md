
|Name          |Type      |Description
|-----------    |-----------|--------------
|add_tags      |strings[]     |An array of tag names corresponding to previously created tags to add to this person when it is created.
|add_tags_uri  |strings[]     |An array of tag URIs corresponding to previously created tags to add to this person when it is created.
|add_lists     |strings[]     |An array of list names corresponding to previously created lists to add to this person when it is created.
|add_lists_uri     |strings[]     |An array of list URIs corresponding to previously created lists to add to this person when it is created.
|add_questions_responses_uri      |[AnswerActionFunction](#answer-action-function-fields)     |An array of Person Signup Helper Answer objects, indicating answers which should be applied to the Person at the moment of signup
|triggers		|[Triggers](#triggers)	|An object hash representing responses a user would like to trigger from the server as part of the POST, such as sending an autoresponse email back to the person who took action with this helper.

### Answer Action Function Fields

|Name          |Type      |Description
|-----------    |-----------|--------------
|question      |string     |The identifier for the [Question](questions.html) which is being answered
|responses     |string[]   |One or more responses to the Question, if the corresponding question_type is SingleChoice or MultiChoice; should be an improper subset of the responses available for the question
|value          |string    |A free-text response to the question, if the corresponding question_type is Paragraph.


#### Triggers

|Name          |Type      |Description
|-----------    |-----------|--------------
|autoresponse   |object     |An object hash representing the autoresponse email trigger type.
|autoresponse.enabled   |boolean     |A boolean indicating whether the autoresponse email should be sent or not.
