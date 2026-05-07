import requests

# INR is Indian Rupee
url = "https://restcountries.com/v3.1/currency/inr"

response = requests.get(url)

countries = response.json()

for country in countries:
    print("Country:", country["name"]["common"])

    # currencies is a nested dictionary
    currencies = country.get("currencies", {})

    for code, details in currencies.items():
        print("Currency Code:", code)
        print("Currency Name:", details.get("name"))
        print("Symbol:", details.get("symbol"))

    print("-" * 50)
