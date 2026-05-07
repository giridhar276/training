import requests

# API endpoint to get all products
url = "https://fakestoreapi.com/products"

# Send GET request
response = requests.get(url)

# Check status code
print("Status Code:", response.status_code)

# Convert JSON response to Python object
products = response.json()

# Display product details
for product in products:
    print("ID:", product["id"])
    print("Title:", product["title"])
    print("Price:", product["price"])
    print("-" * 50)
