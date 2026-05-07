import requests

# Product ID
product_id = 1

# API endpoint for one product
url = f"https://fakestoreapi.com/products/{product_id}"

# Send GET request
response = requests.get(url)

# Convert response to JSON
product = response.json()

# Display product information
print("Product ID:", product["id"])
print("Title:", product["title"])
print("Price:", product["price"])
print("Category:", product["category"])
print("Description:", product["description"])
