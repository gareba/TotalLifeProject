from flask import Flask, request, jsonify
import sqlite3
import requests # for the api

def test(NPI):
#https://www.youtube.com/watch?v=hpc5jyVpUpw&embeds_referring_euri=https%3A%2F%2Fwww.bing.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.bing.com&source_ve_path=Mjg2NjY
    print(str(NPI))
    print("https://npiregistry.cms.hhs.gov/api/?number="+ str(NPI) +"&enumeration_type=&taxonomy_description=&name_purpose=&first_name=&use_first_name_alias=&last_name=&organization_name=&address_purpose=&city=&state=&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1")
    response = requests.get("https://npiregistry.cms.hhs.gov/api/?number="+ str(NPI) +"&enumeration_type=&taxonomy_description=&name_purpose=&first_name=&use_first_name_alias=&last_name=&organization_name=&address_purpose=&city=&state=&postal_code=&country_code=&limit=&skip=&pretty=&version=2.1")
    dictionary = response.json()
    print(dictionary)

    '''
    dictionary['results'] # if the results are empty
    print("There is no doctor with that NPI number, check it is entered correctly and try again")
    
    dictionary['results'] # if the results are not empty, but the names dont match
    print("The name specified does not match the database. Ensure it is spellect correctly, and try again. ")
    '''

def main():
    NPI = input("Enter an NPI number:")

    test(NPI)


main()