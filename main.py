import os
import json
mylist=[]
with open('/home/toorhax/PycharmProjects/valery-json-parser/jsons/test.json') as f:
    dest = open('./parsed/test.json', 'a')
    data = json.load(f)
    for x in data:
        mydict = {"id": {"S": x['id']},
                       "ip": {"S": x['ip']},
                       "name": {"S": x['name']}
                       }
        mylist.append(mydict)
    json.dump(mylist, dest)
