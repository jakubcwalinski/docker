from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

@app.route('/primes', methods=['GET'])
def generate_primes():
    limit = int(request.args.get('limit', 100))
    primes = [n for n in range(2, limit) if is_prime(n)]
    return jsonify(primes)

@app.route('/', methods=['GET'])
def welcome():
    return "Hello World! Welcome in prime number generator app!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
