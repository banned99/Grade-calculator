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
        ==== First section of programme ====
        Contains all starter widget in application window
        """
        ##Space
        Label(master, text=" ").grid(row=0)
        ##Label for text -> Number of subject
        text_sub = Label(master, text="Number of Subject :", width=20)

        ##Entry for num of subject
        self.number = IntVar()
        num_sub = Entry(master, width=5, textvariable=self.number)

        ##Start Button
        self.starter = Button(master, text="Start", command=self.start)

        ##Restart Button
        self.restart = Button(
            master, text="Restart", command=self.reset, state='disabled')

        ##Window arrangement section
        text_sub.grid(row=1, column=0, sticky=E)
        num_sub.grid(row=1, column=1, padx=5, pady=5)
        self.starter.grid(row=2, column=0)
        self.restart.grid(row=2, column=1)

        ##Data for other methods
        self.weight = []
        self.subject = []
        self.entry_subject = []
        self.entry_weight = []
        self.txt = []

    def start(self):
        """
        ==== Second section of programme ====
        -- Appear after pressed the start button
        Create the input slot of subject
        """
        ##Get data section: number of subject from __init__
        num_of_sub = self.number.get()

        ##Create data for creating subject weight and score entry slots
        for i in xrange(num_of_sub):
            if num_of_sub < 1 or num_of_sub > 20:
                pass
            else:
                self.subject.append("Subject "+str(i+1))
                self.weight.append("Weight"+str(i+1))
                self.entry_subject.append("Weight"+str(i))
                self.entry_weight.append("Subject"+str(i))
                self.txt.append("Text"+str(i))
                
        ##Text label section
        Label(text=" ", width=10).grid(row=1, column=3)
        Label(text="Weight :", width=10).grid(row=1, column=4)
        Label(text="Score :", width=10).grid(row=1, column=5)
        
        ##Create subject weight and subject score entry slots
        for j in xrange(len(self.weight)):
            self.txt[j] = Label(text=(self.subject[j]+' :'), width=15)
            self.weight[j] = DoubleVar()
            self.subject[j] = IntVar()
            
            self.entry_weight[j] = Entry(
                width=5, textvariable=self.weight[j])
            
            self.entry_subject[j] = Entry(
                width=5, textvariable=self.subject[j])

            ##All text and entry arrangement section
            self.txt[j].grid(row=j+2, column=3, sticky=E)
            
            self.entry_weight[j].grid(
                row=j+2, column=4, padx=5, pady=5)
            
            self.entry_subject[j].grid(
                row=j+2, column=5, padx=5, pady=5)

        ##Space before button
        self.space = Label(text=" ")
        self.space.grid(row=(num_of_sub+2), column=4)
        
        ##Button calcualate
        self.cal = Button(text="Calculate", command=self.calculate)
        self.cal.grid(row=(num_of_sub+3), column=4)

        ##Enable the restart button
        self.restart.config(state='active')
        
        ##Disable the start button
        self.starter.config(state='disabled')

    def reset(self):
        """
        ==== Additional fucntion ====
        -- Enable after pressed the start button
        Delete the previous input slots
        """
        ##Destroy the text at the top of entry slots
        Label(text=" ", width=10).grid(row=1, column=3)
        Label(text=" ", width=10).grid(row=1, column=4)
        Label(text=" ", width=10).grid(row=1, column=5)

        ##Destoy all input slots
        for i in xrange(len(self.weight)):
            self.entry_weight[i].destroy()
            self.entry_subject[i].destroy()
            self.txt[i].destroy()

        ##Destroy space before calulate button
        self.space.destroy()

        ##Destroy calculate button
        self.cal.destroy()

        ##Re-enable the starter button
        self.starter.config(state='active')

        ##Disable the restart button
        self.restart.config(state='disabled')

        ##Reset all data
        self.weight = []
        self.subject = []
        self.entry_subject = []
        self.entry_weight = []
        self.txt = []
        
    def calculate(self):
        """
        ==== Third section of programme ====
        -- Appear after pressed the calculate button
        Takes all data form second section, calculate, and show outputs
        """
        
    
root = Tk()
app = App(root)
root.title('Grade Calculator')
root.geometry('900x700-50-100')
root.mainloop()
root.destroy()
