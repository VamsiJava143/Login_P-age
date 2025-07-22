import tkinter as tk
import time
def update_time():
    current_time=time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000,update_time)

root=tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.configure(bg="black")

label=tk.Label(root,font=("Arial",40),bg="black",fg="cyan")
label.pack(anchor="center")

update_time()
root.mainloop()
