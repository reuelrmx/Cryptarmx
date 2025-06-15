import os
import json
from encryption import derive_key

USERS_FILE = "data/users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    os.makedirs("data", exist_ok=True)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def register_user(username, master_password):
    users = load_users()
    if username in users:
        raise ValueError("User already exists.")
    salt = os.urandom(16)
    users[username] = {
        "salt": salt.hex()
    }
    save_users(users)
    return derive_key(master_password, salt)

def login_user(username, master_password):
    users = load_users()
    if username not in users:
        raise ValueError("User does not exist.")
    salt = bytes.fromhex(users[username]["salt"])
    return derive_key(master_password, salt)
