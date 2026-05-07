import requests

# fullText=true searches exact country name
url = "https://restcountries.com/v3.1/name/india"

params = {
    "fullText": "true"
}

response = requests.get(url, params=params)

print("Final URL:", response.url)
print("Status Code:", response.status_code)

countries = response.json()

for country in countries:
    print("Country:", country["name"]["common"])
    print("Official:", country["name"]["official"])
