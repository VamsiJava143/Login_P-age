import tkinter as tk
from tkinter import messagebox

#Creating Main Window
root=tk.Tk()
root.title("Login Page")
root.geometry("300x200")
root.configure(bg="lightblue")

#Username label and Entry
tk.Label(root,text="Username:",bg="lightblue").pack(pady=(20,5))
username_entry=tk.Entry(root);
username_entry.pack()

#Password label and Entry
tk.Label(root,text="Password:",bg="lightblue").pack(pady=(10,5))
password_entry=tk.Entry(root,show="*")
password_entry.pack()
def login():
    username=username_entry.get()
    password= password_entry.get()
    if username == "admin" and password=="admin123":
        messagebox.showinfo("Login Succussfull")
    else:
        messagebox.showerror("Incorrect Username or Password")

#Login Button
tk.Button(root,text="Login",bg="green",fg="white",command=login).pack(pady=20)


root.mainloop()