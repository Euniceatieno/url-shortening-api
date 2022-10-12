# URL Shortening Service
This is an application that performs the following:  
 * Converts a provided long url to it's shortened version.
 * Converts a shortened url back to it's original long version. 

# How it works
* The service allows the user to enter an original url through the */encode* endpoint  
and  receive a response with the shortened_url.  
On clicking the shortened_url ,the user is redirected to the resource behind the original url  
* The service also allows the user to enter a shortened url via the */decode* endpoint  
and receive a response with the original url.

## Alternatively watch the video to understand how the service works

<video src="url-shortener-2022-10-13_00.07.29.mp4" controls="controls" style="max-width: 1530px;">
</video>


# Core Technologies and Libraries Used

Technology/Library | Description 
--- | --- |
*Django REST Framework* | *Api building framework for django*
*Postman* |*Api testing*
*Logging* | *Application events recording* 
*Unittest* | *A python library for writing tests*
*Postgres* | *A relational database service*
*Python* | *An object oriented programming language* 
*Redis* | *An in mem0ry cache service*
*Django* | *A python framework for building serverside applications*
*Flake8* | *A code formatting library for Python*  
  

# Setting up the codebase locally

This is a step by step guide on how to set up the codebase locally

Clone the project
----------------------
``` shell
git clone http://finn-gmbh-wbumum@git.codesubmit.io/finn-gmbh/default-python-kyusoj
```
Set up your virtual environment
----------------------
``` shell
gpython3 -m venv env
```
Activate your virtual environment
----------------------
``` shell
source env/bin/activate
```
Install the required packages
----------------------
``` shell
python3 -m pip install -r requirements.txt --no-cache-dir
```
Create a .env file with the following environment variables
------------------------------------------------------------------
``` shell
SECRET_KEY=yoursecretkey
DATABASE_NAME=yourdb
DATABASE_USER=yourdbuser
DATABASE_PASSWORD=yourbdpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
Export your environment variables
--------------------------------------------
``` shell
source .env
```
Create a local database with the credentials in your .env file
---------------------------------------------------------------

Run migrations
----------------------
``` shell
python3 manage.py makemigrations
```
Migrate database updates
----------------------
``` shell
python3 manage.py migrate
```
Run Unit Tests
----------------------
``` shell
coverage run manage.py test

```
Start local server
----------------------
``` shell
python3 manage.py runserver
```
Encode a url on postman *http://127.0.0.1:8000/encode/*
--------------------------------------------------------
``` shell
Add the json below as the request body:
 {
    "original": "https://www.tutorialspoint.com/python_network_programming/python_dns_look_up.htm"
 }

```
Decode a url on postman *http://127.0.0.1:8000/decode/*
-------------------------------------------------------
``` shell
Add the json below as the request body:
 {
    "shortened_url": "http://127.0.0.1:8000/gta8mw"
 }
```


# Contacts
For any queries ,reach out to *eunniceatieno@gmail.com*
