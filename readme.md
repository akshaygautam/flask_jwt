# Flask Authentication and User Management API

This project provides a robust authentication and user management system built with Flask. It includes JWT-based authentication, user role management, and admin-specific privileges for managing users. The project is designed to be a modular and extensible foundation for building secure web applications.

---

## Features

- **JWT Authentication**:
  - Access and refresh token handling.
  - Secure routes protected by JWT.
  - Custom error responses for invalid, expired, or missing tokens.

- **User Management**:
  - User registration with hashed passwords.
  - Login endpoint to issue tokens.
  - Fetch current user details via protected endpoints.
  - Admin-only access to list all users with pagination.

- **Role-Based Access Control**:
  - Claims-based permissions.
  - Assign admin privileges to specific users.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- A supported database (e.g., SQLite, PostgreSQL, MySQL)

### Project Setup Guide

Follow these steps to set up and run the project:

---

## Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```
```bash
FLASK_SECRET_KEY=dghwedkjcbnkurhfwejcnj
FLASK_DEBUG=True
FLASK_SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3
FLASK_SQLALCHEMY_ECHO=True
FLASK_JWT_SECRET_KEY=e2bcff66d508aa933df986dd
```
``` bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
flask run
```


## Usage

### API Endpoints

#### **Authentication (`/auth`)**

1. **Register**:
   - **Endpoint**: `/auth/register`
   - **Method**: `POST`
   - **Description**: Register a new user.
   - **Request Body**:
     ```json
     {
       "username": "user1",
       "email": "user1@example.com",
       "password": "securepassword"
     }
     ```
   - **Response**:
     - **Success**: `201 Created`
     - **Failure**: `400 Bad Request`

2. **Login**:
   - **Endpoint**: `/auth/login`
   - **Method**: `POST`
   - **Description**: Log in an existing user and receive a token.
   - **Request Body**:
     ```json
     {
       "username": "user1",
       "password": "securepassword"
     }
     ```
   - **Response**:
     - **Success**: `200 OK` with a token
     - **Failure**: `401 Unauthorized`

3. **Who Am I**:
   - **Endpoint**: `/auth/whoami`
   - **Method**: `GET`
   - **Description**: Get details of the currently logged-in user.
   - **Headers**:
     ```http
     Authorization: Bearer <access_token>
     ```
   - **Response**:
     - **Success**: `200 OK`
     - **Failure**: `401 Unauthorized`

4. **Refresh Token**:
   - **Endpoint**: `/auth/refresh`
   - **Method**: `GET`
   - **Description**: Refresh the access token using a refresh token.
   - **Headers**:
     ```http
     Authorization: Bearer <refresh_token>
     ```
   - **Response**:
     - **Success**: `200 OK` with a new access token
     - **Failure**: `401 Unauthorized`

---

#### **User Management (`/users`)**

1. **List Users (Admin Only)**:
   - **Endpoint**: `/users/all`
   - **Method**: `GET`
   - **Description**: List all users with pagination.
   - **Headers**:
     ```http
     Authorization: Bearer <access_token>
     ```
   - **Query Parameters**:
     - `page`: Page number (default: 1)
     - `per_page`: Items per page (default: 5)
   - **Response**:
     - **Success**: `200 OK` with user list
     - **Failure**: `401 Unauthorized`


### Dependencies

Key dependencies included in `requirements.txt`:

- **Flask**: Web framework.
- **Flask-JWT-Extended**: JWT-based authentication.
- **Flask-SQLAlchemy**: ORM for database interactions.
- **Marshmallow**: Data serialization and validation.
