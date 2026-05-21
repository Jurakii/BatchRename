import customtkinter as ctk
from customtkinter import filedialog
import os
import sys

version = "v1.0"

def rename():
    if not path.get():
        status.configure(text="File path field is empty", text_color="red")
        return
    elif not replace.get():
        status.configure(text="Replace field is empty", text_color="red")
        return
    dir_list = os.listdir(path.get())
    original = replace.get()
    count = 0
    for i in dir_list:
        count += 1
        if original in i:
            count -= 1
            startPath = path.get()+"/"+i
            renamed = i.replace(original, newname.get())
            endPath = path.get()+"/"+ renamed
            os.rename(startPath, endPath)
            status.configure(text="Files Renamed", text_color="green")
        elif count == len(dir_list):
            print(original + " not found")
            status.configure(text="No file containing " + original + " found", text_color="red")
    
def browse():
    selected_dir = filedialog.askdirectory(
        initialdir="/",
        title="Select a Directory",
    )
    if selected_dir:
        path.delete(0, "end")
        path.insert(0, selected_dir)

app = ctk.CTk()
app.title("Batch Rename")
app.resizable(False, False) 
app.geometry("500x205")
app.grid_columnconfigure(0, weight=1)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app.iconbitmap(resource_path("icon.ico"))

#title = ctk.CTkLabel(app,text="Batch Renamer",)
#title.grid(row=0,column=0, padx=20, pady=10,sticky="ew")

# Path Field
path = ctk.CTkEntry(app, placeholder_text="File Path")
path.grid(row=1, column=0, padx=(20,5), pady=10, sticky="ew")
browseBtn = ctk.CTkButton(app, text="Browse", command=browse)
browseBtn.grid(row=1, column=1, padx=(5,20), pady=10, sticky="ew")

# Replace Field
replace = ctk.CTkEntry(app, placeholder_text="Replace")
replace.grid(row=2, column=0, columnspan=2, padx = 20, pady=10, sticky="ew")

# Name Field
newname = ctk.CTkEntry(app, placeholder_text="Name")
newname.grid(row=3, column=0, columnspan=2, padx = 20, pady=10, sticky="ew")

# Confirm Button
confirm = ctk.CTkButton(app, text="Rename", command=rename)
confirm.grid(row=4, column=0, padx=(20,5), pady=(10,0), sticky="ew")

# Status Label
status = ctk.CTkLabel(app, text="")
status.grid(row=4, column=1, padx=(5,20), pady=(10,0))

# Version Label
ver = ctk.CTkLabel(app, text=version)
ver.grid(row=5, column=1, sticky="se", padx=(0,5), pady=(0,0))

app.mainloop()