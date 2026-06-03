import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 24), justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        action = (
            calculate if btn == '='
            else lambda x=btn: click(x)
        )

        tk.Button(
            frame,
            text=btn,
            font=("Arial", 18),
            command=action
        ).pack(side="left", expand=True, fill="both")

tk.Button(
    root,
    text="Clear",
    font=("Arial", 18),
    command=clear
).pack(fill="both", padx=10, pady=10)

root.mainloop()