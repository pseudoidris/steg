import tkinter
from tkinter import *
from tkinter import filedialog
from functools import partial
import encode
import pickle

def browsefunc():
    filename = filedialog.askopenfilename()
    f = open("tmppath.txt","w")
    f.write(filename)
    f.close()
    pathlabel.config(text=filename)

def save_message(msg):

    encode.main()

top = tkinter.Tk()
top.title("Stagnography")
top.geometry('800x600')
label1= Label(top,text="Please Select the image file which you have to encrypt...!!!!" ,font = "Calibri 16 bold",fg="red")
label1.pack()


#browse button
browsebutton = Button(top,text="Browse",command=browsefunc)
browsebutton.pack()
pathlabel = Label(top)
pathlabel.pack()


#uploadbutton
uploadbutton = Button(top,text="Upload")
uploadbutton.pack()


L1 = Label(top, text="Enter the msg to Encrypt in the image")
L1.pack()
E1 = Entry(top, bd =2,width=30)
E1.pack()


#Encryptbutton
encryptbutton = Button(top,text="Encrypt", command=save_message)
encryptbutton.pack()



top.mainloop()
