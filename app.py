from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}  # Dictionary to store user data

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = str(len(users) + 1)
    users[user_id] = data
    return jsonify({"id": user_id, "user": data}), 201

# Update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id] = data
        return jsonify({"id": user_id, "user": data}), 200
    return jsonify({"error": "User not found"}), 404

# Delete user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        users.pop(user_id)
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
