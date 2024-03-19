from modules import (
    add_contact,
    edit_contact,
    favorite_contact,
    remove_contact,
    unfavorite_contact,
    view_contacts,
    view_favorite_contacts,
)

contacts = []

while True:
    print("\nContacts List Menu:")
    print("1. Add a new contact")
    print("2. Edit existing contact")
    print("3. Add a contact to favorites")
    print("4. Remove a contact from favorites")
    print("5. View favorite contacts")
    print("6. Remove a contact")
    print("7. View all contacts")
    print("8. Exit")

    selected_option = int(input("Choose the desired option: "))

    if selected_option == 1:
        print("Enter the necessary data to create a new contact:")
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        new_contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": False,
        }
        add_contact(contacts, new_contact)
    elif selected_option == 2:
        view_contacts(contacts)
        contact_index = input("Enter the number of the contact you want to edit: ")
        edit_contact(contacts, contact_index)
    elif selected_option == 3:
        view_contacts(contacts)
        contact_index = input("Enter the number of the contact you want to favorite: ")
        favorite_contact(contacts, contact_index)
    elif selected_option == 4:
        view_contacts(contacts)
        contact_index = input(
            "Enter the number of the contact you want to unfavorite: "
        )
        unfavorite_contact(contacts, contact_index)
    elif selected_option == 5:
        view_favorite_contacts(contacts)
    elif selected_option == 6:
        view_contacts(contacts)
        contact_index = input("Enter the number of the contact you want to remove: ")
        remove_contact(contacts, contact_index)
    elif selected_option == 7:
        view_contacts(contacts)
    elif selected_option == 8:
        break
    else:
        print("\033[31mInvalid option. Try again\033[0m")
