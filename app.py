import math
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Helper Functions

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    digits = [int(digit) for digit in str(n)]
    num_digits = len(digits)
    return sum(digit ** num_digits for digit in digits) == n

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def get_fun_fact(n):
    response = requests.get(f'http://numbersapi.com/{n}?json')
    if response.status_code == 200:
        return response.json().get('text', '')
    return "No fun fact available"

def classify_properties(n):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    if is_perfect(n):
        properties.append("perfect")
    if is_prime(n):
        properties.append("prime")
    return properties

# API Endpoints

@app.route('/api', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    
    # Input validation
    if not number.isdigit():
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

# Handle CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)