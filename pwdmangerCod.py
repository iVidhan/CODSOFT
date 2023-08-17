import tkinter as tk
from tkinter.ttk import Combobox
import random
import string

def generate_password():
    # Retrieve the desired password length and strength
    length = int(length_entry.get())
    strength = strength_combobox.get()

    # Define character sets based on the selected strength
    if strength == 'Low Strength':
        charset = string.ascii_lowercase
    elif strength == 'Medium Strength':
        charset = string.ascii_letters
    else:  # High Strength
        charset = string.ascii_letters + string.digits + string.punctuation

    # Generate the random password and display it in the entry field
    password = ''.join(random.choice(charset) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main application window
screen = tk.Tk()
screen.title("Password Generator")
screen.geometry('600x400')
screen.configure(background="bisque")

# Define the Times New Roman font
times_new_roman_font = ("Times New Roman", 14)

# Title label
title_label = tk.Label(screen, text='Password Generator', font=('Arial', 25), fg='red', background="bisque")
title_label.place(x=60, y=0)

# Password label and entry field
password_label = tk.Label(screen, text='Password:', font=times_new_roman_font, background="bisque")
password_label.place(x=145, y=90)
password_entry = tk.Entry(screen, font=times_new_roman_font)
password_entry.place(x=270, y=90)

# Length label and entry field
length_label = tk.Label(screen, text='Length:', font=times_new_roman_font, background="bisque")
length_label.place(x=145, y=120)
length_entry = tk.Entry(screen, font=times_new_roman_font, width=10)
length_entry.place(x=230, y=120)

# Strength label and combobox
strength_label = tk.Label(screen, text='Strength:', font=times_new_roman_font, background="bisque")
strength_label.place(x=145, y=155)
strength_combobox = Combobox(screen, font=times_new_roman_font, width=15, values=('Low Strength', 'Medium Strength', 'High Strength'))
strength_combobox.current(1)
strength_combobox.place(x=237, y=155)

# Generate button
generate_button = tk.Button(screen, text='Generate', font=times_new_roman_font, fg='red', background="white", command=generate_password)
generate_button.place(x=230, y=195)

# Start the Tkinter event loop
screen.mainloop()