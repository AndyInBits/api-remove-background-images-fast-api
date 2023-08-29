# Handler Images API README

Welcome to the Handler Images API project! This API allows users to manage their accounts, upload images, resize images, and perform various image-related tasks. Below, you'll find instructions on how to set up, use, and interact with the API endpoints.

## Table of Contents

1. [Getting Started](#getting-started)
2. [User Management](#user-management)
   - [Create User](#create-user)
   - [Update User](#update-user)
   - [Delete User](#delete-user)
   - [Login User](#login-user)
3. [Image Processing](#image-processing)
   - [Upload and Process Image](#upload-and-process-image)
   - [Get User's Images](#get-users-images)
   - [Delete Image](#delete-image)

## Getting Started

To get started with the Handler Images API, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Run the FastAPI application.

```bash
git clone https://github.com/AndyInBits/api-remove-background-images-fast-api.git

cd api-remove-background-images-fast-api

docker-compose up --build
```

The API will be accessible at http://127.0.0.1.
The API DOC will be accessible at http://127.0.0.1/docs.

## User Management

### Create User
**Endpoint**: POST /users

Create a new user by providing their email, password, password confirmation, and full name.

### Update User
**Endpoint**: PUT /user

Update the current user's email and full name. Requires authentication with a valid JWT token.

### Delete User
**Endpoint**: DELETE /user

Delete the current user's account. Requires authentication with a valid JWT token.

### Login User
**Endpoint**: POST /login

Login with a registered user's email and password to receive an authentication token.

## Image Processing

### Upload and Process Image
**Endpoint**: POST /process_images

Upload an image and optionally specify the output format, width, and height for image processing. Requires authentication with a valid JWT token.

### Get User's Images
**Endpoint**: GET /my_images

Retrieve a list of images uploaded by the current user. Requires authentication with a valid JWT token.

### Delete Image
**Endpoint**: DELETE /delete_image/{id}

Delete an image by providing its ID. Requires authentication with a valid JWT token.

## Conclusion

Congratulations! You now have the basic understanding of how to use the Handler Images API. Feel free to explore the various endpoints and functionalities to create users, manage images, and perform image processing tasks. If you have any questions or encounter issues, refer to the API documentation or contact the project maintainers for assistance. Happy coding!


## Technologies at a Glance

### FastAPI

FastAPI is a Python framework designed to streamline the development of efficient APIs. With its clean syntax and declarative data types, FastAPI simplifies route definition, data validation, and interactive documentation generation.

### Redis

Redis is a high-speed, in-memory database. It excels at caching data to enhance access speed for frequently used information. Within the context of an API, Redis serves to store pre-computed results, mitigating server load.

### Docker

Docker is a containerization platform that packages applications and their dependencies into isolated containers. This ensures consistent execution across diverse environments, facilitating deployment and scalability.

### Docker Compose

Docker Compose simplifies multi-container applications by allowing you to define and manage services, networks, and volumes within a single configuration. This streamlines the deployment of intricate applications comprising multiple components.

### JWT (JSON Web Tokens)

JSON Web Tokens provide a secure means of transmitting information between parties. They are compact and self-contained, often used for user authentication and authorization within APIs. JWTs ensure users access only authorized resources.

### RESTful API

REST (Representational State Transfer) is an architectural style for building web services. RESTful APIs employ standard HTTP methods (GET, POST, PUT, DELETE) to interact with resources via URIs. This approach fosters efficient and scalable web interfaces.
