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
    imagealien = PhotoImage(file="ufo.gif")
    rightlabel = Label(root, image=imagealien)
    rightlabel.pack(side="right")

    print("Loading... ")
    root.mainloop()
    
def decision():
    answer2 = input("Do you want to fight the alien? ")
    if answer2 == 'yes' or answer2 == 'y' or answer2 == 'YES' or answer2 == 'Y' or answer2 == 'Yes':
        theend()
    else:
        print("---------Game Over!--------------")
