from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.title("Text Editor")
root.geometry('400x400')
text=Text(root,width=400,height=400)
text.pack()
root.mainloop()