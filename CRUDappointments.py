from flask import Flask, request, jsonify
import sqlite3
import requests # for the api

#CRUD FUNCS FOR appointments

#CREATE 
def create_appointment():

    # if everything is all fine and dandy, go ahead and add to the database. 
    dbname = "part1db.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    statement = '''INSERT INTO appointments (db parameters here ) VALUES (?,?,?,?,?,?);'''
    data = () #tuple of all args here
    c.execute(statement,data)
    conn.commit()
    return

#READ 
def read_clinician():
    # need to do: implement functionality for filtering by times 
    dbname = "part1db.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''SELECT FROM appointments where NID == clinician info and pid == patient info;''')
    appointments = c.fetchall()
    success = True
    for appointment in appointment:
            print("display appointment information ")
            
    conn.commit()
    conn.close()
    return success


#UPDATE 
def update_appointment():
        dbname = "part1db.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute('''UPDATE  appointment 
                  SET f1 = v1, etc etc
                  where NID == clinician info and patient and time and date;''')
        success = True        
        conn.commit()
        conn.close()
        return success


#DELETE 
def delete_appointment():
        dbname = "part1db.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute('''DELETE FROM appointment where NID == clinician info;''')
        success = True        
        conn.commit()
        conn.close()
        return success


