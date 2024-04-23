import tkinter as tk

def add_task():
    """Function to add a task to the list"""
    task = task_entry.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    """Function to delete a selected task from the list"""
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        pass


root = tk.Tk()
root.title("To-Do List")


task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", width=48, command=add_task)
add_button.pack()

# Tasks List
listbox_tasks = tk.Listbox(root, height=15, width=50)
listbox_tasks.pack()

# Delete Button
delete_button = tk.Button(root, text="Delete Task", width=48, command=delete_task)
delete_button.pack(pady=10)

root.mainloop()