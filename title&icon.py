import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Python GUI")

#Tab Control introduced here ------------------
tabControl = ttk.Notebook(win)          #Create tab control

tab1 = ttk.Frame(tabControl)            #Create a tab
tabControl.add(tab1,text='Tab 1')       #Add the tab

tab2 = ttk.Frame(tabControl)            #Add the second tab
tabControl.add(tab2,text='Tab 2')       #Make second tab visible

tabControl.pack(expand=1,fill='both')   #Pack to make visible
#~ Tab Control introduced here -----------------

bapi = ttk.LabelFrame(tab1,text='--Bapi--')
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

bapi2 = ttk.LabelFrame(tab2,text='Clicks')
bapi2.grid(column=0,row=0,padx=8,pady=4)

#Creating checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(bapi2,text='Disabled',variable=chVarDis,state='disabled')
check1.select()
check1.grid(column=0,row=0,sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(bapi2,text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=0,sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(bapi2,text='Toggle',variable=chVarEn)
check3.deselect()
check3.grid(column=2,row=0,sticky=tk.W)

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
    if    radSel == 0: bapi2.configure(text='Blue')
    elif  radSel == 1: bapi2.configure(text='Gold')
    elif  radSel == 2: bapi2.configure(text='Red')

#create Radiobuttons using one variable
radVar = tk.IntVar()

#Next we are selecting a non-existing index value for radVar.
radVar.set(99)

for col in range(3):
    curRad = 'rad'+str(col)
    curRad = tk.Radiobutton(bapi2,text=colors[col],variable=radVar,value=col,command=radCall)
    curRad.grid(column=col,row=6,sticky=tk.W,columnspan=3)

#Create a container to hold labels
labelsFrame = ttk.LabelFrame(bapi2,text='Labels in a frame')
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


nameEntered.focus()  #Places cursor into name Entry
 

win.mainloop()