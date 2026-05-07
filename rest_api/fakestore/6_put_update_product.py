import requests

# Product ID to update
product_id = 1

# API endpoint
url = f"https://fakestoreapi.com/products/{product_id}"

# Full updated product data
updated_product = {
    "title": "Updated Python Course",
    "price": 1499,
    "description": "Updated Python course with REST API examples.",
    "image": "https://example.com/python-course.png",
    "category": "education"
}

headers = {
    "Content-Type": "application/json"
}

# PUT is used to replace/update a resource
response = requests.put(url, json=updated_product, headers=headers)

print("Status Code:", response.status_code)
print("Updated Product Response:")
print(response.json())
