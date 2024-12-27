# Wallet Information Microservice

A microservice built with FastAPI to retrieve and store information about Tron wallet addresses, including balance, bandwidth, and energy.

## Features
- **POST /wallet/**: Fetch wallet details and save the request in the database.
- **GET /wallet/queries/**: Retrieve a paginated list of recent wallet queries.
- Database integration with SQLAlchemy ORM.
- Tron API interaction using `tronpy`.
- Comprehensive unit and integration tests with `pytest`.

## Project Structure
```plaintext
├── config.py     # Configuration for API keys and test address
├── database.py   # Database models and connection
├── main.py       # FastAPI application and endpoints
├── schemas.py    # Pydantic models for request/response validation
├── test_wallet.py # Unit and integration tests
```

## Requirements
- Python 3.9+
- FastAPI
- SQLAlchemy
- Tronpy
- Pytest

Install the dependencies:
```bash
pip install fastapi sqlalchemy tronpy pytest
```

## Configuration
Add your TronGrid API key and a test address in `config.py`:
```python
API_KEY = "your_api_key_here"
TEST_ADDRESS = "your_test_address_here"
```

## Running the Application
1. Initialize the database by running the application.
2. Start the FastAPI server:
```bash
uvicorn main:app --reload
```
3. Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Endpoints
### POST /wallet/
Fetch wallet information and store the request in the database.

**Request Body:**
```json
{
  "address": "wallet_address_here"
}
```

**Response:**
```json
{
  "address": "wallet_address_here",
  "balance": 100,
  "bandwidth": 2000,
  "energy": 500
}
```

### GET /wallet/queries/
Retrieve the paginated list of recent wallet queries.

**Query Parameters:**
- `skip`: Number of records to skip (default: 0).
- `limit`: Maximum number of records to return (default: 10).

**Response:**
```json
[
  {
    "id": 1,
    "address": "wallet_address_here",
    "timestamp": "2024-12-27T12:00:00"
  }
]
```

## Running Tests
Execute unit and integration tests using `pytest`:
```bash
pytest
```

## Notes
- Use a valid Tron wallet address for testing.
- Ensure the database is properly configured in `database.py`.
- Activate Tron addresses by making a transaction if needed.

## License
This project is open-source and available under the MIT License.
