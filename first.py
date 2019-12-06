# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:53:17 2018

@author: Suman
"""
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
#win.resizable(0,0)

#Modify adding a Label

#aLabel = ttk.Label(win,text="A Label")
#aLabel.grid(column=0,row=0)

#Button Click event function
def clickMe():
    action.configure(text="Hello"+name.get())
#    aLabel.configure(foreground='red')
#    aLabel.configure(text='A Red Label')
    
ttk.Label(win,text="Enter a name:").grid(column=0,row=0)
    
#Adding a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=0,row=1)

#Adding a button
action = ttk.Button(win,text="Click Me!",command=clickMe)
action.grid(column=1,row=1)
#action.configure(state='disabled') #Disable the Button
nameEntered.focus()  #Places cursor into name Entry
 
win.mainloop()