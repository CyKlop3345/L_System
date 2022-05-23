from tkinter import *
import Logic

numIterat = 1
strStart = "F"
rules = ["F", "F+F-F-F+F"], ["", ""], ["", ""], ["", ""], ["", ""]
step = 600
turn = 90
pos = -300, 300
rot = 0
resize = 3

fontText='Times 15'

def start(canvas_0):
    global canvas, fill
    canvas = canvas_0
    fill = BooleanVar()
    fill.set(False)
    interface()

def create():
    numIterat = int(entryIterat.get())
    strStart = entryStrStart.get()
    rules = [[entryRuleFrom1.get(), entryRuleIn1.get()],
            [entryRuleFrom2.get(), entryRuleIn2.get()],
            [entryRuleFrom3.get(), entryRuleIn3.get()],
            [entryRuleFrom4.get(), entryRuleIn4.get()],
            [entryRuleFrom5.get(), entryRuleIn5.get()]]
    step = int(entryStep.get())
    turn = int(entryTurn.get())
    pos = int(entryPosX.get()), int(entryPosY.get())
    rot = int(entryRot.get())
    resize = float(entryResize.get())
    Logic.start(numIterat, strStart, rules, step, turn, fill.get(), pos, rot, resize)

def path():
    Logic.path()

def savePic():
    Logic.savePic()

def saveSettings():
    Logic.saveSettings()

def interface():
    global entryIterat, entryStrStart, entryRuleFrom1, entryRuleIn1, entryRuleFrom2, entryRuleIn2, entryRuleFrom3, entryRuleIn3,\
    entryRuleFrom4, entryRuleIn4, entryRuleFrom5, entryRuleIn5, entryStep, entryTurn, entryPosX, entryPosY, entryRot, entryResize

    labelIterat = Label(canvas, text="Num iteration:", font=fontText)
    entryIterat = Entry(canvas, width = 15)
    labelStrStart = Label(canvas, text="Start:", font=fontText)
    entryStrStart = Entry(canvas, width = 15)

    labelRule1 = Label(canvas, text="Rule 1:", font=fontText)
    entryRuleFrom1 = Entry(canvas, width = 15, )
    entryRuleIn1 = Entry(canvas, width = 15)
    labelRule2 = Label(canvas, text="Rule 2:", font=fontText)
    entryRuleFrom2 = Entry(canvas, width = 15)
    entryRuleIn2 = Entry(canvas, width = 15)
    labelRule3 = Label(canvas, text="Rule 3:", font=fontText)
    entryRuleFrom3 = Entry(canvas, width = 15)
    entryRuleIn3 = Entry(canvas, width = 15)
    labelRule4 = Label(canvas, text="Rule 4:", font=fontText)
    entryRuleFrom4 = Entry(canvas, width = 15)
    entryRuleIn4 = Entry(canvas, width = 15)
    labelRule5 = Label(canvas, text="Rule 5:", font=fontText)
    entryRuleFrom5 = Entry(canvas, width = 15)
    entryRuleIn5 = Entry(canvas, width = 15)

    labelStep = Label(canvas, text="Step:", font=fontText)
    entryStep = Entry(canvas, width = 15)
    labelTurn = Label(canvas, text="Turn:", font=fontText)
    entryTurn = Entry(canvas, width = 15)
    labelFill = Label(canvas, text="Fill:", font=fontText)
    checkFill = Checkbutton(canvas, variable = fill)
    labelPos = Label(canvas, text="Position:", font=fontText)
    entryPosX = Entry(canvas, width = 15)
    entryPosY = Entry(canvas, width = 15)
    labelRot = Label(canvas, text="Rotation:", font=fontText)
    entryRot = Entry(canvas, width = 15)
    labelResize = Label(canvas, text="Resize:", font=fontText)
    entryResize = Entry(canvas, width = 15)

    butStart = Button(canvas, width = 10, height = 1, command = create, text = "Start", font = fontText)
    butPath = Button(canvas, width = 10, height = 1, command=path, text="Path", font = fontText)
    butSave = Button(canvas, width = 10, height = 1, command = savePic, text = "Save", font = fontText)
    butSaveSettings = Button(canvas, width = 10, height = 1, command = saveSettings, text = "Save settings", font = fontText)

    entryIterat.insert(END, numIterat)
    entryStrStart.insert(END, strStart)
    entryRuleFrom1.insert(END, rules[0][0])
    entryRuleIn1.insert(END, rules[0][1])
    entryRuleFrom2.insert(END, rules[1][0])
    entryRuleIn2.insert(END, rules[1][1])
    entryRuleFrom3.insert(END, rules[2][0])
    entryRuleIn3.insert(END, rules[2][1])
    entryRuleFrom4.insert(END, rules[3][0])
    entryRuleIn4.insert(END, rules[3][1])
    entryRuleFrom5.insert(END, rules[4][0])
    entryRuleIn5.insert(END, rules[4][1])
    entryStep.insert(END, step)
    entryTurn.insert(END, turn)
    entryPosX.insert(END, pos[0])
    entryPosY.insert(END, pos[1])
    entryRot.insert(END, rot)
    entryResize.insert(END, resize)

    i = 0
    labelIterat.grid(column=0, row=i)
    entryIterat.grid(column=1, row=i)
    i += 1
    labelStrStart.grid(column=0, row=i)
    entryStrStart.grid(column=1, row=i)
    i += 1
    labelRule1.grid(column=0, row=i)
    entryRuleFrom1.grid(column=1, row=i)
    entryRuleIn1.grid(column=2, row=i)
    i += 1
    labelRule2.grid(column=0, row=i)
    entryRuleFrom2.grid(column=1, row=i)
    entryRuleIn2.grid(column=2, row=i)
    i += 1
    labelRule3.grid(column=0, row=i)
    entryRuleFrom3.grid(column=1, row=i)
    entryRuleIn3.grid(column=2, row=i)
    i += 1
    labelRule4.grid(column=0, row=i)
    entryRuleFrom4.grid(column=1, row=i)
    entryRuleIn4.grid(column=2, row=i)
    i += 1
    labelRule5.grid(column=0, row=i)
    entryRuleFrom5.grid(column=1, row=i)
    entryRuleIn5.grid(column=2, row=i)
    i += 1
    labelStep.grid(column=0, row=i)
    entryStep.grid(column=1, row=i)
    i += 1
    labelTurn.grid(column=0, row=i)
    entryTurn.grid(column=1, row=i)
    i += 1
    labelFill.grid(column=0, row=i)
    checkFill.grid(column=1, row=i)
    i += 1
    labelPos.grid(column=0, row=i)
    entryPosX.grid(column=1, row=i)
    entryPosY.grid(column=2, row=i)
    i += 1
    labelRot.grid(column=0, row=i)
    entryRot.grid(column=1, row=i)
    i += 1
    labelResize.grid(column=0, row=i)
    entryResize.grid(column=1, row=i)
    i += 1
    butStart.grid(column=0, row=i)
    i += 1
    butPath.grid(column=0, row=i)
    i += 1
    butSave.grid(column=0, row=i)
    butSaveSettings.grid(column=1, row=i)
