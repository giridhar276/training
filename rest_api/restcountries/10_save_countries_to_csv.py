import csv
import requests

url = "https://restcountries.com/v3.1/all"

params = {
    "fields": "name,capital,region,subregion,population,area"
}

response = requests.get(url, params=params)

countries = response.json()

# Create CSV file
with open("countries_output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow([
        "country_name",
        "capital",
        "region",
        "subregion",
        "population",
        "area"
    ])

    # Write country rows
    for country in countries:
        name = country["name"]["common"]
        capital = country.get("capital", ["No Capital"])[0]
        region = country.get("region", "")
        subregion = country.get("subregion", "")
        population = country.get("population", 0)
        area = country.get("area", 0)

        writer.writerow([
            name,
            capital,
            region,
            subregion,
            population,
            area
        ])

print("countries_output.csv file created successfully.")
