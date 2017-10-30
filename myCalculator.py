## need to clear entrybox before another calculation is carried out!!!!!!!
from tkinter import *

class Calculator(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master,height=60, width=60)
        self.grid()


        self.Entry=Entry(master,width=40)
        self.Entry.grid(row =0 , columnspan = 4,ipady=10)
        self.B_1= Button(master,text ='1', command = lambda:self.Entry.insert(END,1),height=2, width=6,relief= RAISED).grid(row =1 , column = 0)
        self.B_2= Button(master,text ='2', command = lambda:self.Entry.insert(END,2),height=2, width=6,relief= RAISED).grid(row =1 , column = 1)
        self.B_3= Button(master,text ='3', command = lambda:self.Entry.insert(END,3),height=2, width=6,relief= RAISED).grid(row =1 , column = 2)
        self.B_4= Button(master,text ='4', command = lambda:self.Entry.insert(END,4),height=2, width=6,relief= RAISED).grid(row =2 , column = 0)
        self.B_5= Button(master,text ='5', command = lambda:self.Entry.insert(END,5),height=2, width=6,relief= RAISED).grid(row =2 , column = 1)
        self.B_6= Button(master,text ='6', command = lambda:self.Entry.insert(END,6),height=2, width=6,relief= RAISED).grid(row =2 , column = 2)
        self.B_7= Button(master,text ='7', command = lambda:self.Entry.insert(END,7),height=2, width=6,relief= RAISED).grid(row =3 , column = 0)
        self.B_8= Button(master,text ='8', command = lambda:self.Entry.insert(END,8),height=2, width=6,relief= RAISED).grid(row =3 , column = 1)
        self.B_9= Button(master,text ='9', command = lambda:self.Entry.insert(END,9),height=2, width=6,relief= RAISED).grid(row =3 , column = 2)
        self.B_add= Button(master,text ='+', command = lambda:self.Entry.insert(END,'+'),height=2, width=6,relief= RAISED).grid(row =5 , column = 1)
        self.B_o= Button(master,text ='0', command = lambda:self.Entry.insert(END,'0'),height=2, width=6,relief= RAISED).grid(row =4 , column = 0)
        self.B_equals= Button(master,text = '=', command = self.solve,height=2, width=8,relief= RAISED).grid(row =5 , column = 3)
        self.B_percent= Button(master,text = '%', command=lambda:self.Entry.insert(END,'%'),height=2, width=6,relief= RAISED).grid(row =5 , column = 0)
        self.B_minus= Button(master,text ='-', command = lambda:self.Entry.insert(END,'-'),height=2, width=6,relief= RAISED).grid(row =3 , column = 3)
        self.B_multiply= Button(master,text ='*', command = lambda:self.Entry.insert(END,'*'),height=2, width=6,relief= RAISED).grid(row =4 , column = 3)
        self.B_divide= Button(master,text ='/', command =lambda:self.Entry.insert(END,'/'),height=2, width=6,relief= RAISED).grid(row= 4 , column = 2)
        self.B_comma= Button(master,text ='.', command =lambda:self.Entry.insert(END,'.'),height=2, width=6,relief= RAISED).grid(row= 4 , column = 1)
        self.B_clear= Button(master,text ='CE', command =self.clear,height=2, width=6,relief= RAISED).grid(row= 1 , column = 3)
        self.B_undo= Button(master,text ='AC', command =self.undo,height=2, width=6,relief= RAISED).grid(row= 2 , column = 3)
        self.B_square= Button(master,text ='x^2', command =self.square,height=2, width=6,relief= RAISED).grid(row= 5 , column = 2)

       
    def solve(self):
        try:
            result = eval(self.Entry.get())
            self.Entry.delete(0,END)
       
            self.Entry.insert(END,result)
        except:
            self.Entry.delete(0,END)
            self.Entry.insert(END,'Error')
            
        return

    def clear(self):
        self.Entry.delete(0,END)
        return

    def undo(self):
        try:

            result_1 = list(self.Entry.get())
            result_1.pop()
            self.Entry.delete(0,END)
            result_1 ="".join(result_1)
            self.Entry.insert(END,result_1)

        except:
            self.Entry.delete(0,END)
            self.Entry.insert(END,'NO NUMBERS FOUND')
            
       
    def square(self):
        try:
           result_2 = eval(self.Entry.get())
           result_2 = result_2 * result_2 
           self.Entry.delete(0,END)
           self.Entry.insert(END,result_2)
           
        except:
           self.Entry.delete(0,END)
           self.Entry.insert(END,'INVALID INPUT')


    
    
            


if __name__== "__main__":
    Calculator().mainloop()
        
