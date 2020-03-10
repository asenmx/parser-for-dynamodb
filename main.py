import os
import json
mylist=[]
with open('/home/toorhax/PycharmProjects/valery-json-parser/jsons/test.json') as f:
    data = json.load(f)
    for x in data:
        dest = open('./parsed/' + x, 'a')
        mydict = {"id": {"S": x['id']},
                  "ip": {"S": x['ip']},
                  "name": {"S": x['name']}
                  }
        mylist.append(mydict)
        json.dump(mylist, dest)
