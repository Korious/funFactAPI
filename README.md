# Number Classification API

A simple Python API that classifies a number and provides interesting mathematical properties along with a fun fact.

## API Endpoint

### `GET /api/classify-number?number=<number>`

#### Query Parameters:
- `number` (required): The number to classify.

#### Response Format:

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}