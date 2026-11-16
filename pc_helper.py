import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("PC Helper")
root.geometry("320x200")
root.resizable(False, False)

status = tk.Label(
    root,
    text="PC Helper запущен",
    font=("Arial", 14)
)
status.pack(pady=25)

def notify():
    messagebox.showinfo(
        "PC Helper",
        "Уведомление: скриншот создан"
    )

button = tk.Button(
    root,
    text="Проверить уведомление",
    command=notify
)
button.pack(pady=10)

def stop():
    if messagebox.askyesno("PC Helper", "Отключить программу?"):
        root.destroy()

tk.Button(
    root,
    text="Отключить",
    command=stop
).pack(pady=5)

root.mainloop()
