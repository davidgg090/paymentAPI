# Payment Gateway API

This is a simple payment gateway API that allows you to make payments and retrieve payment details.

## Installation

Create a virtual environment and install the requirements using the following commands:
    
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the root directory and add the following environment variables:

```bash
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
SECRET_KEY=
ALGORITHM=
```

## Usage

To run the server, use the following command:

```bash
python main.py

```

The server will be running on `http://127.0.0.1:8000/`

Check the API documentation at `http://12.0.0.1:8000/api/v1/docs`


## Testing

To run the tests, use the following command:

```bash
pytest
```

## Docker

To run the server using docker, use the following commands:

```bash
docker build -t payment-gateway-api .
docker run --env-file .env p 8000:80 payment-gateway-api
```

## Database

Open the file `execute_sql.sh` and replace the environment variables with the correct values for your database.

```bash
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
```



For create the tables for the database, make it executable the file in folder script call execute_sql.sh with the following command in the terminal:
    
```bash
chmod +x execute_sql.sh
```

Then, execute the file with the following command:

```bash
./execute_sql.sh
```


## Technologies

- FastAPI
- PostgreSQL
- Docker
- Pytest
- SQLAlchemy


## License

[MIT](https://choosealicense.com/licenses/mit/)