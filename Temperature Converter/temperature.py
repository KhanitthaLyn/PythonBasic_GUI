from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage

root = Tk()
root.title("Temperatur-Umrechner")  # Temperature Converter
root.resizable(0, 0)

# Hintergrundfarbe ändern
bg_color = "#87ceeb"  # Light sky blue
root.configure(bg=bg_color)

icon = PhotoImage(file="icon/tem.png")  
root.iconphoto(True, icon)

# Funktionen
def reset():
    output_txt.delete(0, END)
    input_txt.delete(0, END)
    temp_combo.set("Kelvin")

def convert():
    output_txt.delete(0, END)
    try:
        celsius_value = float(input_txt.get())
        unit_value = temp_combo.get()
        if unit_value == "Kelvin":
            kelvin = celsius_value + 273.15
            output_txt.insert(0, round(kelvin, 2))
        else:
            fahrenheit = celsius_value * 1.8 + 32
            output_txt.insert(0, round(fahrenheit, 2))
    except ValueError:
        output_txt.insert(0, "Ungültige Eingabe")  # Invalid input

# Einstellungen
font = ("Arial", 15, "bold")
btn_color = "#ffa500"  # Orange
padx_val = 10
pady_val = 10

# Eingabe-Widgets
input_label = Label(root, text="Temperatur (Celsius)", font=font, bg=bg_color)
input_txt = Entry(root, width=20, font=font)
input_label.grid(row=0, column=0, sticky=W, padx=padx_val, pady=pady_val)
input_txt.grid(row=0, column=1, padx=padx_val, pady=pady_val)

# Combobox
unit_label = Label(root, text="Umwandeln in", font=font, bg=bg_color)
unit_list = ["Fahrenheit", "Kelvin"]
temp_combo = ttk.Combobox(root, value=unit_list, font=font, width=18)
temp_combo.set("Kelvin")
unit_label.grid(row=1, column=0, sticky=W, padx=padx_val, pady=pady_val)
temp_combo.grid(row=1, column=1, padx=padx_val, pady=pady_val)

# Ausgabe-Widgets
output_label = Label(root, text="Ergebnis", font=font, bg=bg_color)
output_txt = Entry(root, width=20, font=font)
output_label.grid(row=2, column=0, sticky=W, padx=padx_val, pady=pady_val)
output_txt.grid(row=2, column=1, padx=padx_val, pady=pady_val)

# Buttons in Frame
button_frame = Frame(root, bg=bg_color)
button_frame.grid(row=3, column=0, columnspan=2, pady=15)

convertBtn = Button(button_frame, text="Umrechnen", font=font, width=12, bg=btn_color, command=convert)
resetBtn = Button(button_frame, text="Zurücksetzen", font=font, width=12, bg=btn_color, command=reset)

convertBtn.pack(side=LEFT, padx=10)
resetBtn.pack(side=LEFT, padx=10)

root.mainloop()
