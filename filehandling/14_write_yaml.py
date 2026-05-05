

import yaml

config = {
    "app_name": "TrainingApp",
    "version": 1.0,
    "database": {
        "host": "localhost",
        "port": 3306,
        "user": "admin"
    },
    "debug": True
}

with open("config.yaml", "w") as file:
    yaml.dump(config, file)

print("YAML file created successfully")