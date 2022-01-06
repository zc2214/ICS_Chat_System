
def layout(self,name):
    self.connect = Button(self.labelBottom,
                          text = "Connect",
                          font = "Helvetica 6 bold", 
                          width = 20,
                          bg = "#ABB2B9",
                          command = lambda : self.showconnect())
def showconnect(self):
    if self.entryMsg.get()=='':
        self.my_msg= 'who'
    else:
        target=self.entryMsg.get()
        self.my_msg= 'c '+target
    self.entryMsg.delete(0, END)