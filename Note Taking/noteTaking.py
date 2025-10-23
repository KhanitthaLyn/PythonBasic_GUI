from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from tkinter import scrolledtext
import tkinter.messagebox
from tkinter.filedialog import *

# Root window
root = Tk()
root.title("Note Taking App")
img = Image.open("icon/note.jpg")
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo) 
root.geometry("800x600")
root.resizable(0, 0)
root.config(bg="#f0f4f3")  # background light

# Functions
def changeFont(e=None):
    if fontStyle.get() == "none":
        myFont = (fontFamily.get(), fontSize.get())
    else:
        myFont = (fontFamily.get(), fontSize.get(), fontStyle.get())
    textArea.config(font=myFont)

def newNote():
    if tkinter.messagebox.askyesno("Confirm", "Do you want to create a new note?"):
        textArea.delete("1.0", END)

def closeNote():
    if tkinter.messagebox.askyesno("Confirm", "Do you want to close the program?"):
        root.destroy()

def saveNote():
    myFile = asksaveasfilename(initialdir="./", title="Save Note", filetypes=(("Text File","*.txt"),("All Files","*.*")))
    if myFile:
        with open(myFile, "w", encoding="utf8") as file:
            file.write(fontFamily.get() + "\n")
            file.write(str(fontSize.get()) + "\n")
            file.write(fontStyle.get() + "\n")
            file.write(textArea.get("1.0", END))

def openNote():
    myFile = askopenfilename(initialdir="./", title="Open Note", filetypes=(("Text File","*.txt"),("All Files","*.*")))
    if myFile:
        with open(myFile, "r", encoding="utf8") as file:
            textArea.delete("1.0", END)
            fontFamily.set(file.readline().strip())
            fontSize.set(file.readline().strip())
            fontStyle.set(file.readline().strip())
            changeFont()
            content = file.read()
            textArea.insert("1.0", content)

# Settings
menu_color = "#27ae60"        # dark green menu
button_color = "#2ecc71"      # light green button
button_hover = "#1e8449"      # darker green on hover
text_color = "#145a32"        # dark green text
frame_border = 2               # border thickness

# Hover effect for buttons
def on_enter(e):
    e.widget['bg'] = button_hover

def on_leave(e):
    e.widget['bg'] = button_color

# Top menu frame
menuFrame = Frame(root, bg=menu_color, height=60, bd=frame_border, relief=RAISED)
menuFrame.pack(fill=X, padx=5, pady=5)

# Buttons
def createButton(img_path, command):
    img = ImageTk.PhotoImage(Image.open(img_path).resize((40,40), Image.Resampling.LANCZOS))
    btn = Button(menuFrame, image=img, bg=button_color, activebackground=button_hover,
                 bd=1, relief=RAISED, command=command)
    btn.image = img
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

btnNew = createButton("icon/new_file.png", newNote)
btnNew.pack(side=LEFT, padx=5, pady=10)

btnOpen = createButton("icon/open-file.png", openNote)
btnOpen.pack(side=LEFT, padx=5, pady=10)

btnSave = createButton("icon/save-file.png", saveNote)
btnSave.pack(side=LEFT, padx=5, pady=10)

btnQuit = createButton("icon/exit.png", closeNote)
btnQuit.pack(side=LEFT, padx=5, pady=10)

# Font options
allFonts = font.families()
fontFamily = StringVar(value="Arial")
fontSize = IntVar(value=12)
fontStyle = StringVar(value="none")

OptionMenu(menuFrame, fontFamily, *allFonts, command=changeFont).pack(side=LEFT, padx=10)
OptionMenu(menuFrame, fontSize, 8, 12, 18, 25, 36, 42, 50, command=changeFont).pack(side=LEFT, padx=10)
OptionMenu(menuFrame, fontStyle, "none", "bold", "italic", command=changeFont).pack(side=LEFT, padx=10)

# Text area frame
textFrame = Frame(root, bg="#fcf9f0", bd=frame_border, relief=SOLID)  # cream background
textFrame.pack(fill=BOTH, expand=True, padx=10, pady=10)

textArea = scrolledtext.ScrolledText(
    textFrame, 
    bg="#fcf9f0", 
    fg=text_color, 
    font=(fontFamily.get(), fontSize.get()), 
    wrap=WORD, 
    bd=frame_border, 
    relief=SOLID, 
    highlightthickness=1, 
    highlightbackground="#145a32"
)
textArea.pack(fill=BOTH, expand=True, padx=5, pady=5)

# Start mainloop
root.mainloop()
