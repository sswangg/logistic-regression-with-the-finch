from tkinter import *


class Application(Tkinter.Frame):
    def __init__(self, master):
        Tkinter.Frame.__init__(self, master)
        self.master.minsize(width=100, height=100)
        self.master.config()

        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)

        self.main_frame = Tkinter.Frame()
        self.main_frame.pack(fill='both', expand=True)
        self.pack()

    @staticmethod
    def left_key(event):
        print(event + " key pressed")

    @staticmethod
    def right_key(event):
        print(event + " key pressed")

root = Tkinter.Tk()
app = Application(root)
app.mainloop()
