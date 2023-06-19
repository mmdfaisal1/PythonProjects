import json
from types import SimpleNamespace

json_string_1 = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
json_object_1: dict = json.loads(json_string_1)
print(json_object_1['hometown'])
print(json_object_1['hometown']['name'])

json_string_2 = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
json_object_2 = json.loads(json_string_2, object_hook=lambda d: SimpleNamespace(**d))
print(json_object_2.hometown.name)
print(type(json_object_2))
