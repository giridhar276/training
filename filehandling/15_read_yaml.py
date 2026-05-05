

import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

print(config)
print("App Name:", config["app_name"])
print("Database Host:", config["database"]["host"])