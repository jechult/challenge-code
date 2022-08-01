# Data Engineering Challenge

Data ingestion process to load and store files in SQL Database.

## 📁 Project structure


```

.
├── .gitignore                  # Prevent staging of unnecessary files to git
├── docker-compose.yml          # Config file to deploy both fastapi and mysql container
├── bonus_sql.sql               # SQL queries to get results from bonus features
├── README.md                   # Project README
├── api                         # API folder
│   ├── app                     # API source code
│   ├── Dockerfile              # Config file to build a python container with api code
│   └── requirements.txt        # Packages list for api environment
├── test_files                  # Set of files for test uploading process
│   ├── 100_million_test.png    # Image with loading stress proof
│   ├── files_structure.png     # Image with data files structure
│   ├── regions.csv             # File which contains regions list
│   ├── sources.csv             # File which contains sources list
│   └── trips.csv               # File which contains trips list
└── db                          # Database scripts folder
    ├── data_model.png          # Tables data model for trips, regions and sources
    └── init_sql.sql            # Initialization script after db container creation

```

# Table of contents

0. Trips data model

<img src="https://github.com/jechult/challenge-code/blob/429bc5790386e4b638049f6ae4a97e7693b6f78e/db/data_model.png" alt="Alt text" title="Trip data model">

1. 👩‍💻 Pre requisites

- If not installed, download Docker Desktop (https://www.docker.com/products/docker-desktop/)
- If not installed, download git (https://git-scm.com/downloads)
- Make sure docker client is up

2. 🖥 Build and run application

- To download the remote repository in local, run in terminal:

    ```shell
    cd challenge-code
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

<img src="https://github.com/jechult/challenge-code/blob/429bc5790386e4b638049f6ae4a97e7693b6f78e/test_files/files_structure.png" alt="Alt text" title="Test files structure">

- As you can see, previous data model has 3 tables which are regions, sources and trips. Before testing reporting requests, you
must upload data to insert it into tables. To do that, you should run the following command:

    ```shell
    curl -L -X POST 'http://localhost/uploadfile' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer [ACCESS_TOKEN]' \
    -H 'Content-Type: multipart/form-data' \
    -F 'table_name="[TABLE_NAME]"' \
    -F 'table_content=@"[FILE_PATH]"'
    ```

    Parameters:
    - ACCESS_TOKEN: obtained code in authentication process
    - TABLE_NAME: table name which 3 possible values (trips, sources, regions)
    - FILE_PATH: path where file is stored. Example: /home/files/trips.csv

- Once the process ends, you'll see a message like this:

    ```shell
    {"message":"table trips updated"}
    ```

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

4. ☁ Cloud sketchup solution using Google Cloud Plaftorm

<img src="https://github.com/jechult/challenge-code/blob/429bc5790386e4b638049f6ae4a97e7693b6f78e/cloud_sketchup/sketchup.png" alt="Alt text" title="GCP Solution">

4.1. What services would be use? How would they work?

- Google Cloud Repository: Here, we will store source code related to the API
- Google Cloud Storage: Its aim is to store different data files to trigger the API
- Google Cloud Function: Once a user uploads a file in GCS bucket, Cloud Function will triggered to process the uploaded file. Then, it will make a connection with BigQuery in order to store the processed file data to tables
- Cloud Monitoring: Its aim is to monitor cloud function performance and get reports from quotas, requests, errors and so on.
- Google Data Studio: It will allow us to create different dashboards from BigQuery data. With this, we can get important insights to
improve our business in a technical and non-technical way