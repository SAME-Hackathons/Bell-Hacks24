from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("App Name")
window.geometry( "800x450" )
label = tk.Label(text="Welcome to MentalMessages!", font=("Helvetica", 24), fg="white")
label.pack()



button = tk.Button(text="Refresh", bg="#FFFDD0", relief=tk.FLAT)
button.pack()




mediaLabel = tk.Label(text="Select your media and provide your credentials below.", font=("Helvetica", 12), fg="white")
mediaLabel.pack()
clicked = StringVar()
clicked.set( "Social Media Type" ) 
mediaTypes= [
    "Instagram", 
    "Discord", 
    "YouTube"
]
drop = tk.OptionMenu( window , clicked, *mediaTypes ) 
drop.pack() 


username_label = tk.Label(window, text="Username:", font=("Helvetica", 16), fg="white")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()
password_label = tk.Label(window, text="Password:", font=("Helvetica", 16), fg="white")
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

submit_button = tk.Button(window, text="Submit", command=submit_credentials, bg="#FFFDD0", relief=tk.FLAT, highlightthickness=0)
submit_button.pack()

window.mainloop()