from tkinter import *
from tkinter import ttk

# root window
root = Tk()
root.title("Checklisten-Anwendung Demo")  # "CheckList Application Demo"
root.iconbitmap("icon/check.ico")
root.geometry("450x500+500+100")
root.resizable(0,0)

# settings
font = ("Arial", 14)
bg_color = "#1E90FF"  # Dark blue background
fg_color = "white"

root.config(bg=bg_color)

# functions
def addItem():
    data = inputEntry.get()
    if data.strip() != "":
        listbox.insert(END, data)
        inputEntry.delete(0, END)

def removeItem():
    listbox.delete(ANCHOR)

def clearList():
    listbox.delete(0, END)

# style for ttk buttons
style = ttk.Style()
style.theme_use('clam') 
style.configure('Blue.TButton', background='#104E8B', foreground=fg_color, font=font, padding=5)
style.map('Blue.TButton', background=[('active', '#1874CD')])

style.configure('Red.TButton', background='#B22222', foreground=fg_color, font=font, padding=5)
style.map('Red.TButton', background=[('active', '#FF4500')])

# design frames
input_frame = Frame(root, bg=bg_color)
output_frame = Frame(root, bg=bg_color)
button_frame = Frame(root, bg=bg_color)

input_frame.pack(pady=20)
output_frame.pack(pady=10)
button_frame.pack(pady=10)

# input widget
inputEntry = Entry(input_frame, width=25, font=font)
inputEntry.grid(row=0, column=0, padx=5, pady=5, ipady=5)

btnAdd = ttk.Button(input_frame, text="Eintrag hinzufügen", style='Blue.TButton', command=addItem)
# "Eintrag hinzufügen" means "Add Item"
btnAdd.grid(row=0, column=1, padx=5, pady=5, ipadx=10, ipady=2)

# output widget
listbox = Listbox(output_frame, width=40, height=15, font=font, bd=3, relief=GROOVE, selectbackground="#87CEFA")
listbox.grid(row=0, column=0, padx=5, pady=5)

# button widget
btnRemove = ttk.Button(button_frame, text="Löschen", style='Blue.TButton', command=removeItem)
# "Löschen" means "Delete"
btnClear = ttk.Button(button_frame, text="Alle löschen", style='Blue.TButton', command=clearList)
# "Alle löschen" means "Clear All"
btnQuit = ttk.Button(button_frame, text="Schließen", style='Red.TButton', command=root.destroy)
# "Schließen" means "Close"

btnRemove.grid(row=0, column=0, padx=5, pady=5, ipadx=10)
btnClear.grid(row=0, column=1, padx=5, pady=5, ipadx=10)
btnQuit.grid(row=0, column=2, padx=5, pady=5, ipadx=10)

root.mainloop()
