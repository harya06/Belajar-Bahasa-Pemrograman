import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, sort_keys=True))   
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# print(json.dumps(x, indent=4, ensure_ascii=False))     
# print(json.dumps(x, indent=4, default=str))
# with open("data.json", "w") as write_file:
#     json.dump(x, write_file)    
# with open("data.json", "r") as read_file:
#     data = json.load(read_file)
# print(data)         
# print(data["name"])
# print(data["age"])
# print(data["cars"])[0]["model"]     
# print(data["cars"])[1]["mpg"]
# print(type(data))
# print(type(y))
# print(type(x))