#install requirement.txt di linux, pip install -r requirements.txt

from engine import engine
from auth import authentification
from create import createUser
from flask import Flask, request
from flask_restful import Api, Resource
import json, datetime

# inisiasi library flask buat api
app = Flask(__name__)
api = Api(app)

with open("pricelist.json") as file:
        pricelist = json.load(file)

class getAPI(Resource):#tindakan
    def get(self, userInput, key): #kalo ada get request maka
        if key == "melothria":
            res = engine(userInput)
            return { "time": str(datetime.datetime.now()),"response" : res} #respond untuk yang menghit api ini
        else:
            return { "time": str(datetime.datetime.now()),"response" : "Sorry request decline!"}
api.add_resource(getAPI, "/get/<string:key>/<string:userInput>") #kalo di hit dgn method get /hit maka lakukan yang asa di getAPI, slash string userInput artinya harus passing data berupa string melalui url yang akan ditampung di var userINput

#ambil daftar harga
class getAPI2(Resource):#tindakan
    def get(self, key):
        if key == "pricelist":
            return pricelist
        else:
            return { "time": str(datetime.datetime.now()),"response" : "Sorry request decline!"}
api.add_resource(getAPI2, "/get/<string:key>")



#autentifikasi login dan signup
class getAPI3(Resource):#tindakan
    def get(self, phone, password, key):
        if key == "auth":
            res = authentification(phone, password)
            return res
        elif key == "create":
            res = createUser(phone, password)
            return res
        else:
            return { "time": str(datetime.datetime.now()),"response" : "Sorry request decline!"}
api.add_resource(getAPI3, "/get/<string:key>/<string:phone>/<string:password>")



class postAPI(Resource): #tindakan
    def post(self): #kalo ada post request maka
        res = engine(request.form['userInput']) #request.form tangkap body yang dikirimkan saat hit
        return { "time": str(datetime.datetime.now()),"response" : res} #respon dari api
api.add_resource(postAPI, "/hit") #kalo di hit dgn method post /hit maka lakukan yang asa di postAPI





#debugging api kita apakah sudah jalan/ proses apa yang dilakukan api
if __name__ == "__main__":
    app.run(debug=True)

    

