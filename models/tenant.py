from __init__ import cursor, conn

from owner import Owner
from property import Propertty

class Tenant:
    
    def __init__(self,name,phone_number, email,property_id, id= None):
        self.id = id 
        self.name = name
        self.phone_number= phone_number
        self.email = email
        self.property_id = property_id
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def name(self, phone_number):
        if isinstance(phone_number, int) and len(phone_number):
            self._phone_number = phone_number
        else:
            raise ValueError(
                "Name must be a non-empty integer"
            )
            
    @property
    def email(self):
        return self._email

    @name.setter
    def email(self, email):
        if isinstance(email, str) and len(email):
            self._email = email
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
   
    
    
    @property
    def property_id(self):
        return self._property_id 
    
    @property_id.setter
    def property_id(self, property_id):
        if type(property_id) is int and Propertty.find_by_id(property_id):
            self._property_id = property_id
            
        else:
            raise ValueError(
                " propert_id must reference a property in the database"
            )
    
   
        