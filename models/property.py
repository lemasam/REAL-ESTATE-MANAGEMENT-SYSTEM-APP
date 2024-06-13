from __init__ import CURSOR, CONN

from owner import Owner

class Property:
    
    def __init__(self,address,owner_id, id= None):
        self.id = id 
        self.adress = address
        self.owner_id = owner_id
        
    @property
    def address(self):
        return self._address
  