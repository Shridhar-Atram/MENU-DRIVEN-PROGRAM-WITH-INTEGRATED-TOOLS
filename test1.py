import tkinter as tk
import os

def function1():
    # Your logic for function1
    return os.system("date")

def function2():
    # Your logic for function2
    return os.system("cal")

def display_output(output):
    # Clear the text widget before displaying new output
    text_widget.delete("1.0", tk.END)
    # Update the text widget with the output
    text_widget.insert(tk.END, output)

def back_to_main_menu():
    # Clear the text widget
    text_widget.delete("1.0", tk.END)
    # Hide the submenu and show the main menu
    main_menu.pack()
    submenu.pack_forget()

root = tk.Tk()
root.title("Nested Menu Example")

# Create the top-level menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the Main Menu (top-level menu)
main_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Main Menu", menu=main_menu)

# Add items to the Main Menu
main_menu.add_command(label="Function 1", command=lambda: display_output(function1()))
main_menu.add_command(label="Function 2", command=lambda: display_output(function2()))

# Create the Submenu
submenu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Submenu", menu=submenu)

# Add "Back to Main Menu" button to the Submenu
submenu.add_command(label="Back to Main Menu", command=back_to_main_menu)

# Create a Text widget to display the output
text_widget = tk.Text(root, height=10, width=30)
text_widget.pack()


# Start the tkinter main loop
root.mainloop()

