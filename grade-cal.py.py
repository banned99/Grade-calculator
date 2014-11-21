"""
Project PSIT   : Grade-Calculator
Contributors   : Patchara Lee
                 Sittichai
Language       : Python
GUI design IDE : Tkinter
"""
from Tkinter import *

class App:
    """
    Application interface and functions
    """
    def __init__(self, master):
        """
        Contains all widget in application window
        """
        ##Label for text -> Number of subject
        text_sub = Label(master,text="Number of Subject :")

        ##Entry for num of subject
        number = IntVar()
        num_sub = Entry(master, width=5, textvariable=number)

        ##Button start
        starter = Button(master, text="Start")

        ##Button reset
        reset = Button(master, text="Reset")

        ##Window's grid arranger
        text_sub.grid(row=0, column=0, sticky=E)
        num_sub.grid(row=0, column=1, padx=5, pady=5)
        starter.grid(row=1, column=0)
        reset.grid(row=1, column=1)
        
root = Tk()
app = App(root)
root.geometry('300x100+50+50')
root.mainloop()
root.destroy()
