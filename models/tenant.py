

from models.owner import Owner
from models.property import Property

import sqlite3

    
conn = sqlite3.connect('management.db')
cursor = conn.cursor()


def create_tables_if_not_exist():
    conn = sqlite3.connect('management.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tenants';")
    tenants_table_exists = cursor.fetchone() is not None
        
    if not tenants_table_exists:
        cursor.execute('''CREATE TABLE tenants (
                             id INTEGER PRIMARY KEY,
                #            name TEXT,
                #            phone_number INTEGER,
                #            email TEXT,
                #             property_id INTEGER NOT NULL REFERENCES owner(id))
                        );''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

class Tenant:
    
    def __init__(self,name,phone_number=None, email=None,property_id=None, id= None):
        self.id = id 
        self.name = name
        self.phone_number= phone_number
        self.email = email
        self.property_id = property_id
     
    @staticmethod   
    def create(name,phone_number=None, email=None,property_id=None):
        cursor.execute(
        'INSERT INTO tenants (name, phone_number, email, property_id) VALUES (?, ?, ?, ?)',
            (name, phone_number, email, property_id)
        )
        conn.commit()
    @staticmethod
    def update(tenant_id, name, phone_number=None, email=None):
        cursor.execute(
            'UPDATE tenants SET name=?, phone_number=?, email=? WHERE id=?',
            (name, phone_number, email, tenant_id)
        )
        conn.commit()
        
    @staticmethod
    def delete(tenant_id):
        confirmation = input("Are you sure you want to delete this tenant? (y/n): ")
        if confirmation.lower() == 'y':
            cursor.execute('DELETE FROM tenants WHERE id=?', (tenant_id,))
            conn.commit()
            print(f"Tenant ID {tenant_id} deleted successfully.")
            
    @staticmethod
    def get_all():
        cursor.execute('SELECT * FROM tenants')
        return cursor.fetchall()

    @staticmethod
    def find_by_id(tenant_id):
        cursor.execute('SELECT * FROM tenants WHERE id=?', (tenant_id,))
        return cursor.fetchone()
    
    @staticmethod
    def get_tenants_by_property(property_id):
        cursor.execute('SELECT * FROM tenants WHERE property_id=?', (property_id,))
        return cursor.fetchall()
            
            