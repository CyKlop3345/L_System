from tkinter import *
import Logic

numIterat = 11
strStart = "2222220"
rule = "1[-0][+0]"
step = 10
randStep = 5
turn = 20
randTurn = 10
pos = 0, -350
rot = 90

fontText='Times 15'

def start(canvas_0):
    global canvas
    canvas = canvas_0
    interface()

def create():
    numIterat = int(entryIterat.get())
    strStart = entryStrStart.get()
    rule = entryRule.get()
    step = int(entryStep.get())
    randStep = int(entryRandStep.get())
    turn = int(entryTurn.get())
    randTurn = int(entryRandTurn.get())
    Logic.start(numIterat, strStart, rule, step, randStep, turn, randTurn, pos, rot)

def path():
    Logic.path()

def savePic():
    Logic.savePic()

def saveSettings():
    Logic.saveSettings()

def interface():
    global entryIterat, entryStrStart, entryRule, entryStep, entryRandStep, entryTurn, entryRandTurn

    labelIterat = Label(canvas, text="Num iteration:", font=fontText)
    entryIterat = Entry(canvas, width = 15)
    labelStrStart = Label(canvas, text="Start:", font=fontText)
    entryStrStart = Entry(canvas, width = 15)
    labelRule = Label(canvas, text="Rule:", font=fontText)
    entryRule = Entry(canvas, width = 15, )
    labelStep = Label(canvas, text="Step:", font=fontText)
    entryStep = Entry(canvas, width = 15)
    labelRandStep = Label(canvas, text="Rand step:", font=fontText)
    entryRandStep = Entry(canvas, width = 15)
    labelTurn = Label(canvas, text="Turn:", font=fontText)
    entryTurn = Entry(canvas, width = 15)
    labelRandTurn = Label(canvas, text="Rand turn:", font=fontText)
    entryRandTurn = Entry(canvas, width = 15)

    butStart = Button(canvas, width = 10, height = 1, command = create, text = "Start", font = fontText)
    butPath = Button(canvas, width = 10, height = 1, command=path, text="Path", font = fontText)
    butSave = Button(canvas, width = 10, height = 1, command = savePic, text = "Save", font = fontText)
    butSaveSettings = Button(canvas, width = 10, height = 1, command = saveSettings, text = "Save settings", font = fontText)

    entryIterat.insert(END, numIterat)
    entryStrStart.insert(END, strStart)
    entryRule.insert(END, rule)
    entryStep.insert(END, step)
    entryRandStep.insert(END, randStep)
    entryTurn.insert(END, turn)
    entryRandTurn.insert(END, randTurn)

    i = 0
    labelIterat.grid(column=0, row=i)
    entryIterat.grid(column=1, row=i)
    i += 1
    labelStrStart.grid(column=0, row=i)
    entryStrStart.grid(column=1, row=i)
    i += 1
    labelRule.grid(column=0, row=i)
    entryRule.grid(column=1, row=i)
    i += 1
    labelStep.grid(column=0, row=i)
    entryStep.grid(column=1, row=i)
    i += 1
    labelRandStep.grid(column=0, row=i)
    entryRandStep.grid(column=1, row=i)
    i += 1
    labelTurn.grid(column=0, row=i)
    entryTurn.grid(column=1, row=i)
    i += 1
    labelRandTurn.grid(column=0, row=i)
    entryRandTurn.grid(column=1, row=i)
    i += 1
    butStart.grid(column=0, row=i)
    i += 1
    butPath.grid(column=0, row=i)
    i += 1
    butSave.grid(column=0, row=i)
    butSaveSettings.grid(column=1, row=i)
