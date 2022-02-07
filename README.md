# Open Data API
This is the monorepo containing all the applications necessary to stand up the Data Ingestion API project. The project ingests and transforms web data and provides access to the data via a various APIs. The core of the project is a django server and the tech stack is described below. The repo also contains the python API for querying data from a hosted version of the project in the `python_api` directory.

## Use Instructions
If you are interested in using data from the project you will need to see our API docs [here](https://etl-project-monorepo.readthedocs.io/en/latest/) which contain instructions on how to make requests to the API and how to use the python API to programmatically pull data.

## Building the Project
If you want to recreate the project there are specific configurations that will need to be set up before building the project via the docker compose file.

### Environment Configuration
Each service will need configuration via environmental variables. The project knows to look for these environment variables in a `.env` file located in the root of the project directory:

#### PostgreSQL Configuration
The environment variables needed to config the psql database are used both by the containerized database to spin up the instance and the django server to connect to it. They are the standard docker params for creating a psql instance:
```
POSTGRES_USER=django_rest_api
POSTGRES_PASSWORD=example_password
POSTGRES_DB=rest_api
POSTGRES_PORT=5432
```
#### Django Server Configuration:
These are also standard configuration variables for a django project. It is important that you add the IP entrypoint to the project as an “allowed_host” variable to allow the Swagger UI to make requests to the API correctly.
```
SECRET_KEY=example_secret_key
PRODUCTION=TRUE
ALLOWED_HOST=xxx.x.x.x 
```



