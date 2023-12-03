import os
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# Глобальная переменная для хранения текущего пути
current_path = os.getcwd()

def create_new_folder():
    new_folder_name = simpledialog.askstring("Create new folder", "Enter the name of the new folder:")
    if new_folder_name:
        new_folder_path = os.path.join(current_path, new_folder_name)
        try:
            os.makedirs(new_folder_path, exist_ok=True)  # Создаем новую папку
            refresh_file_list()
        except OSError as e:
            messagebox.showerror("Error", str(e))

def delete_file_or_folder():
    selected_item = listbox.get(tk.ANCHOR)
    if selected_item:
        if messagebox.askyesno("Delete", "Are you sure you want to delete this item?"):
            item_path = os.path.join(current_path, selected_item)
            try:
                if os.path.isdir(item_path):
                    os.rmdir(item_path)  # Удаляем папку
                else:
                    os.remove(item_path)  # Удаляем файл
                refresh_file_list()
            except OSError as e:
                messagebox.showerror("Error", str(e))

def rename_file_or_folder():
    selected_item = listbox.get(tk.ANCHOR)
    if selected_item:
        new_name = simpledialog.askstring("Rename", "Enter the new name:")
        if new_name:
            item_path = os.path.join(current_path, selected_item)
            new_item_path = os.path.join(current_path, new_name)
            try:
                os.rename(item_path, new_item_path)  # Переименовываем файл или папку
                refresh_file_list()
            except OSError as e:
                messagebox.showerror("Error", str(e))

def refresh_file_list():
    listbox.delete(0, tk.END)
    for item in os.listdir(current_path):  # Получаем список файлов и папок в текущем каталоге
        listbox.insert(tk.END, item)

def change_directory():
    path = filedialog.askdirectory(initialdir=current_path)
    if path:
        global current_path
        current_path = path
        refresh_file_list()

# Создаем главное окно
root = tk.Tk()
root.title("File Manager")

# Список файлов и папок
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(padx=10, pady=10)

# Кнопки управления
create_button = tk.Button(root, text="Create Folder", command=create_new_folder)
create_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(root, text="Delete", command=delete_file_or_folder)
delete_button.pack(side=tk.LEFT, padx=5)

rename_button = tk.Button(root, text="Rename", command=rename_file_or_folder)
rename_button.pack(side=tk.LEFT, padx=5)

change_dir_button = tk.Button(root, text="Change Directory", command=change_directory)
change_dir_button.pack(side=tk.LEFT, padx=5)

# Загружаем список файлов и папок
refresh_file_list()

# Запускаем главный цикл Tkinter
root.mainloop()
