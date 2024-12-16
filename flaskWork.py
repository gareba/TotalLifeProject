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

@app.route("get-clinician/<NPInum>")
def get_clinician(NPInum):
    
    clinicianTuple = CRUDclinicians.read_clinician(NPInum)
    #clinician tuple has the order (NPInum, firstName, lastName, state, specialty)
    clinicianDict = dict()
    clinicianDict["NPInum"] = clinicianTuple[0]
    clinicianDict["firstName"] = clinicianTuple[1]
    clinicianDict["lastName"] = clinicianTuple[2]
    clinicianDict["state"] = clinicianTuple[3]
    clinicianDict["specialty"] = clinicianTuple[4]
    
    return jsonify(clinicianDict), 200
    
@app.route("/post-clinician/<NPInum>", methods = ["POST"])
def post_clinician(NPInum):
    CRUDclinicians.create_clinician(NPInum, request.args)

    return jsonify({"success": True})
    

@app.route("/modify-clinician/<NPInum>", methods = ["PUT"])
def modify_clinician(NPInum):
     
    CRUDclinicians.update_clinician(NPInum, request.args)
    return jsonify({"success": True})


@app.route("/remove-clinician/<NPInum>", methods = ["DELETE"])
def remove_clinician(NPInum):
    #need to verify that the clinician exists in the first place and that they have been deleted
    CRUDclinicians.delete_clinician(NPInum)
    return jsonify({"success": True})

@app.route("get-appointment/clinician/<NPInum>/patient/<pid>")
def get_appointment(NPInum,pid):
    apptTuple = CRUDappointments.read_appointment(NPInum,pid)[0]
    apptDict = dict()
    apptDict["NPInum"] = apptTuple[0]
    apptDict["pid"] = apptTuple[1]
    apptDict["date"] = apptTuple[2]
    apptDict["time"] = apptTuple[3]
    apptDict["location"] = apptTuple[4]
    apptDict["duration"] = apptTuple[5]

    return jsonify(apptDict), 200


#retrieves all appointments for a specific doctor patient pair
@app.route("post-appointment/clinician/<NPInum>/patient/<pid>/date/<date>/time/<time>", methods = ['POST'] )
def post_appointment(NPInum,pid,date,time):
    CRUDappointments.create_appointment(NPInum,pid,date,time)
    return jsonify({"success": True})

@app.route("modify-appointment/clinician/<NPInum>/patient/<pid>/date/<date>/time/<time>", methods = ['PUT'])
def modify_appointment(NPInum,pid,date,time):
    CRUDappointments.update_appointment(NPInum,pid,date,time, request.args)
    return jsonify({"success": True})
    

@app.route("remove-appointment/clinician/<NPInum>/patient/<pid>/date/<date>/time/<time>", methods = ['DELETE'])
def remove_appointment(NPInum,pid,date,time):
    CRUDappointments.delete_appointment(NPInum,pid,date,time)
    return jsonify({"success": True})

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


#missing data validation
@app.route("/post-patient/<pid>", methods = ['POST'])
def post_patient(pid):

    CRUDpatients.create_patient(pid, request.args)

    return jsonify({"success": True})
    

#missing data validation
@app.route("/modify-patient/<pid>", methods = ['PUT'])
def modify_patient(pid):
    
    CRUDpatients.update_patient(pid, request.args)
    return jsonify({"success": True})

@app.route("/remove-patient/<pid>", methods = ['DELETE'])
def remove_patient(pid):

    #need to verify that the patient exists in the first place and that they have been deleted
    CRUDpatients.delete_patient(pid)
    return jsonify({"success": True})


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
