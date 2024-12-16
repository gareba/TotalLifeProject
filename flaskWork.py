from flask import Flask, request, jsonify
import sqlite3
import requests # for the api

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
#GET
#PUT 
#POST update
#DELETE

#CRUD FUNCS FOR CLINICIANS

#CREATE 
def create_clinician():

    #https://www.youtube.com/watch?v=hpc5jyVpUpw&embeds_referring_euri=https%3A%2F%2Fwww.bing.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.bing.com&source_ve_path=Mjg2NjY

    response = requests.get("https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&name_purpose=&first_name=steve&use_first_name_alias=&last_name=&organization_name=&address_purpose=&city=&state=&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1")
    dictionary = response.json()
    dictionary['results'] # if the results are empty
    print("There is no doctor with that NPI number, check it is entered correctly and try again")
    
    dictionary['results'] # if the results are not empty, but the names dont match
    print("The name specified does not match the database. Ensure it is spellect correctly, and try again. ")



    # if everything is all fine and dandy, go ahead and add to the database. 
    dbname = "part1db.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    statement = '''INSERT INTO clinicians (db parameters here ) VALUES (?,?,?,?,?,?);'''
    data = () #tuple of all args here
    c.execute(statement,data)
    conn.commit()
    return

#READ CLINICIAN
def read_clinician():
    # need to do: implement functionality for filtering by times 
    dbname = "part1db.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''SELECT FROM clinician where NID == clinician info;''')
    appointments = c.fetchall()
    success = True
    for appointment in appointment:
            print("display clinician information ")
            
    conn.commit()
    conn.close()
    return success


#UPDATE CLINICIAN
def delete_clinician():
        dbname = "part1db.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute('''UPDATE  clinician 
                  SET f1 = v1, etc etc
                  where NID == clinician info;''')
        success = True        
        conn.commit()
        conn.close()
        return success


#DELETE CLINICIAN
def delete_clinician():
        dbname = "part1db.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute('''DELETE FROM clinician where NID == clinician info;''')
        success = True        
        conn.commit()
        conn.close()
        return success




def create_patient():
    dbname = "part1db.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    statement = '''INSERT INTO patients (db parameters here ) VALUES (?,?,?,?,?,?);'''
    data = () #tuple of all args here
    c.execute(statement,data)
    conn.commit()
    return

def get_appointments():

    # need to do: implement functionality for filtering by times 
    dbname = "part1db.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''SELECT FROM appointments where clinician == clinician info;''')
    appointments = c.fetchall()
    success = True
    for appointment in appointment:
            print("placeholder for displaying the appointments")
            
    conn.commit()
    return success



#CRUD OPERATIONS: Need 1 of each type per table, 12 total 



#@app.route("/get-clinician/<>")
#def get_clinician():
#    return



if __name__ == "__main__":
    app.run(debug=True)
