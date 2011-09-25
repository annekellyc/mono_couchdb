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

import time
import generator
import constants
import datetime

def update(db, documents):
    try:
        start_c = time.clock()
        start_t = time.time()
        for document in documents:
            doc_id = 'post_' + str(document['author'])
            #print str(db[doc_id])
            doc = db[doc_id]
            doc['author'] = generator.generate_word(constants.number_of_letters)
            db[doc_id] = doc
            #print str(db[doc_id])
        elapsed_c = (time.clock() - start_c)
        elapsed_t = (time.time() - start_t)   
        message = "--> " + str(len(documents)) + " updated document(s).\n " + "Time: " + str(elapsed_c) + " seconds process time and " + str(elapsed_t) + " seconds real time.\n"           
        print message
    except Exception:
        print "--> Error updating document(s)."
    


