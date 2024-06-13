import sqlite3 #Import the sqlite3 module to work with SQLite databases.
from __init__ import cursor, conn

def get_db_connection():
    return sqlite3.connect("management.db")



#  creating owners class
class Owner:
    def __init__(self, name, phone_number, id= None):
        self.id = id 
        self.name = name
        self.phone_number = phone_number
        
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
            
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE  IF NOT EXISTS owners(
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone_number INTEGER
        )
        """
        
    @classmethod
    def drop_table(cls):
        sql ="""
        DROP TABLE IF EXISTS;
        """   
        
        cursor.execute(sql)
        conn.commit()
        
    def save(self):
        sql ="""
        INSERT INTO owners(self.name,self.phone_number)
        VALUES (?, ?)
        """
        cursor.execute(sql,(self.name, self.phone_number))
        conn.commit ()
        self.id =cursor.lastrowid 
        
    
    @classmethod
    def create(cls,name,phone_number):
        owner = cls(name, phone_number)
        owner.save()
        return owner 
    
    def update(self):
        sql = """
        UPDATE owners
        SET name = ?, phone_number = ?
        WHERE id =?
        """
        
        cursor.execute(sql, (self.name, self.phone_number,self.id))
        conn.commit()
        
    def delete(owner_id):
        confirmation = input("Are you sure you want to delete this property? (y/n): ")
        if confirmation.lower() == 'y':        
            cursor.execute('DELETE FROM owners WHERE id=?', (owner_id,))
            conn.commit()
            print(f"Owner with ID {owner_id} deleted successfully")
            
        
    @classmethod
    def instance_from_db(cls, row):
           
        owner = cls.all.get(row[0])
        if owner:
            owner.name = row[1]
            owner.phone_number= row[2]
        else:
            owner = cls(row[1], row[2])
            owner.id = row[0]
            cls.all[owner.id] = owner
        return owner
    
    @classmethod
    def get_all(cls):
        sql= """
        SELECT * FROM owners
        """
        rows = cursor.execute(sql).fetchall
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT * FROM  owners
        where id = ?
        """
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None



