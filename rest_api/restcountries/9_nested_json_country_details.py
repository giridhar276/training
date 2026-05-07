import requests

url = "https://restcountries.com/v3.1/name/japan"

response = requests.get(url)

countries = response.json()

country = countries[0]

print("Country:", country["name"]["common"])
print("Official Name:", country["name"]["official"])
print("Capital:", country.get("capital", ["No Capital"])[0])
print("Flag PNG:", country["flags"]["png"])

# Extract currencies
print("\nCurrencies:")
currencies = country.get("currencies", {})

for code, details in currencies.items():
    print(code, "-", details.get("name"), "-", details.get("symbol"))

# Extract languages
print("\nLanguages:")
languages = country.get("languages", {})

for code, language in languages.items():
    print(code, "-", language)
