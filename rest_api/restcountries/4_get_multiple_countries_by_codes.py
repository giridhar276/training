import requests

# Search multiple countries using comma-separated codes
url = "https://restcountries.com/v3.1/alpha"

params = {
    "codes": "ind,usa,gbr,jpn"
}

response = requests.get(url, params=params)

print("Final URL:", response.url)

countries = response.json()

for country in countries:
    print("Country:", country["name"]["common"])
    print("Capital:", country.get("capital", ["No Capital"])[0])
    print("-" * 40)
