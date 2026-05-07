import requests

# IND is the 3-letter country code for India
url = "https://restcountries.com/v3.1/alpha/IND"

response = requests.get(url)

countries = response.json()

for country in countries:
    print("Name:", country["name"]["common"])
    print("Capital:", country.get("capital", ["No Capital"])[0])
    print("Region:", country["region"])
    print("Subregion:", country.get("subregion", "No Subregion"))
