import sqlite3 #Import the sqlite3 module to work with SQLite databases.

conn =  sqlite3.connect("management.sqlite")  # Establish a connection to a database named management.sqlite

cursor = conn.cursor() #Create a cursor object to execute SQL commands.



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
        
 



