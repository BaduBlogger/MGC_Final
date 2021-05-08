# Python program to create 
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *
import tkinter as tk
import os
from pathlib import Path
  
# import filedialog module
from tkinter import filedialog

from PIL import Image, ImageTk
  
# Function for opening the 
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select any MP3 Song",
                                          filetypes=(("Audio Files", ".mp3 .wav"),   ("All Files", "*.*")))
      
    # Change label contents
    #label_file_explorer.configure(text="File Opened: "+filename) 
    path = Path(filename)
    print(path)
    #print(os.path.abspath(path))
    cmd = str("python F:/MGC/MGC_Final/3_prediction.py "+" "+str(path))
    os.system(cmd)
	

	
# Create the root window
window = Tk()
  
# Set window title
window.title("MGC")
  
# Set window size
window.geometry("800x500")
  
#Set window background color
window.config(background = "#F0F8FF")
  

# Create a File Explorer label
label_file_explorer = Label(window, anchor = CENTER,
                            text = "Music Genre Classifier and Segregator Using CNN",
                            width = 63, height = 3, 
                            fg = "white",bg = "#2F4F4F", font = "Times 18")

image1 = Image.open("F:\MGC\MGC_Final\icon.jpg")
image1 = image1.resize((85, 80), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test

# Position image
label1.place(x=1, y=1)
      
button_explore = Button(window,
                        text = "Upload Song",
                        command = browseFiles, width = 15, height = 1 , font = "Times 12",bg = "#008B8B",fg = "white") 
  
# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer.place(x = 0, y = 0)
  
button_explore.place(x = 325, y = 250)
  

window.resizable(0,0)
window.iconbitmap(r'F:\MGC\MGC_Final\biticon.ico')
  
# Let the window wait for any events
window.mainloop()