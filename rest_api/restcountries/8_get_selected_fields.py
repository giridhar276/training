import requests

# For /all endpoint, fields are recommended
url = "https://restcountries.com/v3.1/all"

params = {
    "fields": "name,capital,region,population"
}

response = requests.get(url, params=params)

print("Final URL:", response.url)

countries = response.json()

for country in countries[:10]:
    print("Name:", country["name"]["common"])
    print("Capital:", country.get("capital", ["No Capital"])[0])
    print("Region:", country["region"])
    print("Population:", country["population"])
    print("-" * 50)
