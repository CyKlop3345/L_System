from tkinter import *
import turtle
from tkinter import filedialog
from PIL import ImageGrab
import subprocess
import os

def settings(canvas_0, turtle_0, screen_0):
    global canvas, turtle, screen, folderPath
    canvas = canvas_0
    turtle = turtle_0
    screen = screen_0
    folderPath = StringVar()

def start(numIterat_0, strStart_0, rules_0, step_0, turn_0, fill_0, pos_0, rot_0, resize_0):
    global stack, numIterat, strStart, rules, step, turn, fill, pos, rot
    stack = []
    numIterat = numIterat_0
    strStart = strStart_0
    rules = rules_0
    step = (step_0/(resize_0**numIterat_0))
    turn = turn_0
    fill = fill_0
    pos = pos_0
    rot = rot_0
    resize = resize_0

    str = transform()
    draw(str)

def transform():
    global strStart
    strTemp = ""
    str = strStart
    for i in range(numIterat):
        for char in str:
            if char == rules[0][0]:
                strTemp += rules[0][1]
            elif char == rules[1][0]:
                strTemp += rules[1][1]
            elif char == rules[2][0]:
                strTemp += rules[2][1]
            elif char == rules[3][0]:
                strTemp += rules[3][1]
            elif char == rules[4][0]:
                strTemp += rules[4][1]
            else:
                strTemp += char
        str = strTemp
        strTemp = ""
    return(str)

def draw(str):
    screen.tracer(False)
    screen.resetscreen()
    setSettings()

    if fill == True:
        turtle.begin_fill()

    for char in str:
        if char.isalpha() == True:
            if char.islower() == True:
                turtle.end_fill()
                turtle.up()
                turtle.forward(step)
                turtle.down()
                if fill == True:
                    turtle.begin_fill()
            else:
                turtle.forward(step)
        elif char == '+':
            turtle.right(turn)
        elif char == '-':
            turtle.left(turn)
        elif char == '[':
            stack.append(turtle.heading())
            stack.append(turtle.pos())
        elif char == ']':
            turtle.up()
            turtle.setpos(stack.pop())
            turtle.down()
            turtle.setheading(stack.pop())
        elif char == '^':
            turtle.up()
        elif char == '_':
            turtle.down()
        elif char.isnumeric() == True:
            print()
        else:
            turtle.forward(step)
    turtle.end_fill()
    screen.tracer(True)

def setSettings():
    turtle.hideturtle()
    turtle.color("Black")
    turtle.fillcolor("#6495ED")

    turtle.penup()
    turtle.setpos(pos)
    turtle.pendown()
    turtle.setheading(rot)

def path():
    global folderPath
    folderPath = StringVar()
    filename = filedialog.askdirectory()
    folderPath.set(filename)

def savePic(numIterat):
    global folderPath
    if folderPath.get() == "":
        path()
    curPath = os.getcwd()
    canvas.postscript(file = folderPath.get() + "\L_System.ps")
    cmd =   '"' + curPath + '\ImageMagick-7.1.0-4-portable-Q16-HDRI-x64\magick.exe" ' +\
            '"' + folderPath.get() + "\L_System.ps" + '" ' +\
            '"' + folderPath.get() + "\L_System_" + str(numIterat) + ".png" + '"'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    result = p.communicate()[0]

def saveSettings():
    global folderPath, strStart, rules, step, turn#, sizeBalance
    if folderPath.get() == "":
        path()
    txt = open(folderPath.get() + "\L_System_Set.txt", "w")
    txt.write(  "Start string: " + strStart + "\n" +
                "Rules: " + str(rules[0][0]) + "  -->  " + str(rules[0][1]) + "\n" +
                "          " + str(rules[1][0]) + "  -->  "  + str(rules[1][1]) + "\n" +
                "          " + str(rules[2][0]) + "  -->  "  + str(rules[2][1]) + "\n" +
                "          " + str(rules[3][0]) + "  -->  "  + str(rules[3][1]) + "\n" +
                "          " + str(rules[4][0]) + "  -->  "  + str(rules[4][1]) + "\n" +
                "Turn: " + str(turn) + "\n")# +
                # "Size Balance: " + str(sizeBalance))
    txt.close()
