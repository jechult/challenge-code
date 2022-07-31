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

- Step 1: Authenticate on API by running the following command:

    ```bash
    curl -X 'POST' \
    'http://localhost/login' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'grant_type=&username=[USERNAME]&password=[PASSWORD]&scope=&client_id=&client_secret='
    ```

