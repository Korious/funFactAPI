# Number Classification API

A lightweight Python-based API that analyzes a given number, identifies its mathematical properties, and provides a fun fact about it.

## API Endpoint
- `GET` /api/classify-number?number=<number>

**Query Parameters:**
- `number` (required): The integer to classify.

## Response Format

### Success Response (200 OK)

If the input is a valid integer, the API returns a similar JSON structure:

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**Fields:**
- `number`: The input number.
- `is_prime`: Boolean indicating whether the number is prime.
- `is_perfect`: Boolean indicating whether the number is a perfect number.
- `properties`: An array of mathematical properties:
  - `"armstrong"`: If the number is an Armstrong number.
  - `"even"` or `"odd"`: Indicates whether the number is even or odd.
- `digit_sum`: The sum of the digits of the number.
- `fun_fact`: A fun fact about the number, fetched from the Numbers API.

### Error Response (400 Bad Request)

If the input is invalid (e.g., not a valid integer), the API returns:

```json
{
    "number": "invalid_input",
    "error": true
}
```

**Fields:**
- `number`: The invalid input provided by the user.
- `error`: Boolean indicating an error occurred.

## Example Usage

**Request:**

```
GET /api/classify-number?number=371
```

**Success Response:**

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**Error Response:**

```bash
GET /api/classify-number?number=abc
```

```json
{
    "number": "abc",
    "error": true
}
```

## Features

- Identifies if a number is:
  - Prime
  - Perfect
  - Armstrong
  - Even or Odd
- Calculates the sum of its digits.
- Fetches a fun fact from the Numbers API (http://numbersapi.com/).
- Handles invalid inputs gracefully with appropriate error responses.
- Supports Cross-Origin Resource Sharing (CORS).

## Deployment

The API is deployed on a publicly accessible endpoint. You can test it using tools like Postman, curl, or directly in your browser.

## Technology Stack

- Programming Language: Python 🐍
- Framework: Flask (with async support)
- Asynchronous HTTP Requests: aiohttp
- Hosting Platform: Render (https://funfactapi-n4au.onrender.com)

## How to Run Locally

1. Clone this repository:

    ```bash
    git clone https://github.com/Korious/funFactAPI.git
    cd funFactAPI
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # For Linux/MacOS
    venv\Scripts\activate      # For Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. Access the API locally at:

    ```text
    http://127.0.0.1:5000/api/classify-number?number=<number>
    ```

**thank you 💗**