from tkinter import *
from turtle import Turtle, Screen, RawTurtle
import UI, Logic

bgColor = "gray60"

def main():
    root = Tk()
    root.title("Ку!")
    root.resizable(width=False, height=False)
    canvasUI = Canvas(root, height=500, width=500, highlightthickness=0, bg=bgColor)
    canvasUI.grid(sticky=N+E+S+W, column=0, row=0)
    canvasTurtle = Canvas(root, height=750, width=750)
    canvasTurtle.grid(column=1, row=0, rowspan=2)
    turtle = RawTurtle(canvasTurtle)
    screen = turtle.getscreen()

    labelBy = Label(root, text="By: CyKlop3345", font="Times 15", bg="#EC5700", fg="White", width=15, height=1)
    labelBy.grid(sticky=E+S+W, column=0, row=1)

    Logic.settings(canvasTurtle, turtle, screen)
    UI.start(canvasUI)

    root.mainloop()

if __name__ == "__main__":
    main()
