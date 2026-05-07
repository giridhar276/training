import requests

# Create session object
session = requests.Session()

# Common headers for all requests using this session
session.headers.update({
    "Accept": "application/json",
    "User-Agent": "Python-Training-App/1.0"
})

# First API call using same session
products_response = session.get("https://fakestoreapi.com/products?limit=3")
products = products_response.json()

print("Products:")
for product in products:
    print(product["title"])

print("-" * 50)

# Second API call using same session
users_response = session.get("https://fakestoreapi.com/users?limit=3")
users = users_response.json()

print("Users:")
for user in users:
    print(user["username"], "-", user["email"])

# Close session after use
session.close()
