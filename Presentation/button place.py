# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 22:07:16 2021

@author: 86136
"""

self.buttonMsg = Button(self.labelBottom,
                                text = "Send",
                                font = "Helvetica 10 bold", 
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton(self.entryMsg.get()))
self.buttonMsg.place(relx = 0.77,rely = 0.008,
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