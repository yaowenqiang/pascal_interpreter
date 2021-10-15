import json
data = {'a':1, 'b': {'c':2}}
print(json.dumps(data))
print(json.dumps(data,indent=4))
print(json.dumps(data,indent=True))
