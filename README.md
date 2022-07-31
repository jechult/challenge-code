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
└── db                      # Database scripts folder
    └── init_sql.sql        # Initialization script after db container creation

```

# Table of contents

1. 👩‍💻 Pre requisites

- If not installed, download Docker Desktop (https://www.docker.com/products/docker-desktop/)
- If not installed, download git (https://git-scm.com/downloads)
- Make sure docker client is up

2. 🖥 Build and run application

- In terminal, run:

    ```bash
    git clone https://github.com/jechult/challenge-code.git
    ```
- After cloning project repository, run:

    ```bash
    docker-compose up --build
    ```

3. 🧪 Test running application

For testing purpose, use the following credentials:

    ```bash
    USERNAME = jechult
    PASSWORD = admin
    ```

- Step 1: Authenticate on API using the credentials above by running the following command:

    ```bash
    curl -X 'POST' \
    'http://localhost/login' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'grant_type=&username=[USERNAME]&password=[PASSWORD]&scope=&client_id=&client_secret='
    ```

- If everything's OK, as a result, you'll get an access token like this:

    ```bash
    {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiamVjaHVsdCIsImV4cCI6MTY1OTI4OTYxN30.8hAm4rYXXgk3MHxICzeL33luxKcR5Aeyf3-KaMy5A8g","token_type":"bearer"}
    ```

- Otherwise, you'll get the following message:

    ```bash
    {"detail":"Invalid credentials"}
    ```

- ✔ Once you are correctly authenticated, you'll be able to test the api. Please, save the obtained access token,
you're going to need it for the following tests. ⚠ Warning: The obtained access token will expire in 30 minutes, so please be
careful when making requests to the different apis.

- In order to obtain the weekly average number of trips per region, run the following command:

    ```bash
    curl -L -X GET 'http://localhost/reporting/weekly' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer [ACCESS_TOKEN]'
    ```

- If everything's OK, you'll get this:

    ```bash
    {"Hamburg":16.8,"Prague":20.4,"Turin":22.8}
    ```


