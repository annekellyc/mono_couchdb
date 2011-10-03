# Copyright 2011 Anne Kelly <annekellyc@gmail.com>
#
# This file is part of mono_couchdb.
#
# mono_couchdb is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License as published by the 
# Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version.
#
# mono_couchdb is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 
# for more details.
#
# You should have received a copy of the GNU General Public License along 
# with mono_couchdb. If not, see http://www.gnu.org/licenses/.

#!/bin/env/ python 

import insert_documents
import retrieve_documents
import update_documents
import delete_documents
import connection
import generator
import sys
from datetime import datetime

if len(sys.argv) <= 1 or len(sys.argv) != 2:
    print "--> Invalid input. Please type 'insert', 'retrieve', 'update' or 'delete' to run the program."
elif str(sys.argv[1]) != "insert"  and str(sys.argv[1]) != "retrieve" and str(sys.argv[1]) != "update" and str(sys.argv[1]) != "delete":
    print "--> Invalid input. Please type 'insert', 'retrieve', 'update' or 'delete' to run the program."
else:
    server = connection.create()
    db = ""
        
    print "\n--> Preparing test scenario. It may take a few minutes."
    scenario_01 = generator.generate_post(10)
    scenario_02 = generator.generate_post(100)
    scenario_03 = generator.generate_post(1000)
    scenario_04 = generator.generate_post(10000)
    scenario_05 = generator.generate_post(100000)    
    
    ids_scenario_01 = []
    ids_scenario_02 = []
    ids_scenario_03 = []
    ids_scenario_04 = []
    ids_scenario_05 = []
        
    scenario_list = [scenario_01, scenario_02, scenario_03, scenario_04, scenario_05]
    ids_scenario_list = [ids_scenario_01, ids_scenario_02, ids_scenario_03, ids_scenario_04, ids_scenario_05]

    def execute_function(function, db):
        print "\n::: START RUNNING THE COUCHDB TESTS WITH " + str(len(scenario_list)) + " SCENARIOS :::\n"               
       
        number_of_doc = 100 
        number_scenario = 1                 
        for scenario in scenario_list:   
            try:
               db = server.create('posts')
            except:
               server.delete('posts')
               db = server.create('posts')
            
            print "\nSCENARIO " + str(number_scenario) + " " + str(datetime.now())
            if function == insert_documents.insert:
                function(db, scenario)
            else:
                ids_scenario_list[number_scenario - 1] = insert_documents.bulk_insert(db, scenario)                                     
                function(db, ids_scenario_list[number_scenario - 1])

            number_of_doc = number_of_doc * 10 
            number_scenario += 1   
   
    def execute_program():
        try:            
            param = str(sys.argv[1])       
            if param == "insert":            
                execute_function(insert_documents.insert, db)
            if param == "retrieve":            
                execute_function(retrieve_documents.retrieve, db)
            if param == "update":
                execute_function(update_documents.update, db)
            if param == "delete":
                execute_function(delete_documents.remove, db)
        except Exception:
            print "--> Error executing the program."

    execute_program()
    print "\nEnd: " + str(datetime.now())


