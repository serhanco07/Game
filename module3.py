from tkinter import *

def window():
    root = Toplevel()
    imagealien = PhotoImage(file="alien.gif")
    rightlabel = Label(root, image=imagealien)
    rightlabel.pack(side="right")

    our_text = """Who invited you here??It is time to have a fight!"""

    leftlabel = Label(root, 
                   justify=RIGHT,
                   text=our_text).pack(side="left")

    print("Loading ... ")
    root.mainloop() 

def theend():
    root = Toplevel()
    
    our_text = """BOOM! You won the battle and saved the world!
--------------------------------------------------------------                 THANK YOU FOR PLAYING!
                ░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░
                ░░░░█░░░░░░░░░░░░░█░░░░                 
                ░░░█░░░░░░░░░░▄▄▄░░█░░░
                ░░░█░░▄▄▄░░▄░░███░░█░░░
                ░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░
                ░░░█░░▀█▀█▀█▀█▀█▀░░█░░░
                ░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░
                ░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░
                ▄▀░▄▄▀▄▄▀▀▀▄▀▀▀▄▄▀▄▄░▀▄
                █░░░░▀▄░█▄░░░▄█░▄▀░░░░█
                ░▀▄▄░█░░█▄▄▄▄▄█░░█░▄▄▀░
                ░░░▀██▄▄███████▄▄██▀░░░
                ░░░████████▀████████░░░
                ░░▄▄█▀▀▀▀█░░░█▀▀▀▀█▄▄░░
                ░░▀▄▄▄▄▄▀▀░░░▀▀▄▄▄▄▄▀░﻿
 
--------------------------------------------------------------

                  """

    leftlabel = Label(root, 
                   justify=RIGHT,
                   text=our_text).pack(side="left")

    print("Loading... ")
    root.mainloop()
    
