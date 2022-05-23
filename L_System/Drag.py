# python DragScreen.py
import turtle

# Get canvas (and others)
def start(canvas_0):
    global canvas
    canvas = canvas_0
    canvas.bind("<Button-1>", on_click)
    canvas.bind("<B1-Motion>", on_drag)

old_x = 0
old_y = 0

# Move all elements
def move(offset_x, offset_y):
    for element_id in canvas.find_all():
        canvas.move(element_id, offset_x, offset_y,)

# Get mouse old position
def on_click(event):
    global old_x, old_y
    old_x = event.x
    old_y = event.y

# Get mouse current position
def on_drag(event):
    global old_x, old_y
    move(event.x-old_x, event.y-old_y)
    old_x = event.x
    old_y = event.y
