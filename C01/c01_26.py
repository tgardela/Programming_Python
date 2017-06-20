from tkinter import *
from c01_25 import MyGui

#main app window
mainwin = Tk()
Label(mainwin, text = __name__).pack()

#popups
popup = Toplevel()
Label(popup, text = 'Attach').pack(side = LEFT)
MyGui(popup).pack(side = RIGHT)
mainwin.mainloop()