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




'''