# API advanced — Alx System Engineering DevOps
0x16. API advanced

``Python``
``Scripting``
``Back-end``
``API``

## What is an API?
An ``API`` (Application Programming Interface) is a set of rules and protocols that allows different software applications to **communicate** with each other. It defines how software components should interact, enabling developers to access specific functionalities or data from a service or application without needing to understand its internal workings.

## What is a REST API?
A ``REST`` (Representational State Transfer) API is a type of API that follows a set of architectural principles, defining how web standards, such as **HTTP** and **URLs**, should be used for creating web services. REST APIs use standard HTTP methods (``GET``, ``POST``, ``PUT``, ``DELETE``) to perform **CRUD** (Create, Read, Update, Delete) operations on resources (data) and typically return responses in formats like ``JSON`` or ``XML``.

A **RESTful** web service request contains:
- **An Endpoint URL**. An application implementing a RESTful API will define one or more URL endpoints with a domain, port, path, and/or query string.
- **The HTTP method**. Differing HTTP methods can be used on any endpoint which map to application create, read, update, and delete (CRUD) operations:
  - **``GET``**	read	returns requested data
  - **``POST``**	create	creates a new record
  - **``PUT``** or **``PATCH``** 	update	updates an existing record
  - **``DELETE``**	delete	deletes an existing record
- **HTTP headers**. Information such as authentication tokens or cookies can be contained in the HTTP request header.
- **Body Data**. Data is normally transmitted in the HTTP body in an identical way to HTML form submissions or by sending a single JSON-encoded data string.


## What are Microservices?
``Microservices`` is an architectural style where complex software applications are built as a collection of small, independent services that communicate with each other through APIs. Each service focuses on a specific business function and can be developed, deployed, and scaled independently, promoting flexibility, scalability, and easier maintenance.

**Example**: Instead of building a monolithic e-commerce platform, you break it down into smaller services like user management, inventory management, payment processing, etc., each running as a separate microservice.

## What is the JSON Format?
``JSON`` (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and for machines to parse and generate. It consists of key-value pairs enclosed in curly braces, with keys and string values separated by colons. JSON is commonly used for transmitting data between a server and a web application, especially in ``REST APIs``.

**Example**: A JSON object representing a user profile might look like this:

```json
{
  "id": 1,
  "name": "Ouadia EL-Ouardy",
  "email": "ouadia@elouardy.com",
  "age": 26,
  "is_active": true
}
```

## Contact Me
**Email:** ouadia@elouardy.com \
**Twitter:** https://twitter.com/_ELOUARDY

