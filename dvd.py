import pyautogui
import random
from tkinter import *

INTERVAL = 9
DELAY = 50
COLORS = ["#ff0000", "#ffa500", "#ffff00", "#00ff00", "#0000ff", "#800080"]
COLOR_BG = "#000000"
DVD_STRING = "DVD"
RECT_DIM_W = 100
RECT_DIM_H = 40
SPEED = 3

class Background(Tk):
    def __init__(self):
        super().__init__()
        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()
        self.overrideredirect(1)
        # self.attributes("-topmost", True)
        self.geometry(f"{self.screenWidth}x{self.screenHeight}+0+0")
        self.configure(background = COLOR_BG)

class DVD:
    def __init__(self):
        self.window = Toplevel(root)
        self.window.overrideredirect(1)
        self.window.attributes("-topmost", True)

        self.width = RECT_DIM_W
        self.height = RECT_DIM_H
        self.speedHorizontal = SPEED * random.choice([-1, 1])
        self.speedVertical = SPEED * random.choice([-1, 1])
        self.posWidth = random.randint(0, root.screenWidth - self.width)
        self.posHeight = random.randint(0, root.screenHeight - self.height)
        self.create()

    def create(self):
        self.window.geometry(f"{self.width}x{self.height}+{self.posWidth}+{self.posHeight}")
        self.canvas = Canvas(
            self.window,
            width = self.width,
            height = self.height,
            highlightthickness = 0,
            background = COLOR_BG
        )
        self.canvas.pack(
            fill = BOTH,
            expand = True
        )
        self.text = self.canvas.create_text(
            self.width / 2,
            self.height / 2,
            text = DVD_STRING,
            font = ("Arial", 30),
            fill = random.choice(COLORS)
        )
        self.animate()

    def animate(self):
        self.posWidth += self.speedHorizontal
        self.posHeight += self.speedVertical
        self.window.geometry(f"{self.width}x{self.height}+{self.posWidth}+{self.posHeight}")

        if self.posWidth < 0 or self.posWidth > root.screenWidth - self.width:
            self.color(self.text)
            self.speedHorizontal *= -1
        if self.posHeight < 0 or self.posHeight > root.screenHeight - self.height:
            self.color(self.text)
            self.speedVertical *= -1

        self.window.after(INTERVAL, self.animate)

    def color(self, id):
        self.canvas.itemconfig(
            id,
            fill = random.choice(COLORS)
        )

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

root = Background()
pyautogui.moveTo(root.screenWidth - 1, root.screenHeight - 1)
mouse = Mouse()
DVD()

root.mainloop()