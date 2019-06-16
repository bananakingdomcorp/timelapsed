'''


API DOCUMENTATION:


routes:

/auth: General route for authentication.

Accepted verbs: POST

/auth/convert-token: Converts an Oauth Token to a bearer token that you can use.

/users:

Accepted verbs: POST.

Success: User has been added to the DB, will return a 201.

Failure: User already exists, will return a 400.


/topic:

Accepted verbs: POST, PUT, DELETE

POST: 

Accepts 'Name', a string. 

Returns: {'Data': {'id': id of created Topic, 'Name': Name Given, 'Cards': []}}, Cards is always empty. Status code 201. 

PUT: 

Accepts ('SwitchPosition', 'Name')

SwitchPosition: 

Required = False

ID of a topic that you want to switch the current pk with. 

Name:

Required = False

Name that you want to change your topic to. 

Either SwitchPostion or Name is required. 

Returns: Either SwitchPosition, Name, or Both, depending on which is changed.  Status Code 200.


DELETE:

Deletes on PK. Status code 204. No Payload. 


/card:

Accepted Verbs: POST, PUT, DELETE

POST: 

Accepts: (Data, Times)

Data: ('Name', 'Description', 'Topic')


Name: Name you are giving this card

Description: Description of this card

Topic: PK of the Topic that you are putting this card in. 


Times: ('Day', 'Begin_Date', 'Num_Weeks', 'Weeks_Skipped', 'Begin_Time', 'End_Time'). Not required. 


Day: Day of the week. 

Begin_Date: Python Datetime, only use year month day.

Num_Weeks: Weeks to run this card. Not required, will default to zero. 

Weeks_Skipped: Weeks skipped between running this card. NOt required, will default to zero. 

Begin_Time: Starting time.  Python Timefield, just hour and minute. 

End_Time: Ending Time. Python Timefield, just hour and minute. 


Returns: {'Data': {'Name': name of card, 'Description': description of card}, 'ids': [id of every created datetime, add to your redux], 'id': id of the card you just created}


PUT: 

Accepts: ('Data', 'Times'). 

Both are optional, although one or the other is required. 

Data: 

('Switch_Topic', 'Switch_Position', 'Description', 'Name' ). 

All are optional, although one is required. If you are not changing any of this data, omit 'Data' entirely. 

'Switch_Topic': ID of the topic you want to switch positions with. 

'Switch_Position': ID of the Card you want to switch positions with. 

'Description': String that gives our new description.

'Name': String that gives our new name. 



Times:

('Num_Weeks', 'Weeks_Skipped', 'Begin_Time', 'End_Time')

All are optional, although one is required. If you are not changing any of this data, omit 'Times' entirely. 

'Num_Weeks': Number of weeks

'Weeks_Skipped': Number of weeks to skip

'Begin_Time': Start time of the task

'End_Time': End time of the task.


Returns:

{'Data': {'Name': Name of our card, 'Description': Description of our card}, 'Return_Times': [{'id': id of the time, 'Day': Day for the time, 'Begin_Date': Starting date, 'Num_Weeks': Number of weeks, 'Weeks_Skipped': Weeks skipped, 'Begin_Time': starting time, 'End_Time': ending time. }]}


DELETE: PK of the card to delete, no payload. 


'''