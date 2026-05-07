import requests

# REST Countries API endpoint
url = "https://restcountries.com/v3.1/name/india"

# Send GET request
response = requests.get(url)

# Convert JSON response to Python list
countries = response.json()

# Display country details
for country in countries:
    print("Common Name:", country["name"]["common"])
    print("Official Name:", country["name"]["official"])
    print("Capital:", country.get("capital", ["No Capital"])[0])
    print("Region:", country["region"])
    print("Population:", country["population"])
