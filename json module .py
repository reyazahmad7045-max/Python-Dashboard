import json
json_data = '{"name":"Reyaz", "age":21, "city":"patna"}'
py_data = json.loads(json_data)
print('Python format type:', type (py_data))
print('Python format data:', py_data)