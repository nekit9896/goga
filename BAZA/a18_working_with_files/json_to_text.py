import json

with open("/path/to/your/file.json", "r") as json_response:
    response_dict = json.load(json_response)
    response_string = json.dumps(response_dict)
    json_response.close()
s = response_string.replace('"', '\\"')
print(s)
