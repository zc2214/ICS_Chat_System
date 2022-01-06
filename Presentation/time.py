
import time

def layout(self,name):
    self.time = Button(self.labelBottom,
                       text = "Time",
                       font = "Helvetica 6 bold", 
                       width = 20,
                       bg = "#ABB2B9",
                       command = lambda :  self.showtime())
def showtime(self):
    self.textCons.config(state = NORMAL),
    self.textCons.insert(END,'Time: '+time.strftime('%d.%m.%y,%H:%M', time.localtime())+'\n\n'),    
    self.textCons.config(state = DISABLED)
    self.textCons.see(END)