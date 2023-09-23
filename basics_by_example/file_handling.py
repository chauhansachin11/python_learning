import time
import json
import os

# f = open("class_1.py","a")
# f.write("print(\"append new line\")")

# f.close()

# f = open("class_1.py","r")

# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# f.close()

a = {
    "name":"Sachin",
    "salary":2000000,
    "city":"Bijnor"
}

file_name = str(time.time())


with open(f'{file_name}.json', 'w') as fp:
    fp.write(json.dumps(a))

d = {}
if(os.path.exists("d.json")):
    with open("d.json",'w+') as fp:
        data = fp.read()
        if(data):
            d = json.loads(data)
d[file_name] = a["name"]
with open("d.json",'w') as fp:
    fp.write(json.dumps(d))



