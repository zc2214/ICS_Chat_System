
def layout(self,name):
    self.leave = Button(self.labelBottom,
                        text = "Leave",
                        font = "Helvetica 6 bold", 
                        width = 20,
                        bg = "#ABB2B9",
                        command = lambda : self.sendButton('bye'))
