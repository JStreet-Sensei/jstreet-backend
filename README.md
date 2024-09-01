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

    `docker compose build`  
     `docker compose up`
