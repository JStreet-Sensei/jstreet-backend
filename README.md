# How start

1.  Clone backend repository inside a folder

1.  Clone the fronted repository inside the same root folder

    Example:
    ```

         projects
         ├───nihongo-jouzu-backend
         │   └───backend
         └───nihongo-jouzu-frontend
             └───package.json


1.  Copy .env.example to .env

1.  Create the python virtual environment

    `python -m venv venv`

1.  Activate python virtual environment

    Windows

    `.\venv\Scripts\activate`

    On Linux/macOS

    `source ./venv/bin/activate`

1.  Install libraries

    `pip install -r backend/requirements.txt`

1.  Run docker

   Build  ```docker compose build```
     
   Run  ```docker compose up```
   
   Build and run  ```docker compose up --build```
   
   Build and run production  ```docker compose -f "docker-compose.prod.yml" up -d --build```

1. Seeds data into Database

    ` docker exec -it "container name or id" python manage.py loaddata api/fixtures/initial_data.json`

# Testing
Basic knowledge of python testing.
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

Test URL example.
http://localhost:8000/api/quick-answer-game/game-contents

Run specific test case example<br>
`docker exec -it "container name or id" python manage.py test api.tests.QuickAnswerGameTests.test_quick_answer_game_content`


# Commands
## Migrations
* show all migrations
`docker exec -it "container name or id" python manage.py showmigrations`

* create new migrations. for example, after adding change to model
`docker exec -it "container name or id" python manage.py makemigrations`

* clear all migrations
`docker exec -it "container name or id" python manage.py migrate api zero`

* migration
`docker exec -it "container name or id" python manage.py migrate`

# Error Reference

## Docker

### Cannot sign in
In the case you can't run only with docker, you might need to define your ip adress correctly.
Run this command and put your ip to env files for both frontend and backend.

`Get-NetIPAddress`

example result
```bash
IPAddress         : 172.17.0.1
InterfaceIndex    : 48
InterfaceAlias    : vEthernet (WSL (Hyper-V firewall))
AddressFamily     : IPv4
Type              : Unicast
PrefixLength      : 20
PrefixOrigin      : Manual
SuffixOrigin      : Manual
AddressState      : Preferred
ValidLifetime     :
PreferredLifetime :
SkipAsSource      : False
PolicyStore       : ActiveStore
```
The result of this command doesn't work well. Still searching.
`docker inspect  -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 6b6cd1c04cf416cdfaf8d127bb1d507c6eed495058f2c22f0e3af12fd25fa47f`


# Learning
Django model
https://www.geeksforgeeks.org/django-basic-app-model-makemigrations-and-migrate/

Django rollback migration
https://sentry.io/answers/django-revert-last-migration/

Merge conflicts in migration
https://www.algotech.solutions/blog/python/django-migrations-and-how-to-manage-conflicts/