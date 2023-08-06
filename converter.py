# Importing tkinter class
from tkinter import *
from tkinter import ttk

# Functions for the "solve" buttons, which carry out the weight conversions.
def solve(*args):
    try:
        value = float(ounces.get())
        grams.set(float(value) * 28.3495)
    except ValueError:
        pass
def solve2(*args):
    try:
        value = float(pounds.get())
        ounces2.set(float(value) * 16)
    except ValueError:
        pass

# Creating the textbox for the weight converter.
root = Tk()
root.title("Weight Converter")

mainframe = ttk.Frame(root, padding="3 7 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creation of the input units
ounces = StringVar()
ounces_entry = ttk.Entry(mainframe, width=7, textvariable=ounces)
ounces_entry.grid(column=2, row=1, sticky=(W, E))

pounds = StringVar()
pounds_entry = ttk.Entry(mainframe, width=7, textvariable=pounds)
pounds_entry.grid(column=2, row=4, sticky=(W, E))

# Creation of the output units
grams = StringVar()
ttk.Label(mainframe, textvariable=grams).grid(column=2, row=2, sticky=(W, E))

ounces2 = StringVar()
ttk.Label(mainframe, textvariable=ounces2).grid(column=2, row=5, sticky=(W, E))

# Creation of the two solve buttons
ttk.Button(mainframe, text="Calculate", command=solve).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="Calculate", command=solve2).grid(column=3, row=6, sticky=W)

# Text for completing the converter
ttk.Label(mainframe, text="ounces").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="grams").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="pounds").grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="ounces").grid(column=3, row=5, sticky=W)

# Padding, binding, and other additonal touches
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

ounces_entry.focus()
pounds_entry.focus()
root.bind("<Return>", solve)
root.bind("<Return>", solve2, add="+")

root.mainloop()
