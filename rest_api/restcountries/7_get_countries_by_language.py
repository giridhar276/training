import requests

# Get countries where Hindi is used
url = "https://restcountries.com/v3.1/lang/hindi"

response = requests.get(url)

countries = response.json()

print("Countries using Hindi:")

for country in countries:
    print(country["name"]["common"])

    # languages is a dictionary
    languages = country.get("languages", {})

    print("Languages:", list(languages.values()))
    print("-" * 40)
