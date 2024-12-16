from flask import Flask, request, jsonify
import sqlite3
import requests # for the api

#CRUD FUNCS FOR CLINICIANS

#CREATE 
def create_patient():
    # if everything is all fine and dandy, go ahead and add to the database. 
    dbname = "part1db.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    statement = '''INSERT INTO patients (db parameters here ) VALUES (?,?,?,?,?,?);'''
    data = () #tuple of all args here
    c.execute(statement,data)
    conn.commit()
    return

#READ 
def read_patient():
    # need to do: implement functionality for filtering by times 
    dbname = "part1db.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''SELECT FROM clinician where NID == patient info;''')
    appointments = c.fetchall()
    success = True
    for appointment in appointment:
            print("display patient information ")
            
    conn.commit()
    conn.close()
    return success


#UPDATE 
def update_patient():
        dbname = "part1db.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute('''UPDATE  patient 
                  SET f1 = v1, etc etc
                  where NID == patient info;''')
        success = True        
        conn.commit()
        conn.close()
        return success


#DELETE 
def delete_patient():
        dbname = "part1db.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute('''DELETE FROM patients where NID == patient;''')
        success = True        
        conn.commit()
        conn.close()
        return success


