## Use-Case and User Scenarios
### 1. Patient(User) can sign up or register new account

#### User visit a sign-up / register page :
- - -
* **Frontend Actions**: user input first_name, last_name, email and password and click register
* --
* --
* --
- - -
* **Backend Actions**: gets input data from frontend as POST data
* checks if the email input is valid
* checks if the password meets user requirements ()
* checks if email exists in db
* hash password
* commit data to database
* --
* --

### 2. User login with email and password

#### User visit the login page
- - -
* **Frontend Actions**: user inputs email and password and clicks login
* --
* --
* --
- - -
* **Backend Actions**: gets email and password from the frontend post request
* check if email is in correct syntax
* check if email exist in database
* un-hash password associated with email in database and compare to password input
* generate 12 twelve hour token with email and account type
* --
* --
