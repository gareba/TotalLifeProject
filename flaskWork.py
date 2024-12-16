from flask import Flask, request, jsonify
import sqlite3
import requests # for the api
import NPITEST
import CRUDappointments
import CRUDpatients
import CRUDclinicians

# This is my first attempt at using flask, I used a starter tutorial to get myself started
# https://www.youtube.com/watch?v=zsYIw6RXjfM

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "name": "John Doe",
        "email" : "Jd@email.com"
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200 #returning data, use code 200

#have to specify the functions used here (POST) since get is default
@app.route("/create-user",methods = ["POST"])
def create_user():
    #only needed if you have multiple
    if request.method == "POST":
        data = request.get_json()

        #add to a database

        return jsonify(data), 201 




#@app.route("/get-clinician/<>")
#def get_clinician():
#    return



if __name__ == "__main__":
    app.run(debug=True)
