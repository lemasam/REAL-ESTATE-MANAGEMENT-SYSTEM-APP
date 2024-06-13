from __init__ import cursor, conn

from owner import Owner
from property import Propertty

class Tenant:
    
    def __init__(self,name,phone_number, email,property_id, id= None):
        self.id = id 
        self.name = name
        self.phone_number= phone_number
        self.email = email
  