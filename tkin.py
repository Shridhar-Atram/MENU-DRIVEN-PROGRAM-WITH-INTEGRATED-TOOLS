import tkinter as tk
import os
import face_dist
import face_crop
import face_mesh
import pose_detect
import volume
import auto
import open_ai

root = tk.Tk()
root.title("...Project Integration...")
root.geometry("500x500")

button1 = tk.Button(root, text='Measure distance of face', command=face_dist.dist)
button2 = tk.Button(root, text='Face Mesh', command=face_mesh.mesh)
button3 = tk.Button(root, text='Cropping Face', command=face_crop.cropp)
button4 = tk.Button(root, text='Pose detection', command=pose_detect.detect)
button5 = tk.Button(root, text='Increase/Decrease volume with hand', command=volume.volu)
button6 = tk.Button(root, text='Configure Webserver', command=auto.webserver)
button7 = tk.Button(root, text='Docker services', command=auto.docker_service)
button8 = tk.Button(root, text='Web Based CLI', command=auto.shellinabox)
button9 = tk.Button(root, text='Run Linux commands', command=auto.linux)
button10 = tk.Button(root, text='AWS Services', command=auto.aws)
button11 = tk.Button(root, text='Convert audio to text', command=auto.aud_conv)
button12 = tk.Button(root, text='Open AI chatbot', command=open_ai.aichat)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()
button11.pack()
button12.pack()

root.mainloop()
