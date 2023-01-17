import json

# Open the JSON file
with open('services.json', 'r') as json_file:
    # Load the JSON data from the file
    data = json.load(json_file)

# Get the services data
services = data["services"]

# Iterate over the services
for service in services:
    if service != "debug":
        print(f"{service} : {services[service]['name']}")
