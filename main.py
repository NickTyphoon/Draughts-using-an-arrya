from tkinter import *
from tkinter import  messagebox
import math


# constant
xclick = 700
yclick = 700
has_pressed = 0
p_turn = True

#__builtins__.print(xclick)
#[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
visual_board = [[0]*8]*8
print(visual_board)

def display_coordinates(event):

    my_label_pixelco["text"]=f"x={event.x}, y={event.y}"
    #print(f"x={event.x}")
    click_coords(event, xclick, yclick)

# Finds coords of the click

def click_coords(event, xclick, yclick):
    global has_pressed


    xclick = event.x
    yclick = event.y

    print("your x,y coords are: ",xclick,yclick)
    #x_decimal = xclick/100
    if xclick == 0:
        xclick = 100

    if yclick == 0:
        yclick = 100


    #pressed = PhotoImage(file="pressed.png")
    #window.create_image((xclick), (yclick), anchor=NW, image=pressed)

    xpos = int(math.ceil((xclick)/100))
    ypos = int(math.ceil((yclick)/100))
    print("your x,y squares are",xpos,",",ypos)
    intxpos = xpos
    intypos = ypos
    print(intypos)
    my_label["text"] = ((xpos),",",(ypos))
    has_pressed += 1
    add_piece(xpos, ypos,intypos,intxpos,visual_board)

# adds a piece selected position

def add_piece(xpos,ypos,intypos,intxpos,visual_board):
    array_x_coord = intxpos-1
    array_y_coord = intypos-1


    visual_board[array_y_coord][array_x_coord]=1
    print_grid(visual_board)

# prints the grid

def print_grid(visual_board):
    cur_location = 0
    for i in range (8):
        print(visual_board[cur_location])
        cur_location+=1

    pressed()

# Tkinter window setup

root = Tk()
root.title("mouse coords test")
window = Canvas(root,width=800,height=800,background="white")

img = PhotoImage(file="blueboard.gif")
window.create_image(0,0,anchor=NW,image=img)

window.bind("<Button-1>",display_coordinates)
my_label_pixelco=Label(bd=4,bg="white",fg="black")
my_label=Label(bd=4,bg="white",fg="black")

pressedcoordx = xclick
pressedcoordy = yclick

print("pressed coord y= ",pressedcoordy)
print("yclick =",yclick)

pressed_img = PhotoImage(file="pressed.gif")
window.create_image((500),(500),anchor=NW,image=pressed_img)

def pressed():
    global xclick, yclick
    if has_pressed != 0:
        window.create_image((xclick), (yclick), anchor=NW, image=pressed_img)


# positions in window
window.grid(row=0,column=0)
my_label_pixelco.grid(row=1,column=0)
my_label.grid(row=2,column=0)

root.mainloop()
