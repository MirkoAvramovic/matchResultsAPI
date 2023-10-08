# Match Results API

The Match Results API is a Django-based RESTful web service that allows you to manage and retrieve information about various matches and their results.

## Features

- Create, Read, Update, and Delete (CRUD) operations for match records.
- Retrieve a list of all matches.
- Retrieve details of a specific match by its ID.

## Technologies Used

- Django 4.2.6
- Django Rest Framework 3.14.0
- PostgreSQL database (via psycopg2)
- Python 3.9
- Other dependencies (as specified in requirements.txt)

## Getting Started

To run this project locally on your machine, follow these steps:

1. **Clone the Repository**
2. **Create a Virtual Environment**
3. **Activate the Virtual Environment**
4. **Configure the Database**
5. **Migrate the Database**
6. **Import data.json**
7. **Access the API**

## API Endpoints
GET /match-results/: Retrieve a list of all matches.
POST /match-results/: Create a new match record.
GET /match-results/{id}/: Retrieve details of a specific match by its ID.
PUT /match-results/{id}/: Update an existing match record.
DELETE /match-results/{id}/: Delete an existing match record.