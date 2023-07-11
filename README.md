

# Panorbit Task

## Project Description

The Panorbit Task is a Django project that demonstrates a simple sign-up and login functionality with OTP verification. After successful authentication, the user is redirected to a search page where they can search for information about countries, cities, and country languages.

### Demo Video Link :https://www.veed.io/view/8f152913-e6c0-4f4b-aa6e-b2a7c609929e?panel=share

## Installation and Setup

### Clone the repository:

First, you need to clone the repository to your local machine. You can do this with the following command:

```
git clone https://github.com/Prajna1999/panorbit-task-final.git
```



### Setup Virtual Environment:

This project uses a Python virtual environment. If you're using VS Code, you can create a virtual environment by opening a terminal in VS Code and running the following command:

```
python -m venv venv
```

This will create a new virtual environment in a folder named "venv". To activate the virtual environment, run the following command:

Windows:

```
venv\Scripts\activate
```

Linux/Mac:

```
source venv/bin/activate
```

### Install Dependencies:

Once the virtual environment is activated, you can install the project dependencies with the following command:

```
pip install -r requirements.txt
```

## Usage

To run the application, navigate to the root folder and run the following command:

```
python manage.py runserver
```

This will start the Django development server at `http://127.0.0.1:8000/`.

Then, open your web browser and navigate to `http://127.0.0.1:8000/users/signup/` to create a new account. 

To login, navigate to `http://127.0.0.1:8000/users/login/` and enter your email. An OTP will be sent to the email address you provide.

After successful authentication, you will be redirected to the search page where you can search for information about countries, cities, and country languages.

## Database

This project uses an in-memory SQLite database. A dump of the database is included in the `data.sqlite` and db.sqlite3.

## Product Roadmap



1. **Environment Setup**

- [x] Install Django using pip

- [ ] Install Express.js using npm

2. **Customize Django User Model**

- [x] Create a new model in `models.py` that extends `AbstractBaseUser`

- [x] Add fields: 'First Name', 'Last Name', 'Gender', 'Email ID', 'Phone Number'

- [x] Set 'Email ID' as the USERNAME_FIELD

3. **OTP Based Login**

- [ ] Set up OTP service (e.g., Twilio, SendGrid)

- [x] Create API to generate and send OTP when user tries to login

- [x] Store OTP in session or temporary database table

- [x] Validate user-entered OTP against stored OTP

4. **REST APIs and HTML Pages**

- [x] Use Django Rest Framework to write Signup, Login, Logout APIs

- [x] Create HTML templates for Signup, Login, Logout, Dashboard, Country Details pages

- [x] Implement two-step login process in Login page (accept email or phone number, then OTP)

5. **SQL Dump**

- [x] Load sql dump into your database

- [x] Create Django models to match structure of loaded tables

6. **Dashboard and Search**

- [x] Create HTML template for dashboard with a search bar

- [x] Implement AJAX for autosuggestions as user types in search bar

- [ ] Implement search functionality using Django's database API

7. **Country Details Page and Logout**

- [ ] Create HTML page for country details

- [ ] Provide URL route for country details page in Django's URL configuration

- [ ] Implement logout by clearing session or deleting user's token, and redirect to login page

8. **Connecting Django and Express**

- [ ] Develop APIs in Django to be consumed in Express.js server

- [ ] Use HTTP client library in Express.js to send requests to Django

9. **Code Quality and Testing**

- [x] Ensure proper code structuring and modularity

- [x] Handle errors and exceptions properly

- [ ] Write unit tests and integration tests

- [ ] Review and optimize the code

10. **Documentation**

- [x] Document the setup steps, usage and the API endpoints

- [x] Comment your code for better readability



