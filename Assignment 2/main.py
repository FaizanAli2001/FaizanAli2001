import tkinter as tk
from tkinter import ttk
import requests

# This function retrieves the exchange rates from an API, gets the currency codes selected by the user,
def convert():
    url = "https://openexchangerates.org/api/latest.json?app_id=13709d4010094f4d875812d3c5954778"
    response = requests.get(url)
    c1 = combobox1.get()
    c2 = combobox2.get()
    currency1 = response.json()["rates"][c1]
    currency2 = response.json()["rates"][c2]
    converted_entry.config(text=f"{currency2 / currency1 * float(amount_entry.get())}")


# Create the main window
root = tk.Tk()
root.title("Money Exchanger")

# Set the window size and center it on the screen
window_width = 500
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the background color of the window
root.configure(bg="#FFFFFF")

# Create a label for the heading
heading_label = tk.Label(root, text="CURRENCY CONVERTER", font=("Arial", 24, "bold"), fg="#2C3E50", bg="#FFFFFF",
                         pady=20)
heading_label.pack()

# Create a label for the currency selection
label = tk.Label(root, text="Select Currency", font=("Arial", 16), fg="#2C3E50", bg="#FFFFFF", padx=10, pady=10)
label.pack()

# Create a Combobox
currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "PKR"]
variable = tk.StringVar(root)
variable.set(currencies[1])  # default value
style = ttk.Style()
style.configure('my.TCombobox', font=('Arial', 14), foreground='#2C3E50', background='#FFFFFF',
                fieldbackground='#FFFFFF')
combobox1 = ttk.Combobox(root, textvariable=variable, values=currencies, style='my.TCombobox')
combobox1.pack(pady=10)

# Create a label for the amount input
amount_label = tk.Label(root, text="Enter Amount", font=("Arial", 16), fg="#2C3E50", bg="#FFFFFF", padx=10, pady=10)
amount_label.pack()

# Create an Entry box for the amount input
amount_entry = tk.Entry(root, font=("Arial", 14), bd=5, highlightthickness=1, highlightcolor="#2C3E50")
amount_entry.pack()

# Create a button
button = tk.Button(root, text="Convert", font=("Arial", 16), fg="#FFFFFF", bg="#2C3E50", bd=5, padx=20, pady=5,
                   command=convert)
button.pack(pady=20)

# Create a label for the converted amount
converted_label = tk.Label(root, text="Converted Currency", font=("Arial", 16), fg="#2C3E50", bg="#FFFFFF", padx=10,
                           pady=10)
converted_label.pack()

# Create a Combobox
currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "PKR"]
variable = tk.StringVar(root)
variable.set(currencies[0])  # default value
style = ttk.Style()
style.configure('my.TCombobox', font=('Arial', 14), foreground='#2C3E50', background='#FFFFFF',
                fieldbackground='#FFFFFF')
combobox2 = ttk.Combobox(root, textvariable=variable, values=currencies, style='my.TCombobox')
combobox2.pack(pady=10)

# Create an Entry box for the converted amount
converted_entry = tk.Label(text="Data", font=("Arial", 14), highlightcolor="#2C3E50")
converted_entry.pack()


# Create a button to reset the amount input
def reset():
    # Clear the amount entry box
    amount_entry.delete(0, tk.END)

    # Clear the converted amount label
    converted_entry.config(text="")


# Create a button to reset the amount input
reset_button = tk.Button(root, text="Reset", font=("Arial", 16), fg="#FFFFFF", bg="#C0392B", bd=5, padx=50, pady=10,
                         command=reset)
reset_button.pack(pady=20)

# Run the main loop
root.mainloop()
