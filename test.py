import tkinter as tk

def print_selected_item():
    selected_index = listbox.curselection()  # Get the selected item's index
    if selected_index:
        selected_item = listbox.get(selected_index[0])  # Get the selected item
        result_label.config(text=f"Selected Item: {selected_item}")
    else:
        result_label.config(text="No item selected")

# Create the main window
root = tk.Tk()
root.title("Listbox Example")

# Create a Listbox widget and populate it with items
listbox = tk.Listbox(root)
listbox.pack(pady=10)

items = ["Java Exercises", "c++ Exercises", "C# Exercises", "C# Exercises", "Python Exercis es"]
for item in items:
    listbox.insert(0, item)

# Create a button to print the selected item
print_button = tk.Button(root, text="Print Selected Item", command=print_selected_item)
print_button.pack()

# Create a label to display the selected item
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter main loop
root.mainloop()
