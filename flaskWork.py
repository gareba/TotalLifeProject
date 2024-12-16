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

def get_clinician():
    pass

def post_clinician():
    pass

def modify_clinician():
    pass

def remove_clinician():
    pass


def get_appointment():
    pass

def post_appointment():
    pass

def modify_appointment():
    pass

def remove_appointment():
    pass

@app.route("/get-patient/<pid>") #no need to specify method since get is default
def get_patient(pid):

    patientTuple = CRUDpatients.read_patient(pid)
    #patient tuple has the order (pid, firstName, lastName, age, insuranceProvider, policyNumber, emergContact)
    patientDict = dict()
    patientDict["pid"] = patientTuple[0]
    patientDict["firstName"] = patientTuple[1]
    patientDict["lastName"] = patientTuple[2]
    patientDict["age"] = patientTuple[3]
    patientDict["insuranceProvider"] = patientTuple[4]
    patientDict["policyNumber"] = patientTuple[5]
    patientDict["emergContact"] = patientTuple[6]

    return jsonify(patientDict), 200

@app.route("/get-patient/<pid>", methods = ['POST'])
def post_patient():
    pass

@app.route("/modify-patient/<pid>", methods = ['PUT'])
def modify_patient():
    pass

@app.route("/get-patient/<pid>", methods = ['DELETE'])
def remove_patient():



    CRUDpatients.delete_patient()
    return jsonify(), 200


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
