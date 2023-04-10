import json
from pprint import pprint

contents = ""
with open("sample.json") as file:
    contents = json.loads(file.read())

pprint(contents)
