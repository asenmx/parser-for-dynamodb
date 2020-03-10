import json
count = 0
with open('/home/toorhax/PycharmProjects/valery-json-parser/jsons/test.json') as f:
    data = json.load(f)
    for x in data:
        dest = open('./parsed/test' + str(count) + '.json', 'a')
        mydict = {"id": {"S":"%d" %x ['id']},
                       "ip": {"S": x['ip']},
                       "name": {"S": x['name']}
                       }
        count = count +1
        json.dump(mydict, dest)
