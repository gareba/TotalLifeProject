from flask import Flask, request, jsonify
import sqlite3
import requests # for the api

#CRUD FUNCS FOR CLINICIANS

#CREATE 
def create_patient(pid, firstName = None, lastName = None, age = None, insuranceProvider = None, policyNumber = None, emergContact = None):
    # if everything is all fine and dandy, go ahead and add to the database. 
    dbname = "part1DB.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    statement = '''INSERT INTO patients (pid, firstName, lastName, age, insuranceProvider, policyNumber, emergContact) VALUES (?,?,?,?,?,?,?);'''
    data = (pid, firstName,lastName,age,insuranceProvider,policyNumber,emergContact) #tuple of all args here
    c.execute(statement,data)
    conn.commit()
    return

#READ 
def read_patient(pid):
    # need to do: implement functionality for filtering by times 
    dbname = "part1DB.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''SELECT * FROM patients where pid == :patient ;''',{"patient":pid})
    patients = c.fetchall()
    success = True
    for patient in patients:
            print(patient)
            
    conn.commit()
    conn.close()
    return success


#UPDATE 
def update_patient(pid, dictionary):
        #i need to dynamically handle what things are being updated, oh wait i can just use a dict
        data =  []
        statement = '''UPDATE  patients 
                  SET '''
        for field in ("firstName","lastName","age", "policyNumber", "insuranceProvider", "emergencyContact"):
                if field in dictionary:
                        data.append(dictionary[field])
                        statement = statement + field + ''' = ?, ''' 
        
        statement = statement[:len(statement)-2]
        statement = statement + ''' where pid == ?'''
        data.append(pid)
        data = tuple(data)

        print(statement)
        print(data)
        dbname = "part1DB.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute(statement, data)
        success = True        
        conn.commit()
        conn.close()
        return success


#DELETE 
def delete_patient(pid):
        dbname = "part1DB.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute('''DELETE FROM patients where pid == :patient;''', {"patient":pid})
        success = True        
        conn.commit()
        conn.close()
        return success


def main():
      #create_patient(1, "Gaven", "Barnes", 22, "Greenshield", 4421, 7805557423)
      #delete_patient(1)
      #read_patient(1)

      dictionary = {"firstName" : "Gaven2"}
      update_patient(1,dictionary)

main()