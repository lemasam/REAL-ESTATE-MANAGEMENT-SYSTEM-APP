from models.owner import Owner
from models.property import Property
from models.tenant import Tenant

def main():
    while True:
        print("\n Welcome To Real Estate Management SYSTEM ")

# Owner methods
        print("1. Add Owner")
        print("2. Update Owner")
        print("3. Delete Owner")
        print("4. Display Owners")
        print("5. Find Owner by ID")
        
# Property methods
        print("6. Add Property")
        print("7. Update Property")
        print("8. Delete Property")
        print("9. Display Properties")
        print("10. Find Property by ID")
        
# Tenant methods
        print("11. Add Tenant")
        print("12. Update Tenant")
        print("13. Delete Tenant")
        print("14. Display Tenants")
        print("15. Find Tenant by ID")
        
        print("16. Exit")
        choice = input("Enter your choice: ")
        
# Owner 
 
        if choice == "1":
            name = str(input("Enter Owner's name:"))
            phone_number = int("Enter owner's phone number: ")
            Owner.create(name, phone_number)
            print(f"Owner '{name}' added successfully.")
          
        elif choice =="2":
                try:
                        owner_id = int (input("Enter owner Id to update:"))  
                except ValueError:
                        print("Invalid input. Please enter valid integer for owner Id.")
                        continue
                owner = Owner.find_by_id(owner_id)
                if owner:
                        name= input(f"Enter new name for owner({owner[1]}), or press Enter to leave unchanged")
                        phone_number= input(f"Rnter new phone number for owner({owner[2]}), or press Enter to leave unchanged")
                        Owner.update(owner_id, name, phone_number)
                        print(f"Owner ID {owner_id} updated successfully.")
                else:
                        print("Owner not found.")
                        
        elif choice  == "3":
                try:
                        owner_id = int(input("Enter owner ID to delete: "))
                except ValueError:
                        print("Invalid input. Please enter a valid integer for owner ID.")
                        continue  # Restart the loop to prompt the user again

                owner = Owner.find_by_id(owner_id)
                if owner:
                        Owner.delete(owner_id)                
                else:
                        print("Owner not found.")
                        
        elif choice == '4':
            owners = Owner.get_all()
            if owners:
                print("Owners:")
                print("-" * 20)
                for owner in owners:
                    print(f"ID: {owner[0]}")
                    print(f"Name: {owner[1]}") 
                    print(f"Phone Number: {owner[2]}")
                    print("-" * 20)  # Separate each owner's details
            else:
                print("No owners found.")
                
        elif choice == '5':
            try:
                owner_id = int(input("Enter owner ID to find: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for owner ID.")
                continue  # Restart the loop to prompt the user again

            owner = Owner.find_by_id(owner_id)
            if owner:
                print(f"Owner ID: {owner[0]}, Name: {owner[1]}")
            else:
                print("Owner not found.")    
        
if __name__ == "__main__":
    main()