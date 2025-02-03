import math
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Helper Functions
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(digit) for digit in str(n)]
    num_digits = len(digits)
    return sum(digit ** num_digits for digit in digits) == n

def digit_sum(n):
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

def get_fun_fact(n):
    """Fetch a fun fact about the number from Numbers API."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            data = response.json()
            return data.get("text", "No fun fact available")
        return "No fun fact available"
    except Exception as e:
        return "Error fetching fun fact"

def classify_properties(n):
    """Classify the properties of the number."""
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

# API Endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Get the 'number' parameter from the query string
    number = request.args.get('number')
    
    # Input validation
    if not number or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400
    
    number = int(number)

    # Calculate properties
    properties = classify_properties(number)
    fun_fact = get_fun_fact(number)
    digit_sum_value = digit_sum(number)

    # Create response
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum_value,
        "fun_fact": fun_fact
    }

    return jsonify(response)

# Handle CORS (Cross-Origin Resource Sharing)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)