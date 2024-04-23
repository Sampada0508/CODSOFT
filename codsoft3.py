import tkinter as tk

def add_contact():
    """Function to add a contact"""
    name = name_entry.get()
    number = number_entry.get()
    if name and number:
        contacts[name] = number
        update_contact_list()

def delete_contact():
    """Function to delete a contact"""
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        name = contact_listbox.get(selected_contact)
        del contacts[name]
        update_contact_list()

def update_contact_list():
    """Function to update the contact list"""
    contact_listbox.delete(0, tk.END)
    for name, number in contacts.items():
        contact_listbox.insert(tk.END, f"{name}: {number}")

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Contacts Dictionary
contacts = {}

# Name Entry
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Number Entry
number_label = tk.Label(root, text="Number:")
number_label.grid(row=1, column=0)
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1)

# Add Button
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=2, column=0, columnspan=2, pady=5)

# Contact Listbox
contact_listbox = tk.Listbox(root, width=50)
contact_listbox.grid(row=3, column=0, columnspan=2, padx=5)

# Delete Button
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()