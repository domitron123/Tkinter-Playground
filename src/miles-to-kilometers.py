#** imports
import tkinter as tk 
import ttkbootstrap as ttk

#** convert function
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.609344
    output_string.set(km_output)
    
#** window
window = ttk.Window(themename = 'darkly')
window.title('Demo')
window.geometry("350x150")

#** title widget
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
# pack title widget into window
title_label.pack()

#** input field
# create input frame to hold input widgets -> input frame is a child of window
input_frame = ttk.Frame(master = window)
# define entry_int as an integer variable
entry_int = tk.IntVar()
# create entry widget and button widget, both children of input_frame
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
# set command of button widget to convert function
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
# pack entry and button widgets into input_frame with styling
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
# pack input_frame into window
input_frame.pack(pady = 10)

#** output
# assign output_string as a string variable
output_string = tk.StringVar()
# create output label widget, child of window, with styling
output_label = ttk.Label(master = window, 
                         text = 'Kilometers: ', 
                         font = 'Calibri 25', 
                         textvariable = output_string)
# pack output_label into window
output_label.pack()

#** run window
window.mainloop()