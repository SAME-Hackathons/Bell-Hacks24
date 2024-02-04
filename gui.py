#imports
from class_data import *
from tkinter import *
from tkinter.ttk import Progressbar
import tkinter as tk
import customtkinter as ctk
from instagram import *

#setup main
def main():

    #setup tkinter window
    window = tk.Tk()
    window.title("Healthy Messages")
    window.geometry( "800x600" )

    #Progress bar
    p = Progressbar(window,orient=HORIZONTAL,length=200,mode="determinate",takefocus=False,maximum=100)
    p.pack()            
    for i in range(100):                
        p.step()            
        window.update()

    #titles
    label = tk.Label(text="Welcome to Healthy Messages!", font=ctk.CTkFont(size=30, weight="bold", underline=True))
    label.pack()
    subtitle = tk.Label(window, text="Media where health comes first!", font=ctk.CTkFont(size=15, slant = "italic"), pady=10)
    subtitle.pack()

    #visual buffer
    buffer = tk.Label(window, text="", font=ctk.CTkFont(size=4))
    buffer.pack(pady=4)

    #select media type
    mediaLabel = tk.Label(text="Select your media platform and provide your credentials below.", font=ctk.CTkFont(size=14))
    mediaLabel.pack()

    #visual buffer
    buffer = tk.Label(window, text="", font=ctk.CTkFont(size=4))
    buffer.pack(pady=4)

    #list of media types
    clicked = StringVar()
    clicked.set( "Social Media" ) 
    mediaTypes= [
        "Instagram", 
        "Youtube"
    ]

    #setup for attributes that can be cleaned of hateful messages, starts empty
    cleanOptions = []
    prompt = tk.Label(window, text="What would you like to cleanse?", font=ctk.CTkFont(size=15), underline = True)
    listbox = tk.Listbox(window, font=ctk.CTkFont(size=14), height = len(cleanOptions), selectmode = "multiple")

    #function to show options based on media type
    def showOptions():
        #clear exising options
        listbox.delete(0,END)

        #get options from newly selected
        type = clicked.get()
        cleanOptions = []
        if type == "Instagram": 
            cleanOptions = ["Instagram Comments", "Instagram Messages"]
        elif type == "Youtube":
            cleanOptions = ["Youtube Comments"]
        elif type == "Discord":
            cleanOptions = ["Discord Messages"]
    
        #pack option selector and label
        prompt.pack()
        for count, option in enumerate(cleanOptions, 1):
            listbox.insert(count, option)
        listbox.pack()

    #on change for change media type
    def grabcurrent(event):
        cleanOptions = []
        showOptions()
        pass

    #dropdown for media type
    drop = tk.OptionMenu( window , clicked, *mediaTypes, command = grabcurrent ) 
    drop.pack(pady=10) 

    #visual for username and password entering
    username_label = tk.Label(window, text="Username:", font=ctk.CTkFont(size=12))
    username_label.pack()
    username_entry = tk.Entry(window)
    username_entry.pack()
    buffer = tk.Label(window, text="", font=ctk.CTkFont(size=1))
    buffer.pack()
    password_label = tk.Label(window, text="Password:", font=ctk.CTkFont(size=12))
    password_label.pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    #send user/pass and cleanse preferences to files
    def submit_credentials():
        #grab selected options dropdown and fillable fields
        text = clicked.get()
        username = username_entry.get()
        password = password_entry.get()
    
        #open and read credentials file
        with open("credentials.op", "r") as file:
            lines = file.readlines()
        
        #add and replace corresponding username and password values
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
        
        #write changes to file
        with open("credentials.op", "w") as file:
            file.writelines(lines)
    
        #visually remove entered credentials
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    
        #check cleanse options checked true
        selectedVals = []
        for i in listbox.curselection():
            selectedVals.append(listbox.get(i))
        
        #open and read selected options file
        with open("selectedOptionsNew.op", "r") as file:
            lines = file.readlines()

        #reset boolean values to false before searching for selected values (only coorresponding to selected media type)
        if text == "Instagram":
            lines[2] = f"False\n"
            lines[4] = f"False\n"
        if text == "Youtube":
            lines[8] = f"False\n"
        if text == "Discord":
            lines[12] = f"False\n"

        #change selected cleanse options to true
        for i in selectedVals:
            if i == "Instagram Comments":
                lines[2] = f"True\n"
            elif i == "Instagram Messages":
                lines[4] = f"True\n"
            elif i == "Youtube Comments":
                lines[8] = f"True\n"
            elif i == "Discord Messages":
                lines[12] = f"True\n"

        #remove comments and messages from instagram using external script
        if clicked.get() == "Instagram":
            rmcomments = lines[2]
            rmmessages = lines[4]
            remove(bool(rmcomments), bool(rmmessages))

        #write changes to file    
        with open("selectedOptionsNew.op", "w") as file:
            file.writelines(lines)

        #final loading bar
        p = Progressbar(window,orient=HORIZONTAL,length=200,mode="determinate",takefocus=False,maximum=500)
        p.pack()            
        for i in range(500):                
            p.step()            
            window.update()
        
    #create submit button to accept/update credentials and cleanse options based on media type
    submit_button = ctk.CTkButton(window, text="Submit", font=ctk.CTkFont(size=12), command=submit_credentials)
    submit_button.pack(pady=20)

    #load tkinter window
    window.mainloop()

#dunder main
if __name__ == "__main__":
    main()