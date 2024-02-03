from tkinter import *
import tkinter as tk
import customtkinter as ctk

window = tk.Tk()
window.title("App Name")
window.geometry( "800x450" )

label = tk.Label(text="Welcome to MentalMessages!", font=ctk.CTkFont(size=30, weight="bold", underline=True))
label.pack()
subtitle = tk.Label(window, text="Media where health comes first!", font=ctk.CTkFont(size=15, slant = "italic"), fg="white", pady=10)
subtitle.pack()
buffer = tk.Label(window, text="", font=ctk.CTkFont(size=8))
buffer.pack(pady=8)

#button = ctk.CTkButton(window, text="Refresh", font=ctk.CTkFont(size=12))
#button.pack(pady=20)

mediaLabel = tk.Label(text="Select your media and provide your credentials below.", font=ctk.CTkFont(size=14), fg="white")
mediaLabel.pack()
clicked = StringVar()
clicked.set( "Social Media" ) 
mediaTypes= [
    "Instagram", 
    "Discord", 
    "Youtube"
]

cleanOptions = []
prompt = tk.Label(window, text="What would you like to cleanse?", font=ctk.CTkFont(size=12), underline = True)
listbox = tk.Listbox(window, font=ctk.CTkFont(size=10), height = len(cleanOptions), selectmode = "multiple")

def showOptions():
    listbox.delete(0,END)
    type = clicked.get()
    cleanOptions = []
    if type == "Instagram": 
        cleanOptions = ["Instagram Comments", "Instagram Messages"]
    elif type == "Youtube":
        cleanOptions = ["Youtube Comments"]
    elif type == "Discord":
        cleanOptions = ["Discord Messages"]

    prompt.pack()
    for count, option in enumerate(cleanOptions, 1):
        listbox.insert(count, option)
    listbox.pack()

def grabcurrent(event):
    cleanOptions = []
    showOptions()
    pass

drop = tk.OptionMenu( window , clicked, *mediaTypes, command = grabcurrent ) 
drop.pack(pady=10) 


username_label = tk.Label(window, text="Username:", font=ctk.CTkFont(size=12), fg="white")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()
buffer = tk.Label(window, text="", font=ctk.CTkFont(size=1))
buffer.pack()
password_label = tk.Label(window, text="Password:", font=ctk.CTkFont(size=12), fg="white")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

def submit_credentials():
    text = clicked.get()
    username = username_entry.get()
    password = password_entry.get()

    with open("credentials.op", "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if text == "Instagram" and "Instagram:" in line:
            lines[i + 1] = f"{username}\n"
            lines[i + 2] = f"{password}\n"
        elif text == "Discord" and "Discord:" in line:
            lines[i + 1] = f"{username}\n"
            lines[i + 2] = f"{password}\n"
        elif text == "Youtube" and "Youtube:" in line:
            lines[i + 1] = f"{username}\n"
            lines[i + 2] = f"{password}\n"
        
    with open("credentials.op", "w") as file:
        file.writelines(lines)

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    selectedVals = []
    for i in listbox.curselection():
        selectedVals.append(listbox.get(i))

    with open("selectedOptionsNew.op", "r") as file:
        lines = file.readlines()

    if text == "Instagram":
        lines[2] = f"False\n"
        lines[4] = f"False\n"
    if text == "Youtube":
        lines[8] = f"False\n"
    if text == "Discord":
        lines[12] = f"False\n"

    for i in selectedVals:
        if i == "Instagram Comments":
            lines[2] = f"True\n"
        elif i == "Instagram Messages":
            lines[4] = f"True\n"
        elif i == "Youtube Comments":
            lines[8] = f"True\n"
        elif i == "Discord Messages":
            lines[12] = f"True\n"
            
        
    with open("selectedOptionsNew.op", "w") as file:
        file.writelines(lines)
    #showOptions()

submit_button = ctk.CTkButton(window, text="Submit", font=ctk.CTkFont(size=12), command=submit_credentials)
submit_button.pack(pady=20)

buffer = tk.Label(window, text="", font=ctk.CTkFont(size=8))
buffer.pack(pady=4)



window.mainloop()