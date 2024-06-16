

from models.owner import Owner  
        
import sqlite3

# Create a SQLite database
conn = sqlite3.connect('management.db')
cursor = conn.cursor()
def create_tables_if_not_exist():
    # Connect to the SQLite database
    conn = sqlite3.connect('management.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='properties';")
    properties_table_exists = cursor.fetchone() is not None

    if not properties_table_exists:
        cursor.execute('''CREATE TABLE properties (
                            id INTEGER PRIMARY KEY,
                            address TEXT NOT NULL,
                            owner_id INTEGER,
                            FOREIGN KEY (owner_id) REFERENCES owners (id)
                        );''')
    conn.commit()
    conn.close()
    
class Property:
    def __init__(self, address, owner_id=None):
        self.address = address
        self.owner_id = owner_id

    @staticmethod
    def create(address, owner_id=None):
        cursor.execute('INSERT INTO properties (address, owner_id) VALUES (?, ?)', (address, owner_id))
        conn.commit()

    @staticmethod
    def update(property_id, address):
        cursor.execute('UPDATE properties SET address=? WHERE id=?', (address, property_id))
        conn.commit()

    @staticmethod
    def delete(property_id):
        confirmation = input("Are you sure you want to delete this property? (y/n): ")
        if confirmation.lower() == 'y':
            cursor.execute('DELETE FROM properties WHERE id=?', (property_id,))
            conn.commit()
            print(f"Property with ID {property_id} deleted successfully.")

    @staticmethod
    def get_all():
        cursor.execute('SELECT * FROM properties')
        return cursor.fetchall()

    @staticmethod
    def find_by_id(property_id):
        cursor.execute('SELECT * FROM properties WHERE id=?', (property_id,))
        return cursor.fetchone()
    
    @staticmethod
    def get_properties_by_owner(owner_id):
        cursor.execute('SELECT * FROM properties WHERE owner_id=?', (owner_id,))
        return cursor.fetchall()
        