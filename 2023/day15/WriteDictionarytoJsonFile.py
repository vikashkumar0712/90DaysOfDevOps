import json

data = {
        "name": 'Vikash',
        'age': 30,
        'address' : {
                'city': 'Mathura',
                'state': 'UP',
                'Country': 'India'
        }

}
with open('data.json', 'w') as outfile:
        json.dump(data, outfile)