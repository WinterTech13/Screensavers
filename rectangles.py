import pyautogui
import random
from tkinter import *

COLOR_RECT = "#a562f9"
COLOR_TRANS = "#ffffff"
COLOR_BG = "#000000"
DELAY = 50
INTERVAL = 9
MAX_WINDOWS = 13
RECT_DIM_1 = 200
RECT_DIM_2 = 100
SPEED = 19

class Background(Tk):
    def __init__(self):
        super().__init__()
        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()
        self.overrideredirect(1)
        self.attributes("-topmost", True)
        self.geometry(f"{self.screenWidth}x{self.screenHeight}+0+0")
        self.configure(background = COLOR_BG)

class Rectangle:
    def __init__(self):
        self.window = Toplevel(root)
        self.window.overrideredirect(1)
        self.window.attributes("-topmost", True)
        self.window.attributes("-transparentcolor", COLOR_TRANS)

    def create(self):
        self.window.geometry(f"{self.width}x{self.height}+{self.startPosWidth}+{self.startPosHeight}")
        self.canvas = Canvas(
            self.window,
            width = self.width,
            height = self.height,
            highlightthickness = 0,
            background = COLOR_TRANS
        )
        self.canvas.pack(
            fill = BOTH,
            expand = True
        )
        self.canvas.create_rectangle(
            0,
            0,
            self.width,
            self.height,
            outline = COLOR_RECT,
            width = 4,
            fill = ""
        )

    def animate(self):
        self.startPosWidth += self.speedHorizontal
        self.startPosHeight += self.speedVertical
        self.window.geometry(f"{self.width}x{self.height}+{self.startPosWidth}+{self.startPosHeight}")
        outside = (
            self.startPosWidth + self.width < 0 or
            self.startPosWidth > root.screenWidth or
            self.startPosHeight + self.height < 0 or
            self.startPosHeight > root.screenHeight
        )
        if outside:
            self.window.destroy()
            return
        self.window.after(INTERVAL, self.animate)

class Up(Rectangle):
    def __init__(self):
        super().__init__()
        self.width = RECT_DIM_2
        self.height = RECT_DIM_1
        self.startPosWidth = random.randint(0, root.screenWidth - self.width)
        self.startPosHeight = -self.height
        self.speedHorizontal = 0
        self.speedVertical = SPEED
        self.create()

class Down(Rectangle):
    def __init__(self):
        super().__init__()
        self.width = RECT_DIM_2
        self.height = RECT_DIM_1
        self.startPosWidth = random.randint(0, root.screenWidth - self.width)
        self.startPosHeight = root.screenHeight
        self.speedHorizontal = 0
        self.speedVertical = -SPEED
        self.create()

class Right(Rectangle):
    def __init__(self):
        super().__init__()
        self.width = RECT_DIM_1
        self.height = RECT_DIM_2
        self.startPosWidth = -self.width
        self.startPosHeight = random.randint(0, root.screenHeight - self.height)
        self.speedHorizontal = SPEED
        self.speedVertical = 0
        self.create()

class Left(Rectangle):
    def __init__(self):
        super().__init__()
        self.width = RECT_DIM_1
        self.height = RECT_DIM_2
        self.startPosWidth = root.screenWidth
        self.startPosHeight = random.randint(0, root.screenHeight - self.height)
        self.speedHorizontal = -SPEED
        self.speedVertical = 0
        self.create()

class Mouse:
    def __init__(self):
        self.pos = pyautogui.position()
        self.currentPos = self.pos
        self.check()

    def check(self):
        self.currentPos = pyautogui.position()
        if self.currentPos != self.pos:
            root.destroy()
            return
        root.after(DELAY, self.check)

def createRectangle():
    if len(root.winfo_children()) < MAX_WINDOWS:
        direction = random.randint(1, 4)
        match direction:
            case 1:
                rect = Up()
            case 2:
                rect = Down()
            case 3:
                rect = Right()
            case 4:
                rect = Left()
        rect.animate()
    root.after(DELAY, createRectangle)

root = Background()
mouse = Mouse()
createRectangle()

root.mainloop()