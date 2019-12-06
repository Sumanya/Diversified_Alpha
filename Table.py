from tkintertable import TableCanvas, TableModel


tframe = Frame(master)
tframe.pack()
table = TableCanvas(tframe)
table.show()

model = TableModel()
table = TableCanvas(frame, model=model)


data = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},
       'rec2': {'col1': 99.88, 'col2': 108.79, 'label': 'rec2'}} 
