import pickle
import tkinter as tk
from tkinter import filedialog

def save_list():
    file_name = filedialog.asksaveasfilename(filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        if not file_name.endswith(".dat"):
            file_name += ".dat"
        with open(file_name, 'wb') as output_file:
            pickle.dump(my_list.get(0, tk.END), output_file)

def open_list():
    file_name = filedialog.askopenfilename(filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        my_list.delete(0, tk.END)
        with open(file_name, 'rb') as input_file:
            my_list.insert(tk.END, *pickle.load(input_file))

def modify_item(color):
    selected_index = my_list.curselection()
    if selected_index:
        my_list.itemconfig(selected_index, fg=color)
        my_list.selection_clear(0, tk.END)

root = tk.Tk()
root.title('Tasks to do')
root.geometry("500x500")
root.config(bg="#FFF9EB")  

my_list = tk.Listbox(root, font=("Brush Script MT", 30, "bold"), width=25, height=5,
                     bg="#FFFACD", bd=0, fg="#464646", borderwidth=5, highlightthickness=0,
                     selectbackground="#a6a6a6", activestyle="none")
my_list.pack(pady=10)

my_scrollbar = tk.Scrollbar(root, command=my_list.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
my_list.config(yscrollcommand=my_scrollbar.set)

entry_var = tk.StringVar()
my_entry = tk.Entry(root, font=("Helvetica", 24), width=26, borderwidth=5, textvariable=entry_var)
my_entry.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

button_commands = [lambda: my_list.delete(tk.ANCHOR),
                   lambda: my_list.insert(tk.END, entry_var.get()) if entry_var.get().strip() else None,
                   lambda: modify_item("#dedede"), lambda: modify_item("#464646"),
                   lambda: [my_list.delete(idx) for idx in reversed(range(my_list.size())) if my_list.itemcget(idx, "fg") == "#dedede"]]

for col, (text, command) in enumerate(zip(["Delete Item", "Add Item", "Cross off Item", "Uncross Item", "Delete Crossed"], button_commands)):
    tk.Button(button_frame, text=text, command=command).grid(row=0, column=col, padx=10)

my_menu = tk.Menu(root)
root.config(menu=my_menu)

file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=lambda: my_list.delete(0, tk.END))

Tasks = ["Prayer time", "Exercise", "Bullet service", "movie with gaurav",
         "dinner", "study quantum computing", "follow up mint"]

my_list.insert(tk.END, *Tasks)

root.mainloop()