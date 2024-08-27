# How start

1) Clone backend repository inside a folder

1) Clone the fronted repository inside the same root folder

    Example:
        ```
        
        projects
        ├───nihongo-jouzu-backend
        │   └───backend
        └───nihongo-jouzu-frontend
            └───package.json
        
        

2) Create the python virtual environment

    ```python -m venv venv```
3) Activate python virtual environment
    
    Windows

    ```.\venv\Scripts\activate``` 

    On Linux/macOS

    ```source ./venv/bin/activate```

4) Install libraries

    ```pip install -r backend/requirements.txt```    

5) Run docker

    ```docker compose build```  
    ```docker compose up```  
