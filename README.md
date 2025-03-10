# TestCase Management API

A FastAPI application for managing user stories and test cases with a PostgreSQL database.

## Project Structure

```
project/
├── main.py          # FastAPI application entry point
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic data validation schemas
└── database.py      # Database configuration
```

## Features

- Manage user stories (create, read)
- Manage test cases (create, read)
- One-to-many relationship between user stories and test cases
- PostgreSQL database integration

## Prerequisites

- Python 3.7+
- PostgreSQL database
- Required Python packages: fastapi, uvicorn, sqlalchemy, pydantic, python-multipart

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic python-multipart
   ```
4. Set up PostgreSQL database and update the connection string in `database.py`

## Database Setup

1. Create a PostgreSQL database named `TestcaseApplication`
2. Update the connection string in `database.py` if needed:
   ```python
   DATABASE_URL = 'postgresql://your_user:your_password@localhost:5432/TestcaseApplication'
   ```

## Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### User Stories

- **GET** `/userstories` - Get all user stories
- **GET** `/userstories/{userstory_id}` - Get a specific user story
- **POST** `/userstories` - Create a new user story

### Test Cases

- **GET** `/testcases` - Get all test cases
- **GET** `/testcases/{testcase_id}` - Get a specific test case
- **POST** `/testcases` - Create multiple test cases

## Example Requests

### Create a User Story
```bash
curl -X POST "http://localhost:8000/userstories" \
-H "Content-Type: application/json" \
-d '{
    "title": "Sample User Story",
    "description": "This is a sample user story description"
}'
```

### Create Test Cases
```bash
curl -X POST "http://localhost:8000/testcases" \
-H "Content-Type: application/json" \
-d '[
    {
        "userstoryid": 1,
        "title": "Test Case 1",
        "description": "Description for test case 1",
        "teststeps": "Step 1, Step 2",
        "expected_result": "Expected result",
        "status": "Not Started",
        "priority": "High",
        "testtype": "Functional"
    }
]'
```

## Database Schema

The application uses two main tables:

### User Stories Table
- id (Primary Key)
- title
- description

### Test Cases Table
- id (Primary Key)
- userstoryid (Foreign Key to User Stories)
- title
- description
- teststeps
- expected_result
- status
- priority
- testtype

## Project Dependencies

- **FastAPI**: Web framework
- **SQLAlchemy**: ORM for database operations
- **Pydantic**: Data validation
- **Uvicorn**: ASGI server

## License

[Add your license information here]