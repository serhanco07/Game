import turtle
def star():
    t = turtle.Pen()
    t.color('blue','yellow')


    #draw a star

    t.begin_fill()
    count = 0

    for x in range(1,9):
        t.forward(300)
        t.left(225)
        count = count+1
        print("Loading : " + str(count))
                
    t.end_fill()
    print("This is the star we are entering!")
