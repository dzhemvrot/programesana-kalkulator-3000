import tkinter as tk
from tkinter import messagebox

def on_click(char):
    entry.config(state="normal")
    if char == 'C':
        entry.delete(0, tk.END)
    elif char == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error!")
            messagebox.showerror("ERROR", "ТЫ ДАУН ЧЁ ТВОРИШЬ") 
            entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)
    entry.config(state="readonly")

def on_key(event):
    entry.config(state="normal")
    key = event.char
    if key in "0123456789+-*/().=":
        on_click(key)
    elif event.keysym == "Return":
        on_click("=")
    elif event.keysym == "BackSpace":
        entry.delete(len(entry.get())-1, tk.END)
    elif event.keysym.upper() == "C":
        on_click("C")
    entry.config(state="readonly")

root = tk.Tk()
root.title("Calculator 3000")

entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=5, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.config(state="readonly")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('=', 5, 2, 2)
]

for (text, row, col, *extra) in buttons:
    colspan = extra[0] if extra else 1
    btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: on_click(t))
    btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.bind("<Key>", on_key)

root.mainloop()

