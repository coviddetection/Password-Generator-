import random
import os

from tkinter import *
from tk import *
from tkinter import Frame
from tkinter import ttk



class Application(Frame):


     def createWidgets(self):
         self.QUIT = Button(self)
         self.QUIT["text"] = "QUIT"
         self.QUIT["fg"]   = "red"
         self.QUIT["command"] =  self.quit

         self.QUIT.pack({"side": "left"})

         self.hi_there1 = Button(self)
         self.hi_there1["text"] = "Generate Random Password" 
         self.hi_there1["command"] = self.q
  
         
         self.hi_there1.pack({"side": "left"})

  
         
        

         

    


     def __init__(self, master=None):
            Frame.__init__(self, master)
            self.pack()
            self.createWidgets()





 

     def q(self):
         letters="esvdfsghfghghkjyhkuyıyuywewqwq1234567890*-<>,.feggdfdfabcdefghijklmnoprstuvyz"
         lenght=20
         amount=3
         for x in range(amount):
             password="".join(random.sample(letters,lenght))
             print(password)
         

         

root = Tk()
root.title("Random password generator ")
app = Application(master=root)       
app.mainloop()
root.destroy()

