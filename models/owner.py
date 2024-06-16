



import sqlite3

# Create a SQLite database
conn = sqlite3.connect('management.db')
cursor = conn.cursor()
def create_tables_if_not_exist():
    # Connect to the SQLite database
    conn = sqlite3.connect('management.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='owners';")
    owners_table_exists = cursor.fetchone() is not None


    if not owners_table_exists:
                cursor.execute('''CREATE TABLE owners (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    phone_number TEXT,
                                );''')
                conn.commit()
                conn.close()
                
class Owner:
    def __init__(self, name, phone_number=None):
        self.name = name
        self.phone_number = phone_number
    

    @staticmethod
    def create(name, phone_number=None):
        cursor.execute(
            'INSERT INTO owners (name, phone_number) VALUES (?, ?)',
            (name, phone_number)
        )
        conn.commit()

    @staticmethod
    def update(owner_id, name, phone_number=None):
        cursor.execute(
            'UPDATE owners SET name=?, phone_number=?, WHERE id=?',
            (name, phone_number, owner_id)
        )
        conn.commit()

    @staticmethod
    def delete(owner_id):
        confirmation = input("Are you sure you want to delete this owner? (y/n): ")
        if confirmation.lower() == 'y':
            cursor.execute('DELETE FROM owners WHERE id=?', (owner_id,))
            conn.commit()
            print(f"Owner with ID {owner_id} deleted successfully.")

    @staticmethod
    def get_all():
        cursor.execute('SELECT * FROM owners')
        return cursor.fetchall()

    @staticmethod
    def find_by_id(owner_id):
        cursor.execute('SELECT * FROM owners WHERE id=?', (owner_id,))
        return cursor.fetchone()
  
                
                
                
                
                



















