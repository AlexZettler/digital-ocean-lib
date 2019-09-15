import os
import json
dicts = {}
lists = []
json_payload_template = {
            "name": "aeda",
            "description": "te",
            "purpose": "Web",
            "environment": "Developmeent"
        }
json_data ='{ "name":"John", "age":30, "city":"New York"}'
json_str = json.loads(json_data)
print(json_str)

allowed_envs = ['Development','Production','Testing']

if json_payload_template['environment'] in allowed_envs:
    print("No")
else:
    print("yes")