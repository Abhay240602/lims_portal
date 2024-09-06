Introduction
============

This is the documentation for **Lims Portal**.

Lims Portal is a Django-based platform designed to manage laboratory information systems. It offers a range of features to effectively handle entities, data, and APIs.

Main Features
--------------
- **Model Entity Management**: Manages entities like readers and books.
- **Data Import/Export**: Facilitates importing and exporting data.
- **Configurable APIs**: Provides customizable API endpoints.

API Overview
------------
The Lims Portal API provides various endpoints for interacting with the system:

1. **/api/schema/**
   - **GET**: Provides OpenAPI 3 schema for the API.
   - **Formats Supported**: YAML, JSON.

2. **/api/docs/**
   - **GET**: Provides API documentation in HTML format.

3. **/api/redoc/**
   - **GET**: Provides API documentation in HTML format using ReDoc.

4. **/readers**
   - **GET**: Retrieves a list of all readers.
   - **POST**: Creates a new reader.
   - **Request Body Formats**: JSON, URL-encoded, multipart/form-data.

5. **/readers/{id}**
   - **GET**: Retrieves details of a specific reader by ID.
   - **PUT/PATCH**: Updates a reader’s information (full or partial).
   - **DELETE**: Deletes a reader by ID.

6. **/books**
   - **GET**: Retrieves a list of all books.
   - **POST**: Creates a new book.
   - **Request Body Formats**: JSON, URL-encoded, multipart/form-data.

7. **/books/{id}**
   - **GET**: Retrieves details of a specific book by ID.
   - **PUT/PATCH**: Updates a book’s information (full or partial).
   - **DELETE**: Deletes a book by ID.

8. **/api/token/**
   - **POST**: Obtains a token pair (access and refresh tokens) for authentication.
   - **Request Body Formats**: JSON, URL-encoded, multipart/form-data.

9. **/api/token/refresh/**
   - **POST**: Refreshes an access token using a refresh token.
   - **Request Body Formats**: JSON, URL-encoded, multipart/form-data.

Schemas
-------
- **Reader**: Includes properties such as `reference_id`, `reader_name`, `reader_contact`, `reader_address`, and `books`.
- **Book**: Includes properties such as `name`, `isbn`, `author`, `category`, and `readers`.
- **TokenObtainPair**: Contains `username` and `password` for authentication.
- **TokenRefresh**: Contains `refresh` and `access` tokens.

This summary provides an overview of the Lims Portal’s features, API endpoints, and data schemas.
