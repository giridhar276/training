import requests

# Category name from FakeStoreAPI
category = "jewelery"

# API endpoint
url = f"https://fakestoreapi.com/products/category/{category}"

# Send GET request
response = requests.get(url)

# Convert JSON response to Python list
products = response.json()

print("Category:", category)
print("Total Products:", len(products))

for product in products:
    print("Title:", product["title"])
    print("Price:", product["price"])
    print("-" * 40)
