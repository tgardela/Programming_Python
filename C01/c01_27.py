from tkinter import mainloop
from tkinter.messagebox import showinfo
from c01_25 import MyGui


class CustomGui(MyGui):
    def reply(self):
        showinfo(title = 'popup', message = 'ouch!')


if __name__ == '__main__':
    CustomGui().pack()
    mainloop()