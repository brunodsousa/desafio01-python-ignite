def view_contacts(contact_list):
    if len(contact_list) == 0:
        print("The contacts list is empty")
    for index, contact in enumerate(contact_list, start=1):
        favorite = "⭐" if contact["favorite"] else ""
        name = contact["name"]
        phone = contact["phone"]
        email = contact["email"]
        print(f"{index}. {favorite} {name} - Phone: {phone} - Email: {email}")
    return


def add_contact(contact_list, new_contact):
    contact_list.append(new_contact)
    print("New contact added successfully!")
    return


def edit_contact(contact_list, contact_index):
    adjusted_contact_index = int(contact_index) - 1
    contact = contact_list[adjusted_contact_index]
    while True:
        print(f"1. Name: {contact['name']}")
        print(f"2. Phone: {contact['phone']}")
        print(f"3. Email: {contact['email']}")
        print("4. Finish editing")
        field_choice = input("Choose the field you want to edit: ")

        if field_choice == "1":
            updated_name = input("Enter the new name: ")
            contact["name"] = updated_name
        elif field_choice == "2":
            updated_phone = input("Enter the new phone: ")
            contact["phone"] = updated_phone
        elif field_choice == "3":
            updated_email = input("Enter the new email: ")
            contact["email"] = updated_email
        elif field_choice == "4":
            break
        else:
            print("\033[31mInvalid option. Try again\033[0m")
    print("Editing done successfully")


def favorite_contact(contact_list, contact_index):
    adjusted_contact_index = int(contact_index) - 1
    contact_list[adjusted_contact_index]["favorite"] = True
    contact_name = contact_list[adjusted_contact_index]["name"]
    print(f"The contact {contact_name} has been added to your favorites")
    return


def unfavorite_contact(contact_list, contact_index):
    adjusted_contact_index = int(contact_index) - 1
    contact_list[adjusted_contact_index]["favorite"] = False
    contact_name = contact_list[adjusted_contact_index]["name"]
    print(f"{contact_name} has been removed from your favorites")
    return


def view_favorite_contacts(contact_list):
    for index, contact in enumerate(contact_list, start=1):
        if contact["favorite"]:
            name = contact["name"]
            phone = contact["phone"]
            email = contact["email"]
            print(f"{index}. ⭐ {name} - Phone: {phone} - Email: {email}")
    return


def remove_contact(contact_list, contact_index):
    adjusted_contact_index = int(contact_index) - 1
    contact = contact_list[adjusted_contact_index]
    print("Contact removed successfully")
    contact_list.remove(contact)
    return
