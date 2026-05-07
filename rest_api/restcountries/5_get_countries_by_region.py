import requests

# Get all countries from Asia
url = "https://restcountries.com/v3.1/region/asia"

response = requests.get(url)

countries = response.json()

print("Total Asian Countries:", len(countries))

for country in countries:
    print(country["name"]["common"], "-", country.get("capital", ["No Capital"])[0])
