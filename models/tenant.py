from db import cursor, conn

from models.owner import Owner
from models.property import Property

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
        if type(property_id) is int and Property.find_by_id(property_id):
            self._property_id = property_id
            
        else:
            raise ValueError(
                " propert_id must reference a property in the database"
            )
    
   
    @classmethod
    def create_table(cls):
        sql ="""
        CREATE TABLE IF NOT EXISTS tenants(
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone_number INTEGER,
            email TEXT,
            property_id INTEGER NOT NULL REFERENCES owner(id))
        """
        cursor.execute(sql)
        conn.commit()
        
    @classmethod
    def drop_table(cls):
        sql ="""
        DROP TABLE IF EXISTS  tenants
        """
        cursor.execute(sql)
        conn.commit()
        
    def save (self):
        sql = """
        INSERT INTO tenants(name,phone_number, email,property_id)
        VALUES (?, ?, ?,?)
        """
        
        cursor.execute(sql,(self.name,self.phone_number, self.email,self.property_id))
        conn.commit () 
        
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
    
    def update (self):
        sql = """
        UPDATE tenants
        SET name= ?, phone_number = ?, email= ?, property_id = ?
        WHERE id = ?
        """
        
        cursor.execute(sql,(self.name,self.phone_number, self.email,self.property_id))
        
        conn.commit()
        
    def delete(self):
        sql = """
        DELETE FROM tenants
        WHERE id = ?
        """
        cursor.execute (sql,(self.id))
        conn.commit()
        
        # delete the dictionary entry using id
        del type(self).all[self.id]
        
        #  setting id to none
        self.id = None
      
    @classmethod
    def instance_from_db(cls,row):
        tenant = cls.all.get(row[0])
        if tenant:
            tenant.name = row[1]
            tenant.phone_number =row[2]
            tenant.email =row[3]
            tenant.property_id =[4]
        else: 
            tenant = cls(row[1],row[2],row[3],row[4],row[0])
            cls.all[tenant.id] = tenant
            
            return tenant
        
    @classmethod
    def get_all(cls):
        sql= """
        SELECT * FROM tenants
        """
        rows = cursor.execute(sql).fetchall
        return [cls.instance_from_db(row) for row in rows]
    
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT * FROM  tenants
        where id = ?
        """
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
Tenant.create_table()
   