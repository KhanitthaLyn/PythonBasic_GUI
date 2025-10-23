from tkinter import *
from tkinter import ttk
import platform

root = Tk()
root.title("Calculator")

# ================= Icon =================
icon = PhotoImage(file="icon/cal-logo.png")  # PNG ใช้ได้ทั้ง Windows/Mac
root.iconphoto(True, icon)

# ================= Geometry =================
root.geometry("300x400")
root.resizable(0, 0)

# ================= Font Settings =================
if platform.system() == "Darwin":  # Mac
    displayFont = ("Arial", 24)
    btnFont = ("Arial", 14)
else:
    displayFont = ("Arial", 28)
    btnFont = ("Arial", 16)

color = "#FFA500"  # สีส้มปุ่ม operator
numberColor = "#D9D9D9"
clearQuitColor = "#FF6666"

# ================= Style =================
style = ttk.Style()
style.theme_use('default')

style.configure("TButton",
                font=btnFont,
                foreground="white",
                background=color)

style.configure("Number.TButton",
                font=btnFont,
                foreground="black",
                background=numberColor)

style.configure("Clear.TButton",
                font=btnFont,
                foreground="white",
                background=clearQuitColor)

# ================= Functions =================
def negate():
    try:
        result = float(display.get()) * -1
        display.delete(0, END)
        display.insert(0, result)
    except:
        pass

def square():
    try:
        result = float(display.get()) ** 2
        display.delete(0, END)
        display.insert(0, result)
    except:
        pass

def inverse():
    try:
        if display.get() == "0":
            result = "ERROR"
        else:
            result = 1 / float(display.get())
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def clearDisplay():
    display.delete(0, END)
    enableOperator()

def showNumber(number):
    display.insert(END, number)
    if "." in display.get():
        btnDecimal.state(["disabled"])

def equal():
    try:
        if operator == "add":
            result = float(firstNumber) + float(display.get())
        elif operator == "subtract":
            result = float(firstNumber) - float(display.get())
        elif operator == "multiply":
            result = float(firstNumber) * float(display.get())
        elif operator == "divide":
            if display.get() == "0":
                result = "ERROR"
            else:
                result = float(firstNumber) / float(display.get())
        elif operator == "exponent":
            result = float(firstNumber) ** float(display.get())
        display.delete(0, END)
        display.insert(0, result)
        enableOperator()
    except:
        display.delete(0, END)
        display.insert(0, "ERROR")

def operation(value):
    global firstNumber
    global operator
    operator = value
    firstNumber = display.get()
    btnDecimal.state(["!disabled"])
    display.delete(0, END)
    # Disable operator buttons
    for btn in [btnAdd, btnSubtract, btnMultiply, btnDivide, btnExponent, btnInverse, btnSquare]:
        btn.state(["disabled"])

def enableOperator():
    for btn in [btnAdd, btnSubtract, btnMultiply, btnDivide, btnExponent, btnInverse, btnSquare, btnDecimal]:
        btn.state(["!disabled"])

# ================= Frames =================
displayFrame = LabelFrame(root, bd=0)
buttonFrame = LabelFrame(root, bd=0)
displayFrame.pack(padx=10, pady=10, fill="both")
buttonFrame.pack(padx=10, pady=10, fill="both", expand=True)

# ================= Display =================
display = Entry(displayFrame, width=15, font=displayFont, bg="white", fg="black", border=5, justify=RIGHT)
display.pack(padx=10, pady=10, fill="x")

# ================= Clear & Quit =================
btnClear = ttk.Button(buttonFrame, text="Clear", style="Clear.TButton", command=clearDisplay)
btnQuit = ttk.Button(buttonFrame, text="Quit", style="Clear.TButton", command=root.destroy)
btnClear.grid(row=0, column=0, columnspan=2, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
btnQuit.grid(row=0, column=2, columnspan=2, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)

# ================= Operator Buttons =================
btnInverse = ttk.Button(buttonFrame, text="1/x", style="TButton", command=inverse)
btnSquare = ttk.Button(buttonFrame, text="x^2", style="TButton", command=square)
btnExponent = ttk.Button(buttonFrame, text="x^n", style="TButton", command=lambda: operation("exponent"))
btnDivide = ttk.Button(buttonFrame, text="/", style="TButton", command=lambda: operation("divide"))
btnMultiply = ttk.Button(buttonFrame, text="x", style="TButton", command=lambda: operation("multiply"))
btnSubtract = ttk.Button(buttonFrame, text="-", style="TButton", command=lambda: operation("subtract"))
btnAdd = ttk.Button(buttonFrame, text="+", style="TButton", command=lambda: operation("add"))
btnEqual = ttk.Button(buttonFrame, text="=", style="TButton", command=equal)
btnDecimal = ttk.Button(buttonFrame, text=".", style="TButton", command=lambda: showNumber("."))
btnNegate = ttk.Button(buttonFrame, text="+/-", style="TButton", command=negate)

# ================= Number Buttons =================
buttons = {}
for i in range(10):
    buttons[i] = ttk.Button(buttonFrame, text=str(i), style="Number.TButton", command=lambda x=i: showNumber(x))

# ================= Grid Configuration =================
for i in range(6):
    buttonFrame.rowconfigure(i, weight=1)
for j in range(4):
    buttonFrame.columnconfigure(j, weight=1)

# ================= Grid Layout =================
# Row 1
btnInverse.grid(row=1, column=0, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
btnSquare.grid(row=1, column=1, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
btnExponent.grid(row=1, column=2, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
btnDivide.grid(row=1, column=3, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)

# Row 2
buttons[7].grid(row=2, column=0, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
buttons[8].grid(row=2, column=1, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
buttons[9].grid(row=2, column=2, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
btnMultiply.grid(row=2, column=3, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)

# Row 3
buttons[4].grid(row=3, column=0, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
buttons[5].grid(row=3, column=1, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
buttons[6].grid(row=3, column=2, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
btnSubtract.grid(row=3, column=3, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)

# Row 4
buttons[1].grid(row=4, column=0, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
buttons[2].grid(row=4, column=1, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
buttons[3].grid(row=4, column=2, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
btnAdd.grid(row=4, column=3, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)

# Row 5
btnNegate.grid(row=5, column=0, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
buttons[0].grid(row=5, column=1, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
btnDecimal.grid(row=5, column=2, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)
btnEqual.grid(row=5, column=3, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=5)

root.mainloop()
