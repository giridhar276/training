import requests

# API endpoint
url = "https://fakestoreapi.com/products"

# Query parameters
# limit = number of records
# sort = asc or desc
params = {
    "limit": 5,
    "sort": "desc"
}

# Send GET request with params
response = requests.get(url, params=params)

# Print final URL created by requests
print("Final URL:", response.url)

# Convert response to JSON
products = response.json()

# Display products
for product in products:
    print(product["id"], product["title"], product["price"])
