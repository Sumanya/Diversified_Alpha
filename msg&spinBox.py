import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

win = tk.Tk()
win.title("Python GUI")
#win.resizable(0,0)

bapi = ttk.LabelFrame(win,text='--Bapi--')
bapi.grid(column=0,row=0,padx=8,pady=4)


#Button Click event function
def clickMe():
    action.configure(text="Hello "+name.get()+' '+numberChosen.get())
    
ttk.Label(bapi,text="Enter a name:").grid(column=0,row=0,sticky='W')
    
#Adding a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(bapi,width=12,textvariable=name)
nameEntered.grid(column=0,row=1,sticky='W')

#Adding a button
action = ttk.Button(bapi,text="Click Me!",command=clickMe)
action.grid(column=2,row=1)
#action.configure(state='disabled') #Disable the Button widget

ttk.Label(bapi,text="Choose a number:").grid(column=1,row=0,sticky='E')
number = tk.StringVar()
numberChosen = ttk.Combobox(bapi,width=12,textvariable=number,state='readonly')
numberChosen['values'] = (1,2,4,42,100)
numberChosen.grid(column=1,row=1,sticky='E')
numberChosen.current(0)



#Creating checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(bapi,text='Disabled',variable=chVarDis,state='disabled')
check1.select()
check1.grid(column=0,row=4,sticky=tk.W,columnspan=3)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(bapi,text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W,columnspan=3)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(bapi,text='Toggle',variable=chVarEn)
check3.deselect()
check3.grid(column=2,row=4,sticky=tk.W,columnspan=3)

#GUI callback function
def checkCallback(*ignoredArgs):
    #only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disabled')
    else:   check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:   check2.configure(state='normal')

#trace the state of the two checkbuttons
    chVarUn.trace('w',lambda unused0,unused1,unused2 : checkCallback())
    chVarEn.trace('w',lambda unused0,unused1,unused2 : checkCallback())
    

#Using a scrolled Text control
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(bapi,width=scrolW,height=scrolH,wrap=tk.WORD)
scr.grid(column=0,sticky='WE',columnspan=3)


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
    curRad = tk.Radiobutton(bapi,text=colors[col],variable=radVar,value=col,command=radCall)
    curRad.grid(column=col,row=6,sticky=tk.W,columnspan=3)

#Create a container to hold labels
labelsFrame = ttk.LabelFrame(bapi,text='Labels in a frame')
labelsFrame.grid(column=0,row=7,padx=20,pady=40)

#Place labels into container element
ttk.Label(labelsFrame,text="Label1").grid(column=0,row=0)
ttk.Label(labelsFrame,text="Label2").grid(column=0,row=1)
ttk.Label(labelsFrame,text="Label3").grid(column=0,row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8,pady=4)

#Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

#Creating a Menu bar
menuBar = Menu(win)
win.config(menu=menuBar)

#Add menu items
fileMenu = Menu(menuBar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=_quit)
menuBar.add_cascade(label="File",menu=fileMenu)

#Display a Message box
def _msgBox():
#Callback function
#    mBox.showinfo('Pythonn Message Info Box','A Python GUI created using tkinter.\nThe year is 2018.')
#    mBox.showwarning('Pythonn Message Warning Box','A Python GUI created using tkinter.\nThere might be a bug in this code.')
#    mBox.showerror('Pythonn Message Error Box','A Python GUI created using tkinter.\nError: We have got a serious problem.')
    answer = mBox.askyesno("Python Message Dual Choice Box","Are you sure you really wish to do this?!")
    print(answer)

#Add another menu to the menu bar
helpMenu = Menu(menuBar,tearoff=0)
helpMenu.add_command(label="About",command=_msgBox)
menuBar.add_cascade(label="Help",menu=helpMenu)

#Change main window icon
win.iconbitmap('C:/Users/Suman/Documents/GUI/icon.jpg')


nameEntered.focus()  #Places cursor into name Entry
 
win.mainloop()