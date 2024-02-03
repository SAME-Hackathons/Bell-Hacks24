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
    "YouTube"
]
drop = tk.OptionMenu( window , clicked, *mediaTypes ) 
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









def showOptions():
    type = clicked.get()
    cleanOptions = []
    if type == "Instagram": 
        cleanOptions = ["Comments", "Messages"]
    elif type == "Youtube":
        cleanOptions = ["Comments"]
    elif type == "Discord":
        cleanOptions = ["Messages"]

    prompt = tk.Label(window, text="What would you like to cleanse?", font=ctk.CTkFont(size=12), underline = True)
    prompt.pack()
    listbox = tk.Listbox(window, font=ctk.CTkFont(size=10), height = 2, selectmode = "multiple")
    for count, option in enumerate(cleanOptions, 1):
        listbox.insert(count, option)
    listbox.pack()

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
    showOptions()

submit_button = ctk.CTkButton(window, text="Submit", font=ctk.CTkFont(size=12), command=submit_credentials)
submit_button.pack(pady=20)

buffer = tk.Label(window, text="", font=ctk.CTkFont(size=8))
buffer.pack(pady=4)



window.mainloop()