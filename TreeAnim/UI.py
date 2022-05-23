from tkinter import *
import Logic

numIterat = 60
posStart = 0, -350
step = 5
randStep = 3
turn = 20
randTurn = 10
sleepTime = 0.05

fontText='Times 15'

def start(canvas_0):
    global canvas, saving
    canvas = canvas_0
    saving = BooleanVar()
    saving.set(False)
    interface()

def create():
    numIterat = int(entryIterat.get())
    posStart = (int(entryPosStartX.get()), int(entryPosStartY.get()))
    step = int(entryStep.get())
    randStep = int(entryRandStep.get())
    turn = int(entryTurn.get())
    randTurn = int(entryRandTurn.get())
    sleepTime = float(entrySleepTime.get())
    Logic.start(numIterat, posStart, step, randStep, turn, randTurn, sleepTime, saving.get())

def path():
    Logic.path()

def savePic():
    Logic.savePic()

def saveSettings():
    Logic.saveSettings()

def interface():
    global entryIterat, entryPosStartX, entryPosStartY, entryStep, entryRandStep, entryTurn, entryRandTurn, entrySleepTime

    labelIterat = Label(canvas, text="Num iteration:", font=fontText)
    entryIterat = Entry(canvas, width = 15)
    labelPosStart = Label(canvas, text="Start pos:", font=fontText)
    entryPosStartX = Entry(canvas, width = 15)
    entryPosStartY = Entry(canvas, width = 15)
    labelStep = Label(canvas, text="Step:", font=fontText)
    entryStep = Entry(canvas, width = 15)
    labelRandStep = Label(canvas, text="Rand step:", font=fontText)
    entryRandStep = Entry(canvas, width = 15)
    labelTurn = Label(canvas, text="Turn:", font=fontText)
    entryTurn = Entry(canvas, width = 15)
    labelRandTurn = Label(canvas, text="Rand turn:", font=fontText)
    entryRandTurn = Entry(canvas, width = 15)
    labelSleepTime = Label(canvas, text="Sleep time:", font=fontText)
    entrySleepTime = Entry(canvas, width = 15)
    labelSave = Label(canvas, text="Saving:", font=fontText)
    checkSave = Checkbutton(canvas, variable = saving)

    butStart = Button(canvas, width = 10, height = 1, command = create, text = "Start", font = fontText)
    butPath = Button(canvas, width = 10, height = 1, command=path, text="Path", font = fontText)

    entryIterat.insert(END, numIterat)
    entryPosStartX.insert(END, posStart[0])
    entryPosStartY.insert(END, posStart[1])
    entryStep.insert(END, step)
    entryRandStep.insert(END, randStep)
    entryTurn.insert(END, turn)
    entryRandTurn.insert(END, randTurn)
    entrySleepTime.insert(END, sleepTime)

    i = 0
    labelIterat.grid(column=0, row=i)
    entryIterat.grid(column=1, row=i)
    i += 1
    labelPosStart.grid(column=0, row=i)
    entryPosStartX.grid(column=1, row=i)
    entryPosStartY.grid(column=2, row=i)
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
    labelSleepTime.grid(column=0, row=i)
    entrySleepTime.grid(column=1, row=i)
    i += 1
    labelSave.grid(column=0, row=i)
    checkSave.grid(column=1, row=i)
    i += 1
    butStart.grid(column=0, row=i)
    i += 1
    butPath.grid(column=0, row=i)
