from tkinter import *
import turtle
from tkinter import filedialog

from PIL import ImageGrab
import subprocess
import os

from random import randint

def settings(canvas_0, turtle_0, screen_0):
    global canvas, turtle, screen, folderPath
    canvas = canvas_0
    turtle = turtle_0
    screen = screen_0
    folderPath = StringVar()

def start(numIterat_0, strStart_0, rule_0, step_0, randStep_0, turn_0, randTurn_0, pos_0, rot_0):
    global stack, numIterat, strStart, rule, step, randStep, turn, randTurn, pos, rot
    stack = []
    numIterat = numIterat_0
    strStart = strStart_0
    rule = rule_0
    step = step_0
    randStep = randStep_0
    turn = turn_0
    randTurn = randTurn_0
    pos = pos_0
    rot = rot_0

    str = transform()
    draw(str)

def transform():
    global strStart
    level = 0
    strTemp = ""
    str = strStart
    for i in range(numIterat):
        for char in str:
            if char == "0":
                strTemp += rule
            elif char == "1":
                strTemp += "21"
            elif char == "2":
                if randint(0, 9) < 1 and level > 1:
                    strTemp += "[^30]"
                else:
                    strTemp += "2"
            elif char == "[":
                strTemp += char
                level += 1
            elif char == "]":
                strTemp += char
                level -= 1
            else:
                strTemp += char
        str = strTemp
        strTemp = ""
    return(str)

def draw(str):
    global thickness

    screen.tracer(False)
    screen.resetscreen()
    setSettings()

    for char in str:
        if char ==  "0":
            r = randint(0,2)
            if r == 0:
                turtle.color("#008000")
            elif r == 1:
                turtle.color("#006040")
            else:
                turtle.color("#20C020")
            turtle.pensize(4)
            turtle.forward(step + randint(-randStep, randStep))
            turtle.color("Black")
            turtle.pensize(thickness)
        elif char ==  "1":
            turtle.forward(step + randint(-randStep, randStep))
        elif char ==  "2":
            if randint(0, 9) > 2:
                turtle.forward(step + randint(-randStep, randStep))
        elif char == "3":
            turtle.forward(step + randint(-randStep, randStep))
        elif char == "+":
            turtle.right(turn + randint(-randTurn, randTurn))
        elif char == "-":
            turtle.left(turn + randint(-randTurn, randTurn))
        elif char == "[":
            stack.append(turtle.heading())
            stack.append(turtle.pos())
            stack.append(thickness)
            thickness -= 1
            turtle.pensize(thickness)
        elif char == "]":
            thickness = stack.pop()
            turtle.pensize(thickness)
            turtle.up()
            turtle.setpos(stack.pop())
            turtle.down()
            turtle.setheading(stack.pop())
        elif char == "^":
            if randint(1, 2) == 1:
                turtle.left(turn + randint(-randTurn, randTurn))
            else:
                turtle.right(turn + randint(-randTurn, randTurn))
        else:
            turtle.forward(step)
    screen.tracer(True)

def setSettings():
    global thickness
    turtle.hideturtle()
    turtle.color("Black")

    turtle.penup()
    turtle.setpos(pos)
    turtle.pendown()
    turtle.setheading(rot)

    thickness = numIterat
    turtle.pensize(thickness)

def path():
    global folderPath
    folderPath = StringVar()
    filename = filedialog.askdirectory()
    folderPath.set(filename)

def savePic():
    global folderPath
    if folderPath.get() == "":
        path()
    i = 1
    while os.path.exists(folderPath.get()  + "/L_System_" + str(i) + ".png"):
        i += 1
    curPath = os.getcwd()
    canvas.postscript(file = folderPath.get() + "\L_System.ps")
    cmd =   '"' + curPath + '\ImageMagick-7.1.0-4-portable-Q16-HDRI-x64\magick.exe" ' +\
            '"' + folderPath.get() + "\L_System.ps" + '" ' +\
            '"' + folderPath.get() + "\L_System_" + str(i) + ".png" + '"'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    result = p.communicate()[0]

def saveSettings():
    global folderPath, strStart, rule, step, turn#, sizeBalance
    if folderPath.get() == "":
        path()
    txt = open(folderPath.get() + "\L_System_Set.txt", "w")
    txt.write(  "Start string: " + strStart + "\n" +
                "Rule: " + "0" + "  -->  " + str(rule) + "\n" +
                "Step: " + str(step) + "\n" +
                "Rand step: " + str(randStep) + "\n" +
                "Turn: " + str(turn) + "\n" +
                "Rand turn: " + str(randTurn) + "\n")
    txt.close()
