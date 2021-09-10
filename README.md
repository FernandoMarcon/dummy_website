

## Set up virtual environment
```Bash
sudo apt install python3.8-venv
python3 -m venv venv
source /venv/bin/activate
```
## Install and configure `flask`
```Bash
pip install flask flask-wtf flask-dotenv
```

Create _.flaskenv_ file and add:

  ```
  FLASK_ENV=development
  FLASK_APP=main.py
  ```

## create requirements file
```Bash
pip freeze > requirements.txt
```


# Navigation Links and Routing Patterns
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
