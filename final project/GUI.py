#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 13:36:58 2021

@author: bing
"""

# import all the required  modules

import json
# file related
import os
import select
# import all the required  modules
import threading
from ftplib import FTP
from pathlib import Path
from tkinter import *
import file_opener
from chat_utils import *
import pdf_processor

# GUI class for the chat
def ftpconnect(host='localhost', port=8888, username="Admin", password="Admin"):
    ftp = FTP()
    ftp.connect(host, port)  # Connect the FTP server
    ftp.login(username, password)  # Log in
    return ftp


# pathlib is good for processing file path, strongly encouraged to learn
def download(path=str(Path(__file__).parent / 'user_files' / 'user1')):
    """all files on server are stored in path folder"""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    ftp = ftpconnect()
    for filename in ftp.nlst():
        with open(path / filename, "wb") as f:
            ftp.retrbinary('RETR %s' % filename, f.write)
    ftp.quit()


def upload(path=None):
    ftp = ftpconnect()
    if path is None:
        path = file_opener.file_opener()
    with open(path, 'rb') as contents:
        ftp.storbinary('STOR %s' % os.path.basename(path), contents)
    ftp.quit()
def startgame():
    os.system("gamerunner.py")
class GUI:
    # constructor method
    def __init__(self, send, recv, sm, s):
        # chat window which is currently hidden
        self.Window = Tk()
        self.Window.withdraw()
        self.send = send
        self.recv = recv
        self.sm = sm
        self.socket = s
        self.my_msg = ""
        self.system_msg = ""

    def login(self):
        # login window
        self.login = Toplevel()
        # set the title
        self.login.title("Login")
        self.login.resizable(width = False, 
                             height = False)
        self.login.configure(width = 400,
                             height = 300)
        # create a Label
        self.pls = Label(self.login, 
                       text = "Please login to continue",
                       justify = CENTER, 
                       font = "Helvetica 14 bold")
          
        self.pls.place(relheight = 0.15,
                       relx = 0.2, 
                       rely = 0.07)
        # create a Label
        self.labelName = Label(self.login,
                               text = "Name: ",
                               font = "Helvetica 12")
          
        self.labelName.place(relheight = 0.2,
                             relx = 0.1, 
                             rely = 0.2)
          
        # create a entry box for 
        # tyoing the message
        self.entryName = Entry(self.login, 
                             font = "Helvetica 14")
          
        self.entryName.place(relwidth = 0.4, 
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.2)
          
        # set the focus of the curser
        self.entryName.focus()
          
        # create a Continue Button 
        # along with action
        self.go = Button(self.login,
                         text = "CONTINUE", 
                         font = "Helvetica 14 bold", 
                         command = lambda: self.goAhead(self.entryName.get()))
          
        self.go.place(relx = 0.4,
                      rely = 0.55)
        self.Window.mainloop()
  
    def goAhead(self, name):
        self.user_name=name
        if len(name) > 0:
            msg = json.dumps({"action":"login", "name": name})
            self.send(msg)
            response = json.loads(self.recv())
            if response["status"] == 'ok':
                self.login.destroy()
                self.sm.set_state(S_LOGGEDIN)
                self.sm.set_myname(name)
                self.layout(name)
                self.textCons.config(state = NORMAL)
                # self.textCons.insert(END, "hello" +"\n\n")   
                self.textCons.insert(END, menu +"\n\n")      
                self.textCons.config(state = DISABLED)
                self.textCons.see(END)
                # while True:
                #     self.proc()
        # the thread to receive messages
            process = threading.Thread(target=self.proc)
            process.daemon = True
            process.start()
  
    # The main layout of the chat
    def layout(self,name):
        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width = False,
                              height = False)
        self.Window.configure(width = 470,
                              height = 550,
                              bg = "#17202A")
        self.labelHead = Label(self.Window,
                             bg = "#17202A", 
                              fg = "#EAECEE",
                              text = self.name ,
                               font = "Helvetica 13 bold",
                               pady = 5)
          
        self.labelHead.place(relwidth = 1)
        self.line = Label(self.Window,
                          width = 450,
                          bg = "#ABB2B9")
          
        self.line.place(relwidth = 1,
                        rely = 0.07,
                        relheight = 0.012)
          
        self.textCons = Text(self.Window,
                             width = 20, 
                             height = 2,
                             bg = "#17202A",
                             fg = "#EAECEE",
                             font = "Helvetica 14", 
                             padx = 5,
                             pady = 5)
          
        self.textCons.place(relheight = 0.745,
                            relwidth = 1, 
                            rely = 0.08)
          
        self.labelBottom = Label(self.Window,
                                 bg = "#ABB2B9",
                                 height = 80)
          
        self.labelBottom.place(relwidth = 1,
                               rely = 0.825)
          
        self.entryMsg = Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")
          
        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth = 0.45,
                            relheight = 0.06,
                            rely = 0.008,
                            relx = 0.111)
        def playgame():
            startgame()
        
        self.gamebutton = Button(self.labelBottom,
                                text = "Game",
                                font = "Helvetica 6 bold", 
                                width = 20,
                                bg = "#ABB2B9",
                                command =playgame)
        # place the given widget
        # into the gui window
        self.gamebutton.place(relwidth = 0.08,
                            relheight = 0.06,
                            rely = 0.008,
                            relx = 0.011)
          
        self.entryMsg.focus()
        
        def uploading():
            upload()
            self.textCons.config(state = NORMAL),
            self.textCons.insert(END,self.user_name+' is uploading!'+'\n\n'),    
            self.textCons.config(state = DISABLED)
            self.textCons.see(END)
            self.my_msg=' '+self.user_name+' is uploading!'+'\n\n'

            
            
        
        def download_for_current_user():
            current_path = str(Path(__file__).parent / 'user_files' / self.user_name)
            download(current_path)
            pdf_processor.main(current_path)
            self.textCons.config(state = NORMAL),
            self.textCons.insert(END,self.user_name+' is downloading!'+'\n\n'),    
            self.textCons.config(state = DISABLED)
            self.textCons.see(END)
            self.my_msg=' '+self.user_name+' is downloading!'+'\n\n'

            
          
        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text = "Send",
                                font = "Helvetica 10 bold", 
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton(self.entryMsg.get()))
          
        self.buttonMsg.place(relx = 0.77,
                             rely = 0.008,
                             relheight = 0.024, 
                             relwidth = 0.22)

        self.upload = Button(self.labelBottom,
                                text = "Upload",
                                font = "Helvetica 6 bold", 
                                width = 20,
                                bg = "#ABB2B9",
                                command=uploading)
          
        self.upload.place(relx = 0.77,
                             rely = 0.038,
                             relheight = 0.024, 
                             relwidth = 0.10)
        self.download = Button(self.labelBottom,
                                text = "Download",
                                font = "Helvetica 6 bold", 
                                width = 20,
                                bg = "#ABB2B9",
                                command=download_for_current_user)
          
        self.download.place(relx = 0.88,
                             rely = 0.038,
                             relheight = 0.024, 
                             relwidth = 0.10)
        
        self.time = Button(self.labelBottom,
                                text = "Time",
                                font = "Helvetica 6 bold", 
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda :  self.showtime())
                                        
        self.time.place(relx = 0.6,
                             rely = 0.008,
                             relheight = 0.016, 
                             relwidth = 0.15)
        
        self.connect = Button(self.labelBottom,
                                text = "Connect",
                                font = "Helvetica 6 bold", 
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.showconnect())
          
        self.connect.place(relx = 0.6,
                             rely = 0.026,
                             relheight = 0.016, 
                             relwidth = 0.15)
        
        self.leave = Button(self.labelBottom,
                                text = "Leave",
                                font = "Helvetica 6 bold", 
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton('bye'))
        self.leave.place(relx = 0.6,
                             rely = 0.044,
                             relheight = 0.016, 
                             relwidth = 0.15)
        
          
        self.textCons.config(cursor = "arrow")
          
        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
          
        # place the scroll bar 
        # into the gui window
        scrollbar.place(relheight = 1,
                        relx = 0.974)
          
        scrollbar.config(command = self.textCons.yview)
          
        self.textCons.config(state = DISABLED)
  
    # function to basically start the thread for sending messages
    def sendButton(self, msg):
        self.textCons.config(state = DISABLED)
        self.my_msg = msg
        # print(msg)
        self.entryMsg.delete(0, END)
        
    def showtime(self):
        self.textCons.config(state = NORMAL),
        self.textCons.insert(END,'Time: '+time.strftime('%d.%m.%y,%H:%M', time.localtime())+'\n\n'),    
        self.textCons.config(state = DISABLED)
        self.textCons.see(END)
   
    def showconnect(self):
        if self.entryMsg.get()=='':
            self.my_msg= 'who'
        else:
            target=self.entryMsg.get()
            self.my_msg= 'c '+target
        self.entryMsg.delete(0, END)
        
    def showupload(self):
        self.textCons.config(state = NORMAL),
        self.textCons.insert(END,'uploading!'+'\n\n'),    
        self.textCons.config(state = DISABLED)
        self.textCons.see(END)
        
    def showdownload(self):
        self.textCons.config(state = NORMAL),
        self.textCons.insert(END,'downloading!'+'\n\n'),    
        self.textCons.config(state = DISABLED)
        self.textCons.see(END)

    def proc(self):
        # print(self.msg)
        while True:
            read, write, error = select.select([self.socket], [], [], 0)
            peer_msg = []
            # print(self.msg)
            if self.socket in read:
                peer_msg = self.recv()
            if len(self.my_msg) > 0 or len(peer_msg) > 0:
                # print(self.system_msg)
                self.system_msg += self.sm.proc(self.my_msg, peer_msg)
                self.my_msg = ""
                self.textCons.config(state = NORMAL)
                self.textCons.insert(END, self.system_msg +'\n\n')      
                self.textCons.config(state = DISABLED)
                self.system_msg=''
                self.textCons.see(END)
                
                

    def run(self):
        self.login()
        

# create a GUI class object
if __name__ == "__main__": 
    g = GUI()
