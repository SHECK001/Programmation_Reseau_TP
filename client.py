import requests

def get_all_users():
    response = requests.get("http://localhost:5000/users")
    return response.json()

def create_user(name, email):
    data = {"name": name, "email": email}
    response = requests.post("http://localhost:5000/users")
