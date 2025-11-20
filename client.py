import requests

BASE_URL = "http://127.0.0.1:5000/users"

# -----------------------------
# 1️⃣ POST - Add a new user
# -----------------------------
def add_user():
    data = {
        "name": "Binisha",
        "age": 20
    }
    response = requests.post(BASE_URL, json=data)
    print("POST Response:", response.json())


# -----------------------------
# 2️⃣ GET - Get all users
# -----------------------------
def get_users():
    response = requests.get(BASE_URL)
    print("GET Response:", response.json())


# -----------------------------
# 3️⃣ PUT - Update user (user_id = 1)
# -----------------------------
def update_user():
    user_id = "1"   # change ID if needed
    update_data = {
        "name": "Binisha Updated",
        "age": 21
    }
    response = requests.put(f"{BASE_URL}/{user_id}", json=update_data)
    print("PUT Response:", response.json())


# -----------------------------
# 4️⃣ DELETE - Delete user (user_id = 1)
# -----------------------------
def delete_user():
    user_id = "1"  # change if needed
    response = requests.delete(f"{BASE_URL}/{user_id}")
    print("DELETE Response:", response.json())


# -----------------------------
# RUN functions here
# -----------------------------
add_user()      # Adds a user
get_users()     # Shows all users
update_user()   # Updates user 1
delete_user()   # Deletes user 1
get_users()     # Show empty again
