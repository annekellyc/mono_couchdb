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

def remove(db, documents):
    try:
        start = time.clock()    
        for document in documents:
            doc_id = 'post_' + str(document['author'])
            doc = db[doc_id]
            db.delete(doc)    
        elapsed = (time.clock() - start)    
        print "--> " + str(len(documents)) + " deleted document(s). " + "Time: " + str(elapsed)
    except Exception:
        print "--> Erro ao excluir o(s) documento(s)."
    

