from tkinter import filedialog
from tkinter import *
import os

class App():

    def openFile(self):
        file = filedialog.askopenfilename(
            initialdir = '/',
            title = 'Selecciona una imagen',
            filetypes = (
                ('png files', '.png'),
                ('jpeg files', '.jpg'), 
            )
        )
        self.filename = file

    def quit(self):
        self.root.destroy()

    def __init__(self):
        self.filename = ''
        self.root = Tk()
        self.root.title('Socket imagen')
        self.root.geometry('350x100')

        Button(
            text = 'Seleccionar imagen',
            command = self.openFile,
        ).place(x = 117.5, y = 20)

        Button(
            text = 'Aceptar',
            command = self.quit,
        ).place(x = 150, y = 60)
        self.root.mainloop()

# app = App()