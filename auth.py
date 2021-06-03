import json, datetime


def authentification(phone, password):
    with open("user.json") as file:
            user = json.load(file)
    for i, x in enumerate(user['user']):
        print(user['user'][i]['phone'])
        if phone == user['user'][i]['phone']:    
            if user['user'][i]['password'] == password:     
                return { "time": str(datetime.datetime.now()),"response" : "valid"}

    return { "time": str(datetime.datetime.now()),"response" : "failed"}