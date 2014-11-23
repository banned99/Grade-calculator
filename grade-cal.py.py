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
        text_sub = Label(master, text="Number of Subject :", width=20)

        ##Entry for num of subject
        self.number = IntVar()
        num_sub = Entry(master, width=5, textvariable=self.number)

        ##Button start
        starter = Button(master, text="Start", command=self.start)

        ##Window arrangement section
        text_sub.grid(row=0, column=0, sticky=E)
        num_sub.grid(row=0, column=1, padx=5, pady=5)
        starter.grid(row=1, column=0)

        ##Data for other methods
        self.weight = []
        self.subject = []

    def start(self):
        """
        Create the input slot of subject
        """
        ##Get data section: number of subject from __init__
        num_of_sub = self.number.get()

        ##Text label section
        Label(text=" ", width=10).grid(row=0, column=2)
        Label(text="Weight :", width=10).grid(row=0, column=3)
        Label(text="Score :", width=10).grid(row=0, column=4)

        ##Create data for creating subject weight and subject score entry slots
        for i in xrange(num_of_sub):
            if num_of_sub < 1 or num_of_sub > 20:
                pass
            else:
                self.subject.append("Subject "+str(i+1))
                self.weight.append("Weight"+str(i+1))
                
        ##Create subject weight and subject score entry slots
        for j in xrange(len(self.weight)):
            text = Label(text=(self.subject[j]+str(' :')), width=15)
            self.weight[j] = DoubleVar()
            self.subject[j] = IntVar()
            entry_subject = Entry(width=5, textvariable=self.subject[j])
            entry_weight = Entry(width=5, textvariable=self.weight[j])

            ##All text and entry arrangement section
            text.grid(row=j+1, column=2, sticky=E)
            entry_weight.grid(row=j+1, column=3, padx=5, pady=5)
            entry_subject.grid(row=j+1, column=4, padx=5, pady=5)
            
    
root = Tk()
app = App(root)
root.geometry('500x650-50-100')
root.mainloop()
root.destroy()
