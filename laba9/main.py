import tkinter as tk
import os

def create_directory():
    directory_name = directory_name_entry.get()
    if directory_name:
        os.mkdir(directory_name)
        refresh_listbox()

def create_text_file():
    file_name = text_file_name_entry.get()
    if file_name:
        with open(file_name, 'w') as file:
            pass
        refresh_listbox()

def delete_selected():
    selected_item = file_listbox.get(tk.ACTIVE)
    if selected_item:
        if os.path.isfile(selected_item):
            os.remove(selected_item)
        elif os.path.isdir(selected_item):
            os.rmdir(selected_item)
        refresh_listbox()

def rename_selected():
    selected_item = file_listbox.get(tk.ACTIVE)
    new_name = rename_entry.get()
    if selected_item and new_name:
        os.rename(selected_item, new_name)
        refresh_listbox()

def refresh_listbox():
    file_listbox.delete(0, tk.END)
    current_directory = os.getcwd()
    for item in os.listdir(current_directory):
        file_listbox.insert(tk.END, item)

root = tk.Tk()
root.title("File Manager")

directory_name_label = tk.Label(root, text="New directory:")
directory_name_entry = tk.Entry(root)
create_directory_button = tk.Button(root, text="Create a directory", command=create_directory)

text_file_name_label = tk.Label(root, text="New file:")
text_file_name_entry = tk.Entry(root)
create_text_file_button = tk.Button(root, text="Create a file", command=create_text_file)

file_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
file_listbox.pack()

delete_button = tk.Button(root, text="Delete selected", command=delete_selected)

rename_label = tk.Label(root, text="Rename to:")
rename_entry = tk.Entry(root)
rename_button = tk.Button(root, text="Rename the selected", command=rename_selected)

directory_name_label.pack()
directory_name_entry.pack()
create_directory_button.pack()

text_file_name_label.pack()
text_file_name_entry.pack()
create_text_file_button.pack()

file_listbox.pack()
delete_button.pack()

rename_label.pack()
rename_entry.pack()
rename_button.pack()

refresh_listbox()

root.mainloop()
