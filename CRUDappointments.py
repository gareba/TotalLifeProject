from flask import Flask, request, jsonify
import sqlite3
import requests # for the api

#CRUD FUNCTIONS FOR appointments table
#Database name is hardcoded for development purposes, it will only work if there is a matching name and spec database in the same working directory as this file

#CREATE 
def create_appointment(NPInum, pid, date,time,location,duration):
    dbname = "part1DB.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    statement = '''INSERT INTO appointments (NPInum, patient, date, time, location, duration) VALUES (?,?,?,?,?,?);'''
    data = (NPInum, pid, date,time,location,duration) #tuple of all args here
    c.execute(statement,data)
    conn.commit()
    return

#READ 
def read_appointment(NPInum, pid):
    # need to do: implement functionality for filtering by times 
    dbname = "part1DB.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''SELECT FROM appointments where NPInum == :clinician and pid == :patient info;''',{"clinician":NPInum, "patient": pid})
    appointments = c.fetchall()
    success = True
    for appointment in appointment:
            print(appointment)
    conn.commit()
    conn.close()
    return appointments


#UPDATE 
def update_appointment(NPInum, pid, date, time, dictionary):
        data = []
        dbname = "part1DB.db"
        statement = '''UPDATE appointments SET '''
        for field in ("location","duration"):
              if field in dictionary:
                    data.append(dictionary[field])
                    statement = statement + field + ''' = ?, '''

        statement = statement[:len(statement) -2]
        statement = statement + ''' where pid == ? and NPInum == ? and date == ? and time == ?'''
        data.append(pid,NPInum, date,time)
        data = tuple(data)
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute(statement, data)
        success = True        
        conn.commit()
        conn.close()
        return success


#DELETE 
def delete_appointment(NPInum, pid, date, time):
        dbname = "part1db.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute('''DELETE FROM appointments where NPInum == ? and pid == ? and date == ? and time == ?;''',(NPInum,pid,date,time))
        success = True        
        conn.commit()
        conn.close()
        return success


