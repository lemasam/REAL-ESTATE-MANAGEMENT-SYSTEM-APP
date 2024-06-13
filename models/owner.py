import sqlite3 #Import the sqlite3 module to work with SQLite databases.

conn =  sqlite3.connect("management.sqlite")  # Establish a connection to a database named management.sqlite

cursor = conn.cursor() #Create a cursor object to execute SQL commands.



#  creating owners class
class Owner:
    def __init__(self, name, phone_number, id= None):
        self.id = id 
        self.name = name
        self.phone_number = phone_number




