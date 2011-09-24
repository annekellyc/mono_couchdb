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

server = connection.create()

try:
   db = server.create('posts')
except:
   server.delete('posts')
   db = server.create('posts')
   
# Create scenarios
scenario_01 = generator.generate_post(1)
scenario_02 = generator.generate_post(5)
scenario_03 = generator.generate_post(50)
#scenario_04 = generator.generate_post(100)
#scenario_05 = generator.generate_post(500)
#scenario_06 = generator.generate_post(1000)
#scenario_07 = generator.generate_post(5000)
#scenario_08 = generator.generate_post(10000)
#scenario_09 = generator.generate_post(25000)
#scenario_10 = generator.generate_post(50000)
#scenario_11 = generator.generate_post(75000)
#scenario_12 = generator.generate_post(100000)
#scenario_13 = generator.generate_post(1000000)


def execute_insert_document_tests():

    print "\n::: RESULT INSERT :::\n"
    insert_documents.insert(db, scenario_01)
    #insert_documents.insert(db, scenario_02)
    #insert_documents.insert(db, scenario_03)

def execute_retrieve_document_tests():

    print "\n::: RESULT RETRIEVE :::\n"
    retrieve_documents.retrieve(db, scenario_01)
    #retrieve_documents.retrieve(db, scenario_02)
    #retrieve_documents.retrieve(db, scenario_03)

def execute_update_document_tests():

    print "\n::: RESULT UPDATE :::\n"
    update_documents.update(db, scenario_01)
    #retrieve_documents.retrieve(db, scenario_02)
    #retrieve_documents.retrieve(db, scenario_03)
    
def execute_delete_document_tests():

    print "\n::: RESULT DELETE :::\n"
    delete_documents.remove(db, scenario_01)
    #retrieve_documents.retrieve(db, scenario_02)
    #retrieve_documents.retrieve(db, scenario_03)

def execute():
    try:
        execute_insert_document_tests()
        execute_retrieve_document_tests()
        execute_update_document_tests()
        execute_delete_document_tests()
    except Exception:
        print "--> Erro ao executar o programa."

execute()



