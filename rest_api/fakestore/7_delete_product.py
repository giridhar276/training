import requests

# Product ID to delete
product_id = 1

# API endpoint
url = f"https://fakestoreapi.com/products/{product_id}"

# Send DELETE request
response = requests.delete(url)

print("Status Code:", response.status_code)

# API returns deleted product details
print("Deleted Product:")
print(response.json())
