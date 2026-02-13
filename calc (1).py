import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#EAFAF1")
root.resizable(0, 0)


entry = tk.Entry(root, font=('Arial', 20), bg="blue", fg="white",
                 bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)


def click(x):
    entry.insert(tk.END, x)

def clear():
    entry.delete(0, tk.END)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sin_func():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def cos_func():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def tan_func():
    try:
        value = float(entry.get())
        result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")


buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

r = 1
c = 0

for b in buttons:
    if b == "=":
        cmd = calc
        bg = "#9AE630"
    else:
        cmd = lambda x=b: click(x)
        bg = "#9AE630" if b in "+-*/=" else "#45556C"

    tk.Button(root, text=b, command=cmd, font=('Arial', 20),
              bg=bg, fg="white", bd=0,
              width=4, height=2).grid(row=r, column=c, padx=3, pady=3)

    c += 1
    if c == 4:
        c = 0
        r += 1

tk.Button(root, text="C", command=clear, font=('Arial', 20),
          bg="#F2A097", fg="white", bd=0, width=4, height=2).grid(row=r, column=0,padx=3, pady=3)

tk.Button(root, text="sin", command=sin_func, font=('Arial', 20),
          bg="purple", fg="white", bd=0, width=4, height=2).grid(row=r, column=1,padx=3, pady=3)

tk.Button(root, text="cos", command=cos_func, font=('Arial', 20),
          bg="purple", fg="white", bd=0, width=4, height=2).grid(row=r, column=2,padx=3, pady=3)

tk.Button(root, text="tan", command=tan_func, font=('Arial', 20),
          bg="purple", fg="white", bd=0, width=4, height=2).grid(row=r, column=3,padx=3, pady=3)

root.mainloop()
