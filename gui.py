import tkinter as tk

window = tk.Tk()
window.title("App Name")

label = tk.Label(text="Hello, world!")
label.pack()

button = tk.Button(text="Refresh")
button.pack()

username_label = tk.Label(window, text="Username:")
username_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack()

def submit_credentials():
    username = username_entry.get()
    password = password_entry.get()

    # Here you can send the username and password to a different file or process as needed
    # For example, you could write them to a text file or send them to a server

    print("Username:", username)
    print("Password:", password)

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

submit_button = tk.Button(window, text="Submit", command=submit_credentials)
submit_button.pack()

window.mainloop()