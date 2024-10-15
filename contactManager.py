contacts = []
haghighi_id_counter = 1000
hoghoghi_id_counter = 5000

class Contact:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class Haghighi(Contact):
    def __init__(self, name, family, phone, relationship):
        super().__init__(name)
        global haghighi_id_counter
        self.id = haghighi_id_counter
        haghighi_id_counter += 1
        self._family = family
        self.phone = phone
        self._relationship = relationship

    def __str__(self):
        return f"ID: {self.id}, Name: {self._name}, Family: {self._family}, Phone: {self.phone}, Relationship: {self._relationship}"

class Hoghoghi(Contact):
    def __init__(self, name, city_code, phone, address, email, fox):
        super().__init__(name)
        global hoghoghi_id_counter
        self.id = hoghoghi_id_counter
        hoghoghi_id_counter += 1
        self.city_code = city_code
        self.phone = phone
        self.address = address
        self.email = email
        self.fox = fox

    def __str__(self):
        return f"ID: {self.id}, Name: {self._name}, City Code: {self.city_code}, Phone: {self.phone}, Address: {self.address}, Email: {self.email}, Fox: {self.fox}"

def validate_phone(city_code, phone, is_haghighi=True):
    if is_haghighi:
        return len(phone) == 11 and phone.startswith('09') and phone.isdigit()
    else:
        return len(city_code) == 3 and city_code.isdigit() and len(phone) == 8 and phone.isdigit()

def validate_email(email):
    if email.count('@') != 1:
        return False
    if email.startswith('@') or email.endswith('@'):
        return False
    local_part, domain_part = email.split('@')
    if '.' not in domain_part:
        return False
    if domain_part.startswith('.') or domain_part.endswith('.'):
        return False
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_ ")
    if not set(email).issubset(allowed_chars.union({'@'})):
        return False
    return True

def validate_fox(fox):
    if len(fox) != 12 or not fox.isdigit():
        return False
    return True

def select_relationship():
    print("Select relationship:")
    print("1. Mother")
    print("2. Father")
    print("3. Brother")
    print("4. Sister")
    print("5. Friend")
    print("6. Best Friend")
    print("7. Other (custom input)")
    
    relationships = {
        '1': 'Mother',
        '2': 'Father',
        '3': 'Brother',
        '4': 'Sister',
        '5': 'Friend',
        '6': 'Best Friend'
    }
    
    while True:
        choice = input("Enter your choice (1-7): ")
        if choice in relationships: 
            return relationships[choice]
        elif choice == '7':
            custom_relationship = input("Enter custom relationship: ")
            return custom_relationship
        else:
            print("Invalid choice. Please try again.")

def check_duplicate_phone(phone):
    for contact in contacts:
        if hasattr(contact, 'phone') and contact.phone == phone:
            return contact
    return None

def check_duplicate_email(email):
    for contact in contacts:
        if isinstance(contact, Hoghoghi) and contact.email == email:
            return contact
    return None

def insert_haghighi():
    name = input("Enter name: ")
    family = input("Enter family: ")
    phone = input("Enter phone (format: 09XXXXXXXXX): ")
    if not validate_phone(None, phone, is_haghighi=True):
        print("Invalid phone format.")
        return
    
    duplicate = check_duplicate_phone(phone)
    if duplicate:
        print(f"This phone number is already registered to contact with ID: {duplicate.id}")
        return
    
    relationship = select_relationship()
    contacts.append(Haghighi(name, family, phone, relationship))
    print("Haghighi contact added successfully.")

