# Flask and SQL Data Modeling

Under Development

## Overview

This is an easy, basic and raw example of **HOW to** implement ???

---

## Requirements

* Python 3.6+
* pip 3
* virtualenv
* psycopg2-binary
* SQLAlchemy
* PostgreSQL
* psql
* Flask
* Flask-Migrate
<!-- for creating and running schema migrations -->

## Local development

### Install virtualenv

Install `virtualenv` to create isolated Python environments

```shell
pip3 install virtualenv
```

### Initialize and activate a virtualenv

```shell
python3 -m virtualenv env
source env/bin/activate
```

After this step, you can use just `python` (instead of python3; same for pip)

### Install dependencies

```shell
pip install -r requirements.txt
```

### Create database

```shell
createdb agency
```

### Run the setup script

```shell
source setup.sh
```

### Running the server

#### With Flask

```shell
flask run --reload
```

**Note:** If you want to make your server publicly available add the flag: `--host=0.0.0.0`

```shell
flask run --reload --host=0.0.0.0
```

#### With Python

```shell
python src/app.py 
```

**Note:** 
* When we run our application with `flask` the name of the app will be the name of our server file without the  .py extension, in this case, `app`.
* When we run the script with `python`, `python` will assign the name of `__main__` to the script when the script is executed.

So if you look at the end of our server file, `src/app.py`:

```py
if __name__ == '__main__':
  app.run()
```

... since name is `__main__`, the `app.run()` is executed.

### Populate data

```shell
psql agency
```

### Linting

We are going to use `pycodestyle` to check for pep8 issues and `autope8` to help us fix some of those issues.

If you don't have these packages, please, install them.

```shell
pip install pycodestyle
pip install autopep8
```

Then, at the root level:

```shell
pycodestyle src/
```

The output, in case of linting errors, would look like:

```shell
src/models.py:88:1: W293 blank line contains whitespace
src/models.py:89:3: E111 indentation is not a multiple of four
src/models.py:92:3: E111 indentation is not a multiple of four
src/models.py:97:6: W292 no newline at end of file
```

Now, you can use `autopep8` to start fixing some violations. 


```shell
autopep8 --in-place --aggressive --aggressive src/models.py
```

---

## Notes:

### PSQL: Create table and persist data

Drop and create the DB `test`, using the PostgreSQL cli.

```
dropdb test && createdb test
```

Then:

```shell
createdb test

psql test

CREATE TABLE my_tests (
  id INTEGER PRIMARY KEY,
  completed BOOLEAN NOT NULL DEFAULT False
);

INSERT INTO my_tests (id, completed) VALUES (1, False);

SELECT * FROM my_tests;

// Optional: delete db
dropdb test
```

Sample output:

```shell
 id | completed 
----+-----------
  1 | f
(1 row)
```

### psycopg2 Create table and persist data

BE SURE you are not naming your file `psycopg2.py` our you will end importing our script instead of the `psycopg2 module`

<!--
connection = psycopg2.connect('dbname=test')
AttributeError: partially initialized module 'psycopg2' has no attribute 'connect' (most likely due to a circular import)
 -->

Drop and create the DB `test`, using the PostgreSQL cli.

```
dropdb test && createdb test
```

Then:

```shell
python extras/psycopg2-sample.py
```

Sample output:

```shell
[(1, False)]
```

If you want to use `string interpolation` to compose your SQL query...

```py
# Original
cursor.execute('INSERT INTO my_tests (id, completed) VALUES (1, False);')

# Example 1: %s and tuple
cursor.execute('INSERT INTO my_tests (id, completed) VALUES (%s, %s);', (1, False))

# Example 2: %(my_dic_key) and dictionary
SQL = 'INSERT INTO my_tests (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 1,
  'completed': False
}
cursor.execute(SQL, data)
```

---

## Kudos

Extended version of Udacity's FSN SQL Data Modeling