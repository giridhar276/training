import requests

# API endpoint to create product
url = "https://fakestoreapi.com/products"

# Product data to send
new_product = {
    "title": "Python Training Book",
    "price": 999,
    "description": "A practical Python training book for beginners.",
    "image": "https://example.com/python-book.png",
    "category": "books"
}

# Headers tell the API we are sending JSON data
headers = {
    "Content-Type": "application/json"
}

# Send POST request
response = requests.post(url, json=new_product, headers=headers)

print("Status Code:", response.status_code)

# Display response from API
print(response.json())

# Note:
# FakeStoreAPI returns a fake created response.
# It does not permanently save your product.