def insert_hoghoghi():
    name = input("Enter name: ")
    city_code = input("Enter city code (3 digits): ")
    phone = input("Enter phone (8 digits): ")
    if not validate_phone(city_code, phone, is_haghighi=False):
        print("Invalid phone format.")
        return
    
    full_phone = city_code + phone
    duplicate = check_duplicate_phone(full_phone)
    if duplicate:
        print(f"This phone number is already registered to contact with ID: {duplicate.id}")
        return
    
    address = input("Enter address: ")
    email = input("Enter email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return
    
    duplicate = check_duplicate_email(email)
    if duplicate:
        print(f"This email is already registered to contact with ID: {duplicate.id}")
        return
    
    fox = input("Enter fox (12 digits): ")
    if not validate_fox(fox):
        print("Invalid fox format.")
        return
    contacts.append(Hoghoghi(name, city_code, phone, address, email, fox))
    print("Hoghoghi contact added successfully.")

def insert_menu():
    print("1. Insert Haghighi")
    print("2. Insert Hoghoghi")
    choice = input("Enter your choice: ")
    if choice == '1':
        insert_haghighi()
    elif choice == '2':
        insert_hoghoghi()
    else:
        print("Invalid choice. Please try again.")

def search_by_name():
    name = input("Enter name to search: ")
    results = [contact for contact in contacts if contact.name.lower() == name.lower()]
    if results:
        for contact in results:
            print(contact)
    else:
        print("No contacts found.")

def search_by_id():
    id_to_search = input("Enter ID to search: ")
    result = next((contact for contact in contacts if str(contact.id) == id_to_search), None)
    if result:
        print(result)
    else:
        print("No contact found.")

def search_menu():
    print("1. Search by Name")
    print("2. Search by ID")
    choice = input("Enter your choice: ")
    if choice == '1':
        search_by_name()
    elif choice == '2':
        search_by_id()
    else:
        print("Invalid choice. Please try again.")

def show_all_contacts_menu():
    print("1. Show all contacts")
    print("2. Show Haghighi contacts")
    print("3. Show Hoghoghi contacts")
    choice = input("Enter your choice: ")
    if choice == '1':
        show_all_contacts()
    elif choice == '2':
        show_haghighi_contacts()
    elif choice == '3':
        show_hoghoghi_contacts()
    else:
        print("Invalid choice. Please try again.")

def show_all_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(contact)

def show_haghighi_contacts():
    haghighi_contacts = [contact for contact in contacts if isinstance(contact, Haghighi)]
    if not haghighi_contacts:
        print("No Haghighi contacts found.")
    else:
        for contact in haghighi_contacts:
            print(contact)

def show_hoghoghi_contacts():
    hoghoghi_contacts = [contact for contact in contacts if isinstance(contact, Hoghoghi)]
    if not hoghoghi_contacts:
        print("No Hoghoghi contacts found.")
    else:
        for contact in hoghoghi_contacts:
            print(contact)

def delete_contact_menu():
    print("1. Delete by name")
    print("2. Delete by ID")
    choice = input("Enter your choice: ")
    if choice == '1':
        delete_contact_by_name()
    elif choice == '2':
        delete_contact_by_id()
    else:
        print("Invalid choice. Please try again.")

def delete_contact_by_name():
    name = input("Enter the name of the contact to delete: ")
    found_contacts = [contact for contact in contacts if contact.name.lower() == name.lower()]
    if not found_contacts:
        print("No contacts found with that name.")
        return
    
    for contact in found_contacts:
        print(contact)
        confirm = input(f"Are you sure you want to delete this contact? (yes/no): ")
        if confirm.lower() == 'yes':
            contacts.remove(contact)
            print("Contact deleted successfully.")
        else:
            print("Deletion cancelled.")

def delete_contact_by_id():
    id_to_delete = input("Enter the ID of the contact to delete: ")
    found_contact = next((contact for contact in contacts if str(contact.id) == id_to_delete), None)
    if not found_contact:
        print("No contact found with that ID.")
        return
    
    print(found_contact)
    confirm = input(f"Are you sure you want to delete this contact? (yes/no): ")
    if confirm.lower() == 'yes':
        contacts.remove(found_contact)
        print("Contact deleted successfully.")
    else:
        print("Deletion cancelled.")

def edit_contact_menu():
    print("1. Edit by name")
    print("2. Edit by ID")
    choice = input("Enter your choice: ")
    if choice == '1':
        edit_contact_by_name()
    elif choice == '2':
        edit_contact_by_id()
    else:
        print("Invalid choice. Please try again.")

def edit_contact_by_name():
    name = input("Enter the name of the contact to edit: ")
    found_contacts = [contact for contact in contacts if contact.name.lower() == name.lower()]
    if not found_contacts:
        print("No contacts found with that name.")
        return
    
    for contact in found_contacts:
        print(contact)
        confirm = input(f"Do you want to edit this contact? (yes/no): ")
        if confirm.lower() == 'yes':
            edit_contact(contact)
        else:
            print("Edit cancelled.")

def edit_contact_by_id():
    id_to_edit = input("Enter the ID of the contact to edit: ")
    found_contact = next((contact for contact in contacts if str(contact.id) == id_to_edit), None)
    if not found_contact:
        print("No contact found with that ID.")
        return
    
    print(found_contact)
    confirm = input(f"Do you want to edit this contact? (yes/no): ")
    if confirm.lower() == 'yes':
        edit_contact(found_contact)
    else:
        print("Edit cancelled.")

def edit_contact(contact):
    if isinstance(contact, Haghighi):
        edit_haghighi(contact)
    elif isinstance(contact, Hoghoghi):
        edit_hoghoghi(contact)

def edit_haghighi(contact):
    print("Leave blank if you don't want to change a field.")
    new_name = input(f"Enter new name (current: {contact.name}): ")
    new_family = input(f"Enter new family (current: {contact._family}): ")
    new_phone = input(f"Enter new phone (current: {contact.phone}): ")
    new_relationship = select_relationship() if input(f"Do you want to change the relationship (current: {contact._relationship})? (yes/no): ").lower() == 'yes' else ''

    if new_name:
        contact._name = new_name
    if new_family:
        contact._family = new_family
    if new_phone:
        if validate_phone(None, new_phone, is_haghighi=True):
            duplicate = check_duplicate_phone(new_phone)
            if duplicate and duplicate.id != contact.id:
                print(f"This phone number is already registered to contact with ID: {duplicate.id}")
                print("Phone not updated.")
            else:
                contact.phone = new_phone
        else:
            print("Invalid phone format. Phone not updated.")
    if new_relationship:
        contact._relationship = new_relationship

    print("Contact updated successfully.")

def edit_hoghoghi(contact):
    print("Leave blank if you don't want to change a field.")
    new_name = input(f"Enter new name (current: {contact.name}): ")
    new_city_code = input(f"Enter new city code (current: {contact.city_code}): ")
    new_phone = input(f"Enter new phone (current: {contact.phone}): ")
    new_address = input(f"Enter new address (current: {contact.address}): ")
    new_email = input(f"Enter new email (current: {contact.email}): ")
    new_fox = input(f"Enter new fox (current: {contact.fox}): ")

    if new_name:
        contact._name = new_name
    if new_city_code and new_phone:
        if validate_phone(new_city_code, new_phone, is_haghighi=False):
            full_phone = new_city_code + new_phone
            duplicate = check_duplicate_phone(full_phone)
            if duplicate and duplicate.id != contact.id:
                print(f"This phone number is already registered to contact with ID: {duplicate.id}")
                print("Phone and city code not updated.")
            else:
                contact.city_code = new_city_code
                contact.phone = new_phone
        else:
            print("Invalid phone format. Phone and city code not updated.")
    if new_address:
        contact.address = new_address
    if new_email:
        if validate_email(new_email):
            duplicate = check_duplicate_email(new_email)
            if duplicate and duplicate.id != contact.id:
                print(f"This email is already registered to contact with ID: {duplicate.id}")
                print("Email not updated.")
            else:
                contact.email = new_email
        else:
            print("Invalid email format. Email not updated.")
    if new_fox:
        if validate_fox(new_fox):
            contact.fox = new_fox
        else:
            print("Invalid fox format. Fox not updated.")

    print("Contact updated successfully.")

def save_contacts_to_file():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            if isinstance(contact, Haghighi):
                file.write(f"Haghighi,{contact.id},{contact.name},{contact._family},{contact.phone},{contact._relationship}\n")
            elif isinstance(contact, Hoghoghi):
                file.write(f"Hoghoghi,{contact.id},{contact.name},{contact.city_code},{contact.phone},{contact.address},{contact.email},{contact.fox}\n")
    print("Contacts saved to file successfully.")

def load_contacts_from_file():
    global haghighi_id_counter, hoghoghi_id_counter
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == "Haghighi":
                    contact = Haghighi(data[2], data[3], data[4], data[5])
                    contact.id = int(data[1])
                    contacts.append(contact)
                    haghighi_id_counter = max(haghighi_id_counter, contact.id + 1)
                elif data[0] == "Hoghoghi":
                    contact = Hoghoghi(data[2], data[3], data[4], data[5], data[6], data[7])
                    contact.id = int(data[1])
                    contacts.append(contact)
                    hoghoghi_id_counter = max(hoghoghi_id_counter, contact.id + 1)
        print("Contacts loaded from file successfully.")
    except FileNotFoundError:
        print("No existing contacts file found. Starting with an empty contact list.")

def save_data_prompt():
    choice = input("Do you want to save the data? (yes/no): ")
    if choice.lower() == 'yes':
        save_contacts_to_file()
    else:
        print("Data not saved.")

def main_menu():
    load_contacts_from_file()
    while True:
        print("\nMain Menu:")
        print("1. Insert Contact")
        print("2. Search Contact")
        print("3. Show All Contacts")
        print("4. Delete Contact")
        print("5. Edit Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            insert_menu()
        elif choice == '2':
            search_menu()
        elif choice == '3':
            show_all_contacts_menu()
        elif choice == '4':
            delete_contact_menu()
        elif choice == '5':
            edit_contact_menu()
        elif choice == '6':
            save_data_prompt()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
