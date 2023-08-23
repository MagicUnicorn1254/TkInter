from tkinter import *

class Window(Frame):
    def _init_(self, master=None):
        Frame._init_(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

    def exitProgram(self):
        exit()

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text="Exit", command=self.clickExitButton)

        exitButton.place(x=0, y=0)

    def clickExitButton(self):
        exit()

root = Tk()
app = Window(root)
root.wm_title("rainbow road")
root.geometry("320x200")
root.mainloop()



