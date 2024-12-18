import sqlite3
import NPITEST


#CRUD FUNCTIONS FOR clinicians table
#Database name is hardcoded for development purposes, it will only work if there is a matching name and spec database in the same working directory as this file


#CREATE 
def create_clinician(NPInum, firstName, lastName, state, specialty= None ):
    status, message = NPITEST.verifyNPI(NPInum, firstName, lastName,state)
   
    if (status == True):
         
        # if everything is all fine and dandy, go ahead and add to the database. 
        dbname = "part1DB.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        statement = '''INSERT INTO clinicians (NPInum, firstName, lastName, state, specialty) VALUES (?,?,?,?,?);'''
        data = (NPInum, firstName, lastName, state, specialty) #tuple of all args here
        c.execute(statement,data)
        conn.commit()
        return True, message
    
    return False, message

#READ CLINICIAN
def read_clinician(NPInum):
    # need to do: implement functionality for filtering by times 
    dbname = "part1DB.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    print(type(NPInum))
    c.execute('''SELECT * FROM clinicians where NPInum == :clinician''',{"clinician":NPInum})
    clinicians = c.fetchall()
    success = True
    for clinician in clinicians:
            print(clinician)
            
    conn.commit()
    conn.close()
    return clinicians[0]


#UPDATE CLINICIAN
def update_clinician(NPInum,dictionary):
        data =[]
        statement = '''UPDATE  clinicians 
                  SET '''
        for field in ("firstName","lastName", "state", "specialty"):
             if field in dictionary:
                  data.append(dictionary[field])
                  statement = statement + field + ''' = ?, '''

        statement = statement[:len(statement)-2]
        statement = statement + ''' where NPInum == ?'''
        data.append(NPInum)
        data = tuple(data)

        dbname = "part1DB.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute(statement,data)
        success = True        
        conn.commit()
        conn.close()
        return success


#DELETE CLINICIAN
def delete_clinician(NPInum):
        dbname = "part1DB.db"
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute('''DELETE FROM clinicians where NPInum == :clinician;''',{"clinician":NPInum})
        success = True        
        conn.commit()
        conn.close()
        return success

