# AUTH_API

A simple authentication API built with FastAPI, providing user registration and login functionality using PostgreSQL database and bcrypt for password hashing.

## Features

- User registration with password hashing
- User login with credential verification
- PostgreSQL database integration
- Secure password storage using bcrypt

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL database

### Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd AUTH_API
   ```

2. Install dependencies:
   ```
   pip install fastapi uvicorn pydantic bcrypt psycopg2-binary
   ```

3. Set up the PostgreSQL database:
   - Create a database named `crypto_db`
   - Create a table for users:
     ```sql
     CREATE TABLE users (
         id SERIAL PRIMARY KEY,
         username VARCHAR(255) UNIQUE NOT NULL,
         password VARCHAR(255) NOT NULL
     );
     ```
   - Update the database connection details in `database.py` if necessary.

## Usage

1. Run the application:
   ```
   uvicorn auth_api:app --reload
   ```

2. The API will be available at `http://127.0.0.1:8000`

3. Access the interactive API documentation at `http://127.0.0.1:8000/docs`

## API Endpoints

### POST /register
Register a new user.

**Request Body:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**
- Success: `{"message": "User registered"}`
- Error: `{"error": "error message"}`

### POST /login
Authenticate a user.

**Request Body:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**
- Success: `{"message": "Login successful"}`
- Error: `{"error": "Invalid credentials"}` or `{"error": "User not found"}`

## Development

- `auth_api.py`: Contains the FastAPI application and endpoints
- `database.py`: Database connection setup
- `main.py`: Entry point (currently empty, can be used to run the app)

## Security Notes

- Passwords are hashed using bcrypt before storage
- Database credentials are hardcoded in `database.py` - consider using environment variables for production
- Add proper input validation and error handling as needed

## License

This project is licensed under the MIT License.
