# Universal Tech Academy
This is a dummy website for learning Full-Stack Web Development with Flask.

## Main Topics
- Flask
- HTML
- CSS
- Jinja
- JSON
- Request and Response Objects
- APIs
- Databases
  + mongoDB

### Setting Up Virtual Environments and Flask
#### Set up virtual environment
```Bash
sudo apt install python3.8-venv
python3 -m venv venv
source /venv/bin/activate
```
#### Install and configure `flask`
```Bash
pip install flask flask-wtf flask-dotenv
```

Create _.flaskenv_ file and add:
```
FLASK_ENV=development
FLASK_APP=main.py
```
#### Create requirements file
```Bash
pip freeze > requirements.txt
```

### Navigation Links and Routing Patterns
- Creating navigation menus
- Using the `url_for` function to resolve links
- Using the `route()` decorator to build a function to one or more URL patterns
```
http://domain.com/
http://domain.com/index
http://domain.com/home
```

- Jinja delimiters
```
{% ... %} - Statements
{{ ... }} - Expressions
{# ... #} - Comments
```
- The `if` statement in Jinja

### Request and Response Objects
#### The Request Object
Accessing Query String (GET)
```Python
request.args.get(<field_name>)
request.args[<field_name>]
```

Accessing Form Data (POST)
```Python
request.form.get(<field_name>)
request.form[<field_name>]
```
#### The Response Object
```Python
class flask.Response(
  response=None, # Most common used parameters
  status=None,
  headers=None,
  mimetype=None, # Most common used parameters
  content_type=None, # Most common used parameters
  direct)passthrough=False)
```
### Databases
#### mongoDB
[Installation](https://www.mongodb.com/)
```Bash
sudo systemctl start mongod
mongoimport --jsonArray --db UTA_Enrollment --collection courses  --file models/courses.json
mongoimport --jsonArray --db UTA_Enrollment --collection user  --file models/user.json
```

Setting up a mongoDB database
```
MONGODB_SETTINGS = {'db': 'UTA_Enrollment'}
```

Importing the MongoEngine
```Python
from flask_mongoengine import MongoEngine
```

Initializing the database object
```Python
db = MongoEngine()
db.init_app(app)
```
-  Exploring the MongoDB Aggregation framework using Compass interface
-  Creating the aggregation pipeline to process data in three stages
```
$lookup: Performs a left outer join
$match: Filters documents
$unwind: Deconstructs an array field
```

#### Flask-WTF Extension
- Flask-WTF is an extension for the WTForms library
- WTForms provides a clean way to generate HTML form fields
- Maintain a separation of code and presentation

```html
<form>
{{ form.hidden_tag() }}
{{ form.username }}
{{ form.email }}
{{ form.password }}
<\form>
```
- Provides common security and authentication features:
  - Session-based authentication
  - Password hashing
  - Basic HTTP and token-based authentications
  - User registration
  - Login tracking (Flask-Login)

- Supports data persistancy for Flask-SQLAlchemy, Flask-MongoEngine, flask-peewee, and PonyORM

### Sessions
#### State management and User Authentication using **Flask-Session**
- The **session** object stores information specific to a user
- Implementation on top of cookies and signs cookies cryptographically

```Python
session['jey'] = value   # setting a session
session.get('key')       # getting a session

session.pop('key',None)   # destroying a session
session['key']= False     # destroying a session
```
#### Flask-Login Extension
- Sessions and state management using Flask-Login extension
- Managing user logged-in state using a user-loader() function
- Using the LoginManager class to manage login state
- Implementing the "remember me" feature
- Restricting access to protected pages with @login_required
- Logging out users using the logout_user() function

## Source:
- [Full-Stack Web Development with Flask (LinkedIn)](linkedin.com/learning/full-stack-web-development-with-flask/)
