from tkinter import *
import turtle
from tkinter import filedialog

import math
from random import randint
import time
from datetime import datetime

from PIL import ImageGrab
import subprocess
import os

numIterat = 70
posStart = 0, -350
step = 5
randStep = 3
turn = 20
randTurn = 10
sleepTime = 0.05
internodes = []

def settings(canvas_0, turtle_0, screen_0):
    global canvas, turtle, screen, folderPath, internodes
    canvas = canvas_0
    turtle = turtle_0
    screen = screen_0
    folderPath = StringVar()

def start(numIterat, posZero_0, stepMax_0, randStep_0, turn_0, randTurn_0, sleepTime, saving):
    global posZero, stepMax, randStep, turn, randTurn
    posZero = posZero_0
    stepMax = stepMax_0
    randStep = randStep_0
    turn = turn_0
    randTurn = randTurn_0
    internodes.clear()
    internode_0 = Internode_0()
    internodes.append(Internode(parent = internode_0, randTurn_0 = 0))
    for i in range(numIterat):
        for i in range(len(internodes)):
            internodes[i].growing()
        rewrite()
        draw()
        if saving == True:
            savePic()
        time.sleep(sleepTime)
        # savePic()

class Internode_0:
    def __init__(self):
        self.posEnd = posZero
        self.rot = 90
        self.stage = -1

class Internode():
    def __init__(self, parent, turn = 0, randTurn_0 = randTurn, step_0 = None, randStep_0 = randStep, stage = 0, thickness = 0.1):
        self.parent = parent
        self.posStart = parent.posEnd
        self.posEnd = self.posStart
        if stage == 0:
            self.rot = parent.rot + turn + randint(-randTurn_0, randTurn_0)
        else:
            self.rot = parent.rot
        if step_0 == None:
            self.stepMax = stepMax + randint(-randStep_0, randStep_0)
            self.step = 0
        else:
            self.stepMax = step_0
            self.step = step_0
        self.stage = stage
        if stage == 0:
            r = randint(0, 2)
            if r == 0:
                self.color = ("#008000")
            elif r == 1:
                self.color = ("#006040")
            else:
                self.color = ("#20C020")
        else:
            self.color = ("Black")
        self.thickness = thickness
        self.timeout = randint(10, 30)

    def growing(self):
        self.step += 1
        self.thickness += 0.15

        if self.step > self.stepMax:
            if self.stage == 0:
                self.stage = 1
                self.color = ("Black")
                internodes.append(Internode(self, turn = turn))
                internodes.append(Internode(self, turn = -turn))
            elif self.stage == 1:
                self.stage == 2



def rewrite():
    for i in range(len(internodes)):
        internodes[i].posStart = internodes[i].parent.posEnd
        internodes[i].posEnd = internodes[i].posStart[0] - (internodes[i].step * math.sin(math.radians(internodes[i].rot - 90))),\
                               internodes[i].posStart[1] + (internodes[i].step * math.cos(math.radians(internodes[i].rot - 90)))

def draw():
    global internodes

    screen.tracer(False)
    screen.resetscreen()
    setSettings()
    for i in range(len(internodes)):
        if internodes[i].stage == 0:
            turtle.pensize(6)
        else:
            turtle.pensize(internodes[i].thickness)
        turtle.color(internodes[i].color)
        turtle.penup()
        turtle.setpos(internodes[i].posStart)
        turtle.pendown()
        turtle.setheading(internodes[i].rot)
        turtle.forward(internodes[i].step)
    screen.tracer(True)

def setSettings():
    turtle.hideturtle()
    turtle.pencolor("Black")

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
