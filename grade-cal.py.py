"""
Project PSIT   : Grade-Calculator
Contributors   : Patchara Lee
                 Sittichai
Language       : Python
GUI design IDE : Tkinter
"""
from Tkinter import *
import tkMessageBox

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
        Label(master, text=" ").grid(row=3)
        Label(text=" ", width=5).grid(row=1, column=3)
        
        ##Label for text -> Number of subject
        text_sub = Label(master, text="Number of Subject :", width=20)

        ##Entry for num of subject
        self.number = IntVar(value=1)
        num_sub = Entry(master, width=5, textvariable=self.number)

        ##Start Button
        self.starter = Button(master, text="Start", command=self.start)

        ##Restart Button
        self.restart = Button(
            master, text="Restart", command=self.reset, state='disabled')

        ##Text for grade range
        Label(master, text="Grade Range :").grid(row=4, column=0,)
        Label(master, text="A    :", width=5).grid(row=5, column=0, sticky=N)
        Label(master, text="B+ :", width=5).grid(row=6, column=0, sticky=N)
        Label(master, text="B    :", width=5).grid(row=7, column=0, sticky=N)
        Label(master, text="C+ :", width=5).grid(row=8, column=0, sticky=N)
        Label(master, text="C    :", width=5).grid(row=9, column=0, sticky=N)
        Label(master, text="D+ :", width=5).grid(row=10, column=0, sticky=N)
        Label(master, text="D    :", width=5).grid(row=11, column=0, sticky=N)
        Label(text=" ", width=10).grid(row=13, column=0)
            
        ##Entry for grade range
        self.grade_a = DoubleVar(value=80.0)
        ent_a = Entry(master, width=5, textvariable=self.grade_a)
        self.grade_b_plu = DoubleVar(value=75.0)
        ent_b_plu = Entry(master, width=5, textvariable=self.grade_b_plu)
        self.grade_b = DoubleVar(value=70.0)
        ent_b = Entry(master, width=5, textvariable=self.grade_b)
        self.grade_c_plu = DoubleVar(value=65.0)
        ent_c_plu = Entry(master, width=5, textvariable=self.grade_c_plu)
        self.grade_c = DoubleVar(value=60.0)
        ent_c = Entry(master, width=5, textvariable=self.grade_c)
        self.grade_d_plu = DoubleVar(value=55.0)
        ent_d_plu = Entry(master, width=5, textvariable=self.grade_d_plu)
        self.grade_d = DoubleVar(value=50.0)
        ent_d = Entry(master, width=5, textvariable=self.grade_d)
        
        ##Window arrangement section
        text_sub.grid(row=1, column=0, sticky=E)
        num_sub.grid(row=1, column=1, padx=5, pady=5)
        self.starter.grid(row=2, column=0)
        self.restart.grid(row=2, column=1)
        ent_a.grid(row=5, column=1, padx=5, pady=5)
        ent_b_plu.grid(row=6, column=1, padx=5, pady=5)
        ent_b.grid(row=7, column=1, padx=5, pady=5)
        ent_c_plu.grid(row=8, column=1, padx=5, pady=5)
        ent_c.grid(row=9, column=1, padx=5, pady=5)
        ent_d_plu.grid(row=10, column=1, padx=5, pady=5)
        ent_d.grid(row=11, column=1, padx=5, pady=5)
            
        ##Data for other methods
        self.weight = []
        self.subject = []
        self.entry_subject = []
        self.entry_weight = []
        self.txt = []
        self.grade_print = []
        self.var_print = []

    def start(self):
        """
        ==== Second section of programme ====
        -- Appear after pressed the start button
        Create the input slot of subject
        """   
        ##Get data section: number of subject from __init__
        self.num_of_sub = self.number.get()

        try:
            temp = [self.grade_a, self.grade_b_plu, self.grade_b,
                    self.grade_c_plu, self.grade_c, self.grade_d_plu,
                    self.grade_d]
            for i in temp:
                tester = i.get()

            ##Create data for creating subject weight and score entry slots
            for i in xrange(self.num_of_sub):
                if self.num_of_sub < 1 or self.num_of_sub > 20:
                    tkMessageBox.showerror(title='Value error',
                                           message='Value must be 1 - 20')
                    break
                else:
                    self.subject.append("Subject "+str(i+1))
                    self.weight.append("Weight"+str(i+1))
                    self.entry_subject.append("Subject"+str(i))
                    self.entry_weight.append("Weight"+str(i))
                    self.txt.append("Text"+str(i))

            if self.subject == []:
                pass
            else:        
                ##Text label section
                self.txt_weight = Label(text="Weight :", width=10)
                self.txt_score = Label(text="Score :", width=10)
                self.txt_weight.grid(row=1, column=4)
                self.txt_score.grid(row=1, column=5)
                
                ##Create subject weight and subject score entry slots
                for j in xrange(len(self.weight)):
                    self.txt[j] = Label(text=(self.subject[j]+' :'), width=15)
                    self.weight[j] = DoubleVar(value=1.0)
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

                ##Space before and after button
                self.space_be = Label(text=" ")
                self.space_af = Label(text=" ")
                self.space_be.grid(row=(self.num_of_sub+2), column=4)
                self.space_af.grid(row=(self.num_of_sub+4), column=4)
                
                ##Button calcualate
                self.cal = Button(text="Calculate", command=self.calculate)
                self.cal.grid(row=(self.num_of_sub+3), column=4)

                ##Reset button
                self.reset_result = Button(text="Reset",
                                           command=self.re_result, 
                                           state='disabled')
                self.reset_result.grid(row=(self.num_of_sub+3), column=5)

                ##Enable the restart button
                self.restart.config(state='active')
                
                ##Disable the start button
                self.starter.config(state='disabled')
        except:
            tkMessageBox.showerror(title='Value Error',
                                   message='Value must be number')
        
    def calculate(self):
        """
        ==== Third section of programme ====
        -- Appear after pressed the calculate button
        Takes all data form second section, calculate, and show outputs
        """
        ##Text each subject result
        self.txt_result = Label(text="Result :", width=10)
        self.txt_grade = Label(text="Grade :", width=10)
        self.txt_aver = Label(text="Grade Average :", width=11)
        
        ##Get all the data for calculate and show
        weight_var = []
        grade_var = []
        grade_data = {'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5,
                      'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}
        result = []

        for i in xrange(len(self.weight)):
            self.grade_print.append('Result'+str(i+1))
            self.var_print.append('Grade'+str(i+1))
            weight_var.append(self.weight[i].get())
            
            if self.subject[i].get() >= self.grade_a.get():
                grade_var.append('A')
            elif self.subject[i].get() >= self.grade_b_plu.get():
                grade_var.append('B+')
            elif self.subject[i].get() >= self.grade_b.get():
                grade_var.append('B')
            elif self.subject[i].get() >= self.grade_c_plu.get():
                grade_var.append('C+')
            elif self.subject[i].get() >= self.grade_c.get():
                grade_var.append('C')
            elif self.subject[i].get() >= self.grade_d_plu.get():
                grade_var.append('D+')
            elif self.subject[i].get() >= self.grade_d.get():
                grade_var.append('D')
            else:
                grade_var.append('F')

        ##Text arrange section
        self.txt_result.grid(row=1, column=6)
        self.txt_grade.grid(row=1, column=7)

        ##Calculate and show result section
        for j in xrange(len(grade_var)):
            result.append(grade_data[grade_var[j]] * weight_var[j])

            ##Show result section
            grade_sub = StringVar(value=grade_var[j])
            self.grade_print[j] = Entry(width=5, textvariable=grade_sub,
                                        state='disabled')
            var_sub = DoubleVar(value=grade_data[grade_var[j]])
            self.var_print[j] = Entry(width=5, textvariable=var_sub,
                                      state='disabled')

            ##Show result arrange section
            self.grade_print[j].grid(row=j+2, column=6, padx=5, pady=5)
            self.var_print[j].grid(row=j+2, column=7, padx=5, pady=5)

        ##Show grade average
        aver = sum(result) / sum(weight_var)
        grade_average = StringVar(value='%.2f' % aver)
        self.grade_aver = Entry(width=5, textvariable=grade_average,
                                state='disabled')

        ##Show grade average arrangement
        self.txt_aver.grid(row=len(grade_var)+3, column=6)
        self.grade_aver.grid(row=len(grade_var)+3, column=7)

        ##Disable the calculate button
        self.cal.config(state='disabled')

        ##Enable the reset button
        self.reset_result.config(state='active')

    def reset(self):
        """
        === Additonal function ===
        -- Appear after pressed start button
        - Active after pressed calculate button
        Revert to basic interface before pressed start button
        """
        ##Destroy the second section
        ##Destroy the text at the top of entry slots
        self.txt_weight.destroy()
        self.txt_score.destroy()

        ##Destoy all input slots
        for i in xrange(len(self.weight)):
            self.entry_weight[i].destroy()
            self.entry_subject[i].destroy()
            self.txt[i].destroy()

        ##Destroy space before and after calulate button
        self.space_be.destroy()
        self.space_af.destroy()

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

        ##Destroy third section
        if self.grade_print == []:
            pass
        else:
            ##Destroy text on the top
            self.txt_result.destroy()
            self.txt_grade.destroy()
            self.txt_aver.destroy()

            ##Destroy all result slots
            for i in xrange(len(self.var_print)):
                if type(self.grade_print[i]) == str:
                    pass
                else:
                    self.grade_print[i].destroy()
                    self.var_print[i].destroy()

            ##Destroy grade average result entry
            self.grade_aver.destroy()

        ##Destroy second section button
        self.reset_result.destroy()

        ##Reset third section
        self.grade_print = []
        self.var_print = []

    def re_result(self):
        """
        ==== Additional function ====
        -- Active after pressed calculate button
        Destroy all result
        """
        ##Destroy text on the top
        self.txt_result.destroy()
        self.txt_grade.destroy()
        self.txt_aver.destroy()

        ##Destroy all result slots
        for i in xrange(len(self.var_print)):
            if type(self.grade_print[i]) == str:
                pass
            else:
                self.grade_print[i].destroy()
                self.var_print[i].destroy()

        ##Destroy grade average result entry
        self.grade_aver.destroy()

        ##Disable reset button
        self.reset_result.config(state='disabled')
        
        ##Re-enable the calculate button
        self.cal.config(state='active')

        ##Reset third section
        self.grade_print = []
        self.var_print = []
        
root = Tk()
app = App(root)
root.title('Grade Calculator')
root.resizable(True, True)
root.mainloop()
