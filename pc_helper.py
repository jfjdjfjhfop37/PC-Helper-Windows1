import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("PC Helper")
root.geometry("300x180")

status = tk.Label(
    root,
    text="Помощник запущен",
    font=("Arial", 14)
)
status.pack(pady=25)

def stop():
    if messagebox.askyesno("Выход", "Отключить помощник?"):
        root.destroy()

button = tk.Button(
    root,
    text="Отключить",
    command=stop
)
button.pack(pady=10)

root.mainloop()