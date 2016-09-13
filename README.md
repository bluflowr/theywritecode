
# They Write Code Django App

This project takes random identities and puts them together in funny and thought provoking ways showing us that a coder can be anyone.

## APIs Used

###[Twitter](https://dev.twitter.com/)  

## Installation

### 1. virtualenv

Learn more about [virtualenv](http://www.virtualenv.org/). Create a new virtualenv for your own project, where `projectname` is the name of your project:

`$ virtualenv --python=python3 projectname`

Activate your virtualenv:

`$ source projectname/bin/activate`

### 2. Download
Now, you need the *writecode* project files in your environment:

    $ cd /path/to/your/project
    $ git clone git://github.com/bluflowr/theywritecode.git projectname && cd projectname

### 3. Requirements
Included is the *requirements.txt* file that has all the resources you'll need for this project. To install them, simply type:

`$ pip install -r requirements.txt`  

### 4. SECRET_KEY and Credentials
Rename `secret_example.py` to `secret.py`

Go to <http://www.miniwebtool.com/django-secret-key-generator/>, create your secret key, copy it. Open `secret.py`, find `key` line, paste your secret key.  
Go to [Twitter](https://dev.twitter.com/). Once you've created you app keys and access tokens, enter your Twitter credentials in `secret.py`.

### 5. Initialize the database

First set the database engine (PostgreSQL, MySQL, etc..) in your settings files; `plotcreator/settings.py`. Install necessary database drivers. Define your credentials. Then create your database:

    $ python manage.py migrate
    $ python manage.py makemigrations writecode
    $ python manage.py migrate


### 6. Runserver

    $ python manage.py runserver

### 7. Twitter Cron Job

Create a cron job to post updates to twitter. 

	$ python manage.py tweet 

## Implementation
This site is currently live at [theywritecode.com](http://theywritecode.com/)
There is also a cron job posting pairings to twitter twice a day! [@theywritecode](https://twitter.com/theywritecode)