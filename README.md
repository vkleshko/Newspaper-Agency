# Newspaper-Agency

You are the head of a newspaper agency. And you work with a great team of editors. But you are not properly tracking the newspapers your agency publishes. That is why a tracking system for Redactors assigned to Newspapers was created. With it you will always know, who were the publishers of each Newspaper.

Demo project
--------------------------------
Check out the demo at:
https://publisher-insight.onrender.com

## Installing using GitHub

Clone the project

```bash
  git clone https://github.com/vkleshko/Newspaper-Agency
```

Go to the project directory

```bash
  cd newspapers_agency_service
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Set up environment variables:

```
  set SECRET_KEY=<your secret key>
```

Migrate Database

```bash
  python manage.py migrate
```

Runserver

```bash
  python manage.py runserver
```

## Getting access

- Username: user
- Password: user12345

## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```
