from db import cursor, conn

from models.owner import Owner

class Property:
    
    def __init__(self,address,owner_id, id= None):
        self.id = id 
        self.adress = address
        self.owner_id = owner_id
        
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self,address):
        if isinstance(address,str) and len(address):
            self._address = address
            
        else: 
            raise ValueError(
                "Address must be a non-empty string"
            )
            
    @property
    def owner_id(self):
        return self._owner_id 
    
    @owner_id.setter
    def owner_id(self, owner_id):
        if type(owner_id) is int and Owner.find_by_id(owner_id):
            self._owner_id = owner_id
            
        else:
            raise ValueError(
                " owner_id must reference a owner in the database"
            )
    
    @classmethod
    def create_table(cls):
        sql ="""
        CREATE TABLE IF NOT EXISTS properties(
            id INTEGER PRIMARY KEY,
            address TEXT,
            owner_id INTEGER NOT NULL REFERENCES owner(id))
        """
        cursor.execute(sql)
        conn.commit()
        
    @classmethod
    def drop_table(cls):
        sql ="""
        DROP TABLE IF EXISTS  properties
        """
        cursor.execute(sql)
        conn.commit()
        
    def save (self):
        sql = """
        INSERT INTO properties(address,owner_id)
        VALUES (?, ?, ?)
        """
        
        cursor.execute(sql,(self.address,self.owner_id))
        conn.commit () 
        
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
    
    def update (self):
        sql = """
        UPDATE properties 
        SET adrress= ?, owner_id = ?
        WHERE id = ?
        """
        
        cursor.execute(sql,(self.address,self.owner_id))
        
        conn.commit()
        
    def delete(self):
        sql = """
        DELETE FROM properties
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
        property = cls.all.get(row[0])
        if property:
            property.address = row[1]
        else: 
            property = cls(row[1],)
            property.id = row[0] 
            cls.all[property.id]= property
            
            return property
        
    @classmethod
    def get_all(cls):
        sql= """
        SELECT * FROM properties
        """
        rows = cursor.execute(sql).fetchall
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT * FROM  properties
        where id = ?
        """
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def owners(self):
        from owner import Owner
        sql = """
            SELECT * FROM owner
            WHERE owner_id = ?
        """
        cursor.execute(sql, (self.id,),)

        rows = cursor.fetchall()
        return [
            Owner.instance_from_db(row) for row in rows
        ]
    
        
Property.create_table()