import tkinter as tk
import os

def output_console(items):
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, f"> {items}\n")

root = tk.Tk()
root.title("hello")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the File menu (top-level menu)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add items to the File menu
file_menu.add_command(label="New", command=lambda: output_console("New"))
file_menu.add_command(label="Open", command=lambda: output_console("Open"))

# Create the Edit menu (top-level menu)
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add a submenu to the Edit menu
submenu = tk.Menu(edit_menu, tearoff=0)
edit_menu.add_cascade(label="Options", menu=submenu)

# Add items to the submenu
submenu.add_command(label="Option 1", command=lambda: output_console("Option 1"))
submenu.add_command(label="Option 2", command=lambda: output_console("Option 2"))

# Create a Text widget to display the output
text_widget = tk.Text(root, height=10, width=30)
text_widget.pack()

# Start the tkinter main loop
root.mainloop()
