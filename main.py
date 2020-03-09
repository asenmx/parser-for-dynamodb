import os
import json

for filename in os.listdir("./jsons"):
    with open('./jsons/' + filename) as f:
        dest = open('./parsed/' + filename, 'a')

        data = json.load(f)

        person_dict = {"id": {"S": data['id']},
                       "ip": {"S": data['ip']},
                       "name": {"S": data['name']}
                       }
        json.dump(person_dict, dest)
