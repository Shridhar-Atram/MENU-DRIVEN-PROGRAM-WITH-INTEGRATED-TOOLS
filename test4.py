import tkinter as tk
import os
import subprocess

def scroll_text(*args):
    text_widget.yview(*args)

def insert_text():
    text_widget.insert(tk.END, subprocess.run(["yum"], ["install"], ["httpd"], ["-y"]))

root = tk.Tk()
root.title("Text Widget with Scrolling")

# Create a Text widget with vertical scrolling
text_widget = tk.Text(root, height=10, width=40, wrap=tk.WORD)
text_widget.pack()

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(root, command=scroll_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Text widget to use the scrollbar
text_widget.config(yscrollcommand=scrollbar.set)

# Create a button to insert text
insert_button = tk.Button(root, text="Insert Text", command=insert_text)
insert_button.pack()

root.mainloop()

