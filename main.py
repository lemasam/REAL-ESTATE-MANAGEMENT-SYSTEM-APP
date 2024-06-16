from rich.console  import Console
from rich.theme import Theme
from rich import print

console = Console()
custom_theme = Theme({"success":"green", "error":"bold red"})
console = Console(theme=custom_theme)
from models.owner import Owner
from models.property import Property
from models.tenant import Tenant
import re 

# Function to validate a name input
def validate_name(name):
    while not re.match(r"^[a-zA-Z ]+$", name.strip()):  # Allows alphabets and spaces only
        print("Invalid name format. Please enter a valid name (alphabets and spaces only).")
        name = input("Enter name again: ")
    return name.strip()

# Function to validate a phone number input
def validate_phone_number(phone_number):
    while not re.match(r"^\d{10,}$", phone_number.strip()): # Requires 10 digits or more for phone number
        print("Invalid phone number format. Please enter a valid 10-digit phone number.")
        phone_number = input("Enter phone number again: ")
    return phone_number.strip()

def main():
    while True:
        console.print("\n Welcome To Real Estate Management SYSTEM", style="bold underline red on white")


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
            name = validate_name(input("Enter owner's name: "))
            phone_number = validate_phone_number(input("Enter owner's phone number: "))
            Owner.create(name, phone_number)
            console.print(f"Owner '{name}' added successfully.", style="success")
          
        elif choice == "2":
                try:
                    owner_id = int (input("Enter owner Id to update:"))  
                except ValueError:
                        console.print("Invalid input. Please enter valid integer for owner Id.",style="error")
                        continue
                owner = Owner.find_by_id(owner_id)
                if owner:
                 while True:
                    name_input = input(f"Enter new name for owner ({owner[1]}), or press Enter to leave unchanged: ")
                    if name_input.strip():  
                        name = validate_name(name_input)
                        break
                    else:
                        name = owner[1]
                        break
                    
                 while True:
                    phone_input = input(f"Enter new phone number for owner ({owner[2]}), or press Enter to leave unchanged: ")
                    if phone_input.strip():  # Check if input is not empty
                        phone_number = validate_phone_number(phone_input)
                        break
                    else:
                        phone_number = owner[2]
                        break                
                    
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
                
 #property method:  
                
        elif choice == '6':
            try:
                address = input("Enter property address: ")
                owner_id = int(input("Enter owner ID for this property: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for owner ID.")
                continue  # Restart the loop to prompt the user again

            
            Property.create(address, owner_id)
            console.print(f"Property '{address}' added successfully with Owner ID {owner_id}.", style="error")
                
                
        elif choice == '7':
            try:
                property_id = int(input("Enter property Id to update: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for property Id.")
                continue  # Restart the loop to prompt the user again

            property = Property.find_by_id(property_id)
            if property:
                address = input(f"Enter new address for property ({property[1]}): ")
                Property.update(property_id, address)
                print(f"Property ID {property_id} updated successfully.")
            else:
                print("Property not found.")
                
        elif choice == '8':
            try:
                property_id = int(input("Enter property Id to delete: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for property Id.")
                continue  # Restart the loop to prompt the user again

            property = Property.find_by_id(property_id)
            if property:
                Property.delete(property_id)                
            else:
                print("Property not found.")

        elif choice == '9':
            properties = Property.get_all()
            if properties:
                print("Properties:")
                print("-" * 20)
                for property in properties:
                    print(f"ID: {property[0]}")
                    print(f"Address: {property[1]}")
                    print(f"Owner ID: {property[2]}")
                    print("-" * 20)  # Separate each property details
            else:
                print("No properties found.")
                
        elif choice == '10':
            try:
                property_id = int(input("Enter property ID to find: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for property ID.")
                continue  # Restart the loop to prompt the user again

            property = Property.find_by_id(property_id)
            if property:
                print(f"Property ID: {property[0]}, Address: {property[1]}, Owner ID: {property[2]}")
            else:
                print("Property not found.")
                
# tenant
        elif choice == '11':
            name = validate_name(input("Enter tenant's name: "))
            phone_number = validate_phone_number(input("Enter tenant's phone number: "))
            email = input("Enter tenant's email: ")
            property_id = input("Enter property ID for this tenant: ")
            Tenant.create(name, phone_number, email, property_id)
            print(f"Tenant '{name}' added successfully to Property ID {property_id}.")
            
        elif choice == '12':
            try:
                tenant_id = int(input("Enter tenant Id to update: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for tenant ID.")
                continue
            
            tenant = Tenant.find_by_id  (tenant_id)  
            if tenant:             
                while True:
                    name_input = input(f"Enter new name for tenant ({tenant[1]}), or press Enter to leave unchanged: ")
                    if name_input.strip():  
                        name = validate_name(name_input)
                        break
                    else:
                        name = tenant[1]
                        break

               
                while True:
                    phone_input = input(f"Enter new phone number for tenant ({tenant[2]}), or press Enter to leave unchanged: ")
                    if phone_input.strip(): 
                        phone_number = validate_phone_number(phone_input)
                        break
                    else:
                        phone_number = tenant[2]
                        break
                email = input(f"Enter new email for tenant ({tenant[3]}), or press Enter to leave unchanged: ")
        
                Tenant.update(tenant_id, name, phone_number, email)
                print(f"Tenant Id {tenant_id} updated successfully.")
            else:
                print("Tenant not found.")
            
        elif choice == '13':
            try:
                tenant_id = int(input("Enter tenant ID to delete: "))             
            except ValueError:
                        print("Invalid input. Please enter a valid integer for tenant ID.")
                        continue 

            tenant = Tenant.find_by_id(tenant_id)
            if tenant:
                    Tenant.delete(tenant_id)                
            else:
                    print("Tenant not found.")  
        elif choice =='14':
            tenants = Tenant.get_all()
            if tenants:
                print("Tenants:")
                print("-" * 20)
                for tenant in tenants:
                    print(f"ID: {tenant[0]}")
                    print(f"Name: {tenant[1]}")
                    print(f"Phone Number:{tenant[2]}")
                    print(f"Email:{tenant[2]}")
                    print(f"Properties ID: {tenant[3]}")
                    print("-" * 20)  # Separate each tenants details
            else:
                print("No tenants found.")
        elif choice == '15':
            try:
                tenant_id = int(input("Enter tenant Id to find: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer for tenant ID.")
                continue  # Restart the loop to prompt the user again

            tenant = Tenant.find_by_id(tenant_id)
            if tenant:
                print(f"Tenant ID: {tenant[0]}, Name:{tenant[1]} Phone number: {tenant[2]}, Email: {tenant[3]}, Project ID: {tenant[4]}")
            else:
                print("Tenant not found.")
                         
        elif choice == '16':
            console.print(":thumbs_up: Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            
        
if __name__  == "__main__":
    main()
 
                
        
        
        
            
