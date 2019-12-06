import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Python GUI")
#win.resizable(0,0)


#Button Click event function
def clickMe():
    action.configure(text="Hello "+name.get()+' '+numberChosen.get())
    
ttk.Label(win,text="Enter a name:").grid(column=0,row=0)
    
#Adding a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=0,row=1)

#Adding a button
action = ttk.Button(win,text="Click Me!",command=clickMe)
action.grid(column=2,row=1)
#action.configure(state='disabled') #Disable the Button widget

ttk.Label(win,text="Choose a number:").grid(column=1,row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win,width=12,textvariable=number,state='readonly')
numberChosen['values'] = (1,2,4,42,100)
numberChosen.grid(column=1,row=1)
numberChosen.current(0)


#Creating checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win,text='Disabled',variable=chVarDis,state='disabled')
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win,text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text='Enabled',variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W)


#Using a scrolled Text control
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(win,width=scrolW,height=scrolH,wrap=tk.WORD)
scr.grid(column=0,columnspan=3)


#Radiobutton globals
colors = ["Blue","Gold","Red"]

#Radiobutton Callback
def radCall():
    radSel=radVar.get()
    if    radSel == 0: win.configure(background=colors[0])
    elif  radSel == 1: win.configure(background=colors[1])
    elif  radSel == 2: win.configure(background=colors[2])

#create Radiobuttons using one variable
radVar = tk.IntVar()

#Next we are selecting a non-existing index value for radVar.
radVar.set(99)

for col in range(3):
    curRad = 'rad'+str(col)
    curRad = tk.Radiobutton(win,text=colors[col],variable=radVar,value=col,command=radCall)
    curRad.grid(column=col,row=6,sticky=tk.W,columnspan=3)

#Create a container to hold labels
labelsFrame = ttk.LabelFrame(win,text='Labels in a frame')
labelsFrame.grid(column=0,row=7)

#Place labels into container element
ttk.Label(labelsFrame,text="Label1").grid(column=0,row=0,sticky=tk.W)
ttk.Label(labelsFrame,text="Label2").grid(column=1,row=0,sticky=tk.W)
ttk.Label(labelsFrame,text="Label3").grid(column=2,row=0,sticky=tk.W)



nameEntered.focus()  #Places cursor into name Entry
 
win.mainloop()