import module1, module2, module3
from tkinter import *
module1.intro()
answer = input("Do you want to enter the star? ")
if answer == 'yes' or 'y':
    module2.star()
    module1.enter()
    module3.window()
    module3.theend()
else:
    print("---------Game Over!--------------")
