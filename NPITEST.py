from flask import Flask, request, jsonify
import sqlite3
import requests # for the api

def verifyNPI(NPI, firstName, lastName, state):
#https://www.youtube.com/watch?v=hpc5jyVpUpw&embeds_referring_euri=https%3A%2F%2Fwww.bing.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.bing.com&source_ve_path=Mjg2NjY
    #print(str(NPI))
    #print("https://npiregistry.cms.hhs.gov/api/?number="+ str(NPI) +"&enumeration_type=&taxonomy_description=&name_purpose=&first_name=&use_first_name_alias=&last_name=&organization_name=&address_purpose=&city=&state=&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1")
    response = requests.get("https://npiregistry.cms.hhs.gov/api/?number="+ str(NPI) +"&enumeration_type=&taxonomy_description=&name_purpose=&first_name=&use_first_name_alias=&last_name=&organization_name=&address_purpose=&city=&state=&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1")
    dictionary = response.json()
    #print(dictionary['result_count'])
    #print(dictionary['results'][0]['addresses'][0]['state'])
    
    
    if(dictionary['result_count']==0):
        print("There is no doctor with that NPI number, check it is entered correctly and try again")
        return False, None,None,None
    
    if(dictionary['results'][0]['basic']['first_name']!= firstName or dictionary['results'][0]['basic']['last_name'] != lastName or dictionary['results'][0]['addresses'][0]['state'] != state ):# if the results are not empty, but the names or state dont match
        print("The name specified does not match the database. Ensure it is spellect correctly, and try again. ")
        return False, None, None, None
    
    else:
        print(dictionary['results'][0]['basic']['first_name'])
        print(dictionary['results'][0]['basic']['last_name'])
        print(dictionary['results'][0]['addresses'][0]['state'])

        return True, dictionary['results'][0]['basic']['first_name'], dictionary['results'][0]['basic']['last_name'], dictionary['results'][0]['addresses'][0]['state']



        #print("Success!")

def main():
    NPI = input("Enter an NPI number:")
    firstName = input().upper()
    lastName = input().upper()
    state = input().upper()

    #    state = input("Please only enter a 2 character state abbreviation")

    verifyNPI(NPI, firstName, lastName, state)


main()