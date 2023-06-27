# import tkinter and ttk
import tkinter as tk
from tkinter import ttk

# button_funch() function to run when button is clicked
def button_func():
    # get the content of the entry widget
    entry_content = entry.get()
    # print the content of the entry widget
    print(entry_content)

# window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('800x500')

# widgets
# label widget with styling 
label = ttk.Label(master = window, text = 'Hello, world!', font = 'Calibri 24 bold')
label.pack()

# entry widget 
entry = ttk.Entry(master = window)
entry.pack()

# button widget with styling and command to run button_func
button = ttk.Button(master = window, text = 'Click me!', command = button_func)
button.pack()

# run
window.mainloop()