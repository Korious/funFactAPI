import math
import asyncio
import aiohttp
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from functools import lru_cache

app = Flask(__name__)
CORS(app)

# Helper Functions
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(abs(n))) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    if n <= 0:  # Perfect numbers are positive integers
        return False
    total = 1  # Start with 1 as a divisor
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Add the complementary divisor
                total += n // i
    return total == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(digit) for digit in str(abs(n))]
    num_digits = len(digits)
    return sum(digit ** num_digits for digit in digits) == abs(n)

def digit_sum(n):
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(abs(n)))

@lru_cache(maxsize=1000)
async def fetch_fun_fact(session, n):
    """Fetch a fun fact about the number from Numbers API."""
    try:
        async with session.get(f"http://numbersapi.com/{n}/math?json") as response:
            if response.status == 200:
                data = await response.json()
                return data.get("text", "No fun fact available")
            return "No fun fact available"
    except Exception:
        return "Error fetching fun fact"

async def get_fun_fact_async(n):
    """Wrapper to manage the async session for fetching fun facts."""
    async with aiohttp.ClientSession() as session:
        return await fetch_fun_fact(session, n)

def classify_properties(n):
    """Classify the properties of the number."""
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    properties.append("even" if n % 2 == 0 else "odd")
    return properties

def create_response(number, fun_fact):
    """Create a structured response dictionary."""
    properties = classify_properties(number)
    
    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    }

# API Endpoint
@app.route('/api/classify-number', methods=['GET'])
async def classify_number():
    # Get the 'number' parameter from the query string
    number = request.args.get('number')
    
    # Input validation: Check for valid integers (positive or negative)
    try:
        number = int(number)
    except (ValueError, TypeError):
        return jsonify({
            "number": "alphabet",
            "error": True
        }), 400

    # Fetch fun fact asynchronously
    fun_fact = await get_fun_fact_async(number)

    # Create structured response
    response = create_response(number, fun_fact)

    return jsonify(response)

# Handle CORS (Cross-Origin Resource Sharing)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)