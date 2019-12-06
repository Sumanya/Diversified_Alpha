import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox 
from tkinter import Spinbox

class ToolTip(object):
    def __init__(self,widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
    def showtip(self,text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x,y,_cx,cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27 
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d"%(x,y))
        
        label = tk.Label(tw,text=self.text,justify=tk.LEFT,
                         background="#ffffe0",relief=tk.SOLID,borderwidth=1,
                         font=("tahoma","8","normal"))
        label.pack(ipadx=1)
    
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
        
#====================================

def creatToolTip(widget,text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>',enter)
    widget.bind('<Leave>',leave)
    
#Create instance and add title
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

#Spinbox Callback
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT,value+'\n')


#Adding spinbox widget
spin = Spinbox(bapi,width =5,bd=8,command=_spin)
spin["values"] = (1,2,4,42,100)
spin.grid(column=0,row=2)
creatToolTip(spin,'This is a Spin control.')


#Adding second spinbox widget using set of values
#spin2 = Spinbox(bapi,from_=0, to=10,width =5,bd=8,command=_spin,relief=tk.RIDGE)
#spin2.grid(column=1,row=2)
#creatToolTip(spin2,'This is a Spin control.')

#Using a scrolled Text control
scrolW = 30; scrolH = 3
scr = scrolledtext.ScrolledText(bapi,width=scrolW,height=scrolH,wrap=tk.WORD)
scr.grid(column=0,sticky='WE',columnspan=3)

#Adding a tooltip to the scrooltext widgets
creatToolTip(scr,'This is a ScrolledText widget.')

#Tab control 2 refactoring ---------------------
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

strData = spin.get()
print("Spinbox value: "+strData)

nameEntered.focus()  #Places cursor into name Entry
#===============================
#Strat GUI
#=============================== 
win.mainloop()    
        
        