from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'POST':
        data = request.json.get("data", [])
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

        response = {
            "is_success": True,
            "user_id": "shruthi_k_1709",
            "email": "shruthi13.krishna@gmail.com",
            "roll_number": "21BCE0092",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response), 200

    elif request.method == 'GET':
        response = {
            "operation_code": 1
        }
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
