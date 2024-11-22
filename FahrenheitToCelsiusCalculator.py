import tkinter as tk

window = tk.Tk()

#   This will be called when converting from Fahrenheit to Celsius
def conversion():
    f = float(fahrenheit_var.get())
    c = (f - 32) * (5/9)
    celsius_var.set(f"{c:.1f}")

#   Creation of string variables, labels, and entries for the window
fahrenheit_var = tk.StringVar()
celsius_var = tk.StringVar()
fLabel = tk.Label(text="°F")
fahrenheit = tk.Entry(textvariable=fahrenheit_var, width=10)
celsius = tk.Label(text="°C")
result = tk.Label(textvariable=celsius_var)

#   The button that calls the conversion function
btnConvert = tk.Button(text="→", command=conversion)

#   Creation of the grid layouts
fahrenheit.grid(row=0, column=0)
fLabel.grid(row=0, column=1)
btnConvert.grid(row=0, column=2)
result.grid(row=0, column=3)
celsius.grid(row=0, column=4)


window.mainloop()