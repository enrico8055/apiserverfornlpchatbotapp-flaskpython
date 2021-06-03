import json


def createUser(phone, password):
    with open("user.json") as file:
            user = json.load(file)
    # cek apakah sudah ada user di database
    already = 0
    for i, x in enumerate(user['user']):
        if phone == user['user'][i]['phone']:
            already += 1

    #kalo blm ada maka tambahkan
    if already == 0:
        user['user'].append({"phone": phone, "password": password})
        with open('user.json', 'w') as data:
            json.dump(user, data)
        return "success"
    else:
        return "failed"