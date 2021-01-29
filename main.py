from tkinter import *
from tkinter import  messagebox
import math


#__builtins__.print(xclick)

visual_board = [[[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]],
                [[],[],[],[],[],[],[],[]]
                ]
print(visual_board)


def display_coordinates(event):

    my_label["text"]=f"x={event.x}, y={event.y}"
    #print(f"x={event.x}")
    click_coords(event)



def click_coords(event):

    xclick = event.x
    yclick = event.y
    print("your x.y coords are: ",xclick,yclick)
    #x_decimal = xclick/100
    if xclick == 0:
        xclick = 100

    if yclick == 0:
        yclick = 100

    xpos = int(math.ceil((xclick)/100))
    ypos = int(math.ceil((yclick)/100))
    print("your x,y squares are",xpos,",",ypos)
    intxpos = xpos
    intypos = ypos
    print(intypos)
    add_piece(xpos, ypos,intypos,intxpos)


def add_piece(xpos,ypos,intypos,intxpos):
    global visual_board
    #visual_board.insert((intxpos,intypos),(8))
    #print("hello")
    #[(intxpos),(intypos)]

    visual_board = {intxpos:1,intxpos:1}
    print(visual_board)






root = Tk()
root.title("mouse coords test")
window = Canvas(root,width=800,height=800,background="white")
img = PhotoImage(file="blueboard.gif")
window.create_image(0,0,anchor=NW,image=img)
window.bind("<Button-1>",display_coordinates)
my_label=Label(bd=4,bg="white",fg="black")

window.grid(row=0,column=0)
my_label.grid(row=0,column=1)

root.mainloop()