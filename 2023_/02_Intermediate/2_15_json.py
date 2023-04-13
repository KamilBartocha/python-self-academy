# JSON = JavaScript Object Notation

import json
### JSON Stinngs
json_string = '''
    {
    "students": [
            {
                "id": 1,
                "name": "Kamil",
                "age": "25",
                "full-time": true
            },
            {
                "id": 2,
                "name": "Matu",
                "age": "24",
                "full-time": false
            }
        ]
    }
'''
# json.loads() - load string
# json.load() - load json form file
data = json.loads(json_string)
print(data) # data is a dictionary
print(data['students'][0])

# add value into json obj

data['test'] = True

# dump json data into a string:

new_json = json.dumps(data, indent=2)
new_json = json.dumps(data, indent=2, sort_keys=True)
print(new_json)

### JSON file
# load json file:
with open("2_15_json_file_example.json", "r") as f:
    data = json.load(f)

print(data)


# dump data into json:
with open("2_15_json_file_example_dump.json", "w") as f:
    data = json.dump(data, f)