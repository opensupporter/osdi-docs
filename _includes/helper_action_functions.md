
Helper Action Functions are additional actions that the OSDI server will perform along with inserting or updating the associated person.

|Name          |Type      |Description
|-----------    |-----------|--------------
|add_tags      |strings[]     |An array of tag names corresponding to previously created tags to add to this person when it is created.
|add_tags_uri  |strings[]     |An array of tag URIs corresponding to previously created tags to add to this person when it is created.
|add_lists     |strings[]     |An array of list names corresponding to previously created lists to add to this person when it is created.
|add_lists_uri     |strings[]     |An array of list URIs corresponding to previously created lists to add to this person when it is created.
|add_questions_responses_uri      |[QuestionResponseObject](#question-response-object-fields)     |An array of Question Response Objects, indicating answers which should be applied to the person.
|triggers		|[Triggers](#triggers)	|An object hash representing responses a user would like to trigger from the server as part of the POST, such as sending an autoresponse email back to the person who took action with this helper.

#### Question Response Object Fields

|Name          |Type      |Description
|-----------    |-----------|--------------
|question      |string     |The identifier for the [Question](questions.html) which is being answered
|responses     |string[]   |One or more responses to the Question, if the corresponding question_type is SingleChoice or MultiChoice; should be an improper subset of the responses available for the question
|value          |string    |A free-text response to the question, if the corresponding question_type is Paragraph.


#### Triggers

Here autoresponse identifiers are handled independent of the OSDI specification's identifier schema. The autoresponse sent is determined by the server that is being interacted with, the system, and the `id`. 
Three types of autoresponse triggers are defined below and those types should follow this specification and format.

|Name          |Type      |Description
|-----------    |-----------|--------------
|autoresponse   |object     |An object hash representing the autoresponse email trigger type.
|autoresponse.enabled   |boolean     |A boolean indicating whether the autoresponse email should be sent or not.
|autoresponse.identifiers |strings[]     | A unique string array of identifiers in the format `[system name]:[id]`.

|Name          |Type      |Description
|-----------    |-----------|--------------
|sms_response |object     |An object hash representing the autoresponse sms trigger type.
|sms_response.enabled   |boolean     |A boolean indicating whether the autoresponse sms should be sent or not.
|sms_response.identifiers |strings[]     | A unique string array of identifiers in the format `[system name]:[id]`.

|Name          |Type      |Description
|-----------    |-----------|--------------
|call_response |object     |An object hash representing the autoresponse call trigger type.
|call_response.enabled   |boolean     |A boolean indicating whether the autoresponse call should be sent or not.
|call_response.identifiers |strings[]     | A unique string array of identifiers in the format `[system name]:[id]`.