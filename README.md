# Data Engineering Challenge

Data ingestion process to load and store files in SQL Database.

## 📁 Project structure


```

.
├── .gitignore              # Prevent staging of unnecessary files to git
├── docker-compose.yml      # Config file to deploy both fastapi and mysql container
├── bonus_sql.sql           # SQL queries to get results from bonus features
├── README.md               # Project README
├── api                     # API folder
│   ├── app                 # API source code
│   ├── Dockerfile          # Config file to build a python container with api code
│   └── requirements.txt    # Packages list for api environment
├── test_files              # Set of files for test uploading process
│   ├── regions.csv         # File which contains regions list
│   ├── sources.csv         # File which contains sources list
│   └── trips.csv           # File which contains trips list
└── db                      # Database scripts folder
    └── init_sql.sql        # Initialization script after db container creation

```

# Table of contents

0. Trips data model

<img src="https://github.com/jechult/challenge-code/blob/d70c3a5621351ce7d3b73de02d85f7de5168ec11/db/data_model.png" alt="Alt text" title="Trip data model">

1. 👩‍💻 Pre requisites

- If not installed, download Docker Desktop (https://www.docker.com/products/docker-desktop/)
- If not installed, download git (https://git-scm.com/downloads)
- Make sure docker client is up

2. 🖥 Build and run application

- To download the remote repository in local, run in terminal:

    ```shell
    git clone https://github.com/jechult/challenge-code.git
    ```
- Once you have downloaded the repository, run the following command to build and deploy the containers (api and mysql):

    ```shell
    docker-compose up --build
    ```

3. 🧪 Test running application

- For testing purpose, use the following credentials:

    ```shell
    USERNAME = jechult
    PASSWORD = admin
    ```

- As a first step, please authenticate on API using the credentials above by running the following command:

    ```shell
    curl -L -X POST 'http://localhost/login' \
    -F 'username=[USERNAME]' \
    -F 'password=[PASSWORD]'
    ```

    Parameters:
    - USERNAME: user displayed in 3.1
    - PASSWORD: password displayed in 3.1

- If everything's OK, as a result, you'll get an access token like this:

    ```shell
    {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiamVjaHVsdCIsImV4cCI6MTY1OTI4OTYxN30.8hAm4rYXXgk3MHxICzeL33luxKcR5Aeyf3-KaMy5A8g","token_type":"bearer"}
    ```

- Otherwise, you'll get the following message:

    ```shell
    {"detail":"Invalid credentials"}
    ```

- ✔ Once you are correctly authenticated, you'll be able to test the api. Please, save the obtained access token,
you're going to need it for the following tests. ⚠ Warning: The obtained access token will expire in 30 minutes, so please be
careful when making requests to the different apis.

- Before uploading any data, it's mandatory data files have the following structure:

<img src="https://github.com/jechult/challenge-code/blob/eb73157fde63ff683b54b7345299ae95d70efe56/test_files/files_structure.png" alt="Alt text" title="Test files structure">

- As you can see, previous data model has 3 tables which are regions, sources and trips. Before testing reporting requests, you
must upload data to insert it into tables. To do that, you should run the following command:

    ```shell
    curl -L -X POST 'http://localhost/uploadfile' \
    -H 'Authorization: Bearer [ACCESS_TOKEN]' \
    -F 'table_name="[TABLE_NAME]"' \
    -F 'table_content=@"[FILE_PATH]"'
    ```

    Parameters:
    - ACCESS_TOKEN: obtained code in authentication process
    - TABLE_NAME: table name which 3 possible values (trips, sources, regions)
    - FILE_PATH: path where file is stored. Example: /home/files/trips.csv

- In order to obtain the weekly average number of trips per region, run the following command:

    ```shell
    curl -L -X GET 'http://localhost/reporting/weekly' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer [ACCESS_TOKEN]'
    ```

- If everything's OK, you'll get this:

    ```shell
    {"Hamburg":16.8,"Prague":20.4,"Turin":22.8}
    ```

