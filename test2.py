import tkinter as tk
import os
import subprocess

root = tk.Tk()
root.title("Nested Menu Example")
root.geometry("500x500")

def function1():
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, subprocess.check_output(["yum", ["install"], "httpd"], ["-y"]))

def function2():
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Output of Function 2")

def function3():
    # Add more sub-buttons here if needed
    sub_button1.config(text="Sub Button 1", command=sub_function1)
    sub_button2.config(text="Sub Button 2", command=sub_function2)
    sub_button3.config(text="Sub Button 3", command=sub_function3)
    sub_button4.config(text="Back to Main Menu", command=main_menu)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Sub Menu 1")

def function4():
    # Add more sub-buttons here if needed
    sub_button1.config(text="Sub Button 4", command=sub_function4)
    sub_button2.config(text="Sub Button 5", command=sub_function5)
    sub_button3.config(text="Back to Main Menu", command=main_menu)
    sub_button4.config(text="", command=None)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Sub Menu 2")

def sub_function1():
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Sub Function 1")

def sub_function2():
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Sub Function 2")

def sub_function3():
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Sub Function 3")

def sub_function4():
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Sub Function 4")

def sub_function5():
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Sub Function 5")

def main_menu():
    sub_button1.config(text="", command=None)
    sub_button2.config(text="", command=None)
    sub_button3.config(text="", command=None)
    sub_button4.config(text="", command=None)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Main Menu")

button1 = tk.Button(root, text="Button 1", command=function1)
button2 = tk.Button(root, text="Button 2", command=function2)
button3 = tk.Button(root, text="Button 3", command=function3)
button4 = tk.Button(root, text="Button 4", command=function4)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

sub_button1 = tk.Button(root, text="", command=None)
sub_button2 = tk.Button(root, text="", command=None)
sub_button3 = tk.Button(root, text="", command=None)
sub_button4 = tk.Button(root, text="", command=None)

output_text = tk.Text(root, height=400, width=50, wrap=tk.NONE)
output_text.pack()

main_menu()

root.mainloop()

