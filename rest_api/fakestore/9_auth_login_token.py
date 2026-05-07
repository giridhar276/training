import requests

# Login endpoint
url = "https://fakestoreapi.com/auth/login"

# Login credentials provided by FakeStoreAPI
login_data = {
    "username": "mor_2314",
    "password": "83r5^_"
}

# Send POST request for login
response = requests.post(url, json=login_data)

print("Status Code:", response.status_code)

# Convert response to JSON
data = response.json()

# Extract token
token = data.get("token")

print("Token:", token)

# Example of how token is generally passed in headers
headers = {
    "Authorization": f"Bearer {token}"
}

print("Authorization Header:")
print(headers)

# Note:
# FakeStoreAPI returns a token, but most public endpoints do not require that token.
