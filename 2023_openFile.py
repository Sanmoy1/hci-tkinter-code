import tkinter as tk
from tkinter import filedialog

def onClickCount():
    # Open file dialog to select a text file
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt;*.csv")])
    if file_path:
        # Open the selected file and read its content
        with open(file_path, 'r') as file:
            content = file.read()  # Read the entire file content
        
        # Display the content in the label
        label.config(text=content)

# Create the main window
root = tk.Tk()
root.title("File Viewer")
root.geometry("400x400")
# Create a button that triggers the onClickCount function
button = tk.Button(root, text="Open File", command=onClickCount)
button.pack()

# Create a label to display the content
label = tk.Label(root, text="", justify=tk.LEFT, width=100, height=100)
label.pack()

# Run the application
root.mainloop()