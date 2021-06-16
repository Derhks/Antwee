# Antwee
[![codecov](https://codecov.io/gh/Derhks/Antwee/branch/master/graph/badge.svg?token=meBTrDeM4Z)](https://codecov.io/gh/Derhks/Antwee)

## Table of Content

* [Prerequisites](#prerequisites)
* [Development Environment Configuration](#development-environment-configuration)
* [Run development version with docker](#run-development-version-with-docker)
* [Test the Application](#test-the-application)
* [Built With](#built-with)
* [Authors](#authors)


## Prerequisites

To execute the project, you will need the following:

* [Python3](https://www.python.org/downloads/)
* [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)
* [PostgreSQL](https://www.postgresql.org/download/)

## Development Environment Configuration

Download the files from this repository

```bash
git clone https://github.com/Derhks/Antwee.git
```

Go to the Antwee folder

```bash
cd Antwee/
```

Verify that we have installed anaconda, if we do not have it, 
we must install it

```bash
conda --version
```

Create a virtual environment with Anaconda

```bash
conda create -n antwee python=3.8 -y
```

Now, let's activate the created virtual environment

```bash
conda activate antwee
```

With the virtual environment activated we are going to install 
the requirements used in the project, but first let's update pip

```bash
pip install --upgrade pip
```

and now the requirements

```bash
pip3 install -r requirements.txt
```

We must export the environment variables that we need in our project. 
Change the name of the `example.env` file to `.env`, fill in the 
environment variables with their corresponding value and finally execute 
the following command:

```bash
export $(cat .env | grep -v ^# | xargs)
```

### Setup PostgreSQL

Verify that you have `PostgreSQL` installed on your computer, run the 
following command to find out which version you have installed:

```bash
psql -V
```

If you do not see the PostgreSQL version, you must install it.

Run the `setup_postgres.sql` script to create the database, username 
and password to be used in the project. 

```bash
cat setup_postgres.sql | sudo -u postgres psql
```

With the above command we enter the PostgreSQL Shell and the commands inside 
the file are executed. To verify that the database, and the user were created 
execute the following commands:

1. Database
```bash
echo "SELECT datname FROM pg_database;" | sudo -u postgres psql | grep antwee_db
```

2. User
```bash
echo "SELECT * FROM pg_catalog.pg_user;" | sudo -u postgres psql | grep derhks
```

Verify that the FLASK_APP environment variable is declared:

```bash
env | grep FLASK_APP
```

Let's create the table we will use in the project within our database

```bash
flask db init && flask db migrate && flask db upgrade
```

If you create a new model or if you update an existing one you 
must update the database, to do this run the following command:

```bash
flask db migrate && flask db upgrade
```


### Run tests
We need to declare the environment variable TESTING as True 
to perform the tests:

```bash
export TESTING=True
```

The application has its unit tests, run the following command:

```bash
coverage run -m unittest discover
```

We can view the report with the command:
  
```bash
coverage report -m
```

After finishing the tests, delete the TESTING variable:

```bash
unset TESTING
```


### Run server

You can verify that the environment variables were added 
correctly with the following command:

```bash
env | grep "FLASK"
```

Finally, run the application server

```bash
python -m flask run
```


## Run development version with docker

Run the following command to initialize the project using docker:

```bash
docker-compose up --remove-orphans
```

You can stop the containers and also delete everything that was 
created at initialization by executing the following command, to 
do this you must open a new console:

```bash
docker-compose down --rmi all && sudo rm -rf data/
```

## Test the Application

### Develop

#### Locally

If you are running the project locally, visit the following link to test the endpoints:

```bash
http://localhost:5000/apidocs/
```

#### Docker

If you are running the project with docker, visit the following link to test the endpoints:

```bash
http://0.0.0.0:5000/apidocs/
```

## Built With

- [Python](https://www.python.org/) - Programming language
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web framework
- [PostgreSQL](https://www.postgresql.org) - Database


## Authors
- **Julián Sandoval [derhks]** https://github.com/Derhks
