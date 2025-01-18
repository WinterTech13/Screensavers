import math
import pyautogui
import random
import sys
import time
from tkinter import *

root = Tk()

max_windows = 13
speed = 19
interval = math.ceil((1/120)*1000)
spawn_delay = 250
mouse_position = pyautogui.position()

class Rectangle:
    def __init__(self, root):
        self.root = root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.window = Toplevel(root)
        self.window.overrideredirect(1)
        self.window.attributes('-topmost', True)
        self.window.attributes('-transparentcolor', 'white')
        self.create()

    def create(self):
        self.direction = random.randint(1, 4)
        if self.direction in [1, 2]:
            self.width = 200
            self.height = 100
        else:
            self.width = 100
            self.height = 200

        if self.direction == 1:
            self.startw = -self.width
            self.endw = self.screen_width
            self.starth = self.endh = random.randint(0, self.screen_height - self.height)
            self.w = speed
            self.h = 0
        elif self.direction == 2:
            self.startw = self.screen_width
            self.endw = -self.width
            self.starth = self.endh = random.randint(0, self.screen_height - self.height)
            self.w = -speed
            self.h = 0
        elif self.direction == 3:
            self.startw = self.endw = random.randint(0, self.screen_width - self.width)
            self.starth = -self.height
            self.endh = self.screen_height
            self.w = 0
            self.h = speed
        else:
            self.startw = self.endw = random.randint(0, self.screen_width - self.width)
            self.starth = self.screen_height
            self.endh = -self.height
            self.w = 0
            self.h = -speed

        self.window.geometry(f"{self.width}x{self.height}+{int(self.startw)}+{int(self.starth)}")
        self.canvas = Canvas(self.window, width=self.width, height=self.height, highlightthickness=0, bg='white')
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.create_rectangle(0, 0, self.width-4, self.height-4, outline='#a562f9', width=4, fill='')

    def animate(self):
        if ((self.direction in [1, 2] and ((self.w >= 0 and self.startw <= self.endw) or (self.w <= 0 and self.startw >= self.endw))) or
            (self.direction in [3, 4] and ((self.h >= 0 and self.starth <= self.endh) or (self.h <= 0 and self.starth >= self.endh)))):
            self.startw += self.w
            self.starth += self.h
            self.window.geometry(f"{self.width}x{self.height}+{int(self.startw)}+{int(self.starth)}")
            self.window.after(interval, self.animate)
        else:
            self.window.destroy()
            create_rectangle(self.root)

def create_background(root):
    bg_window = Toplevel(root)
    bg_window.overrideredirect(1)
    bg_window.attributes('-topmost', True)
    bg_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    bg_window.configure(bg='black')
    return bg_window

def create_rectangle(root):
    if len(root.winfo_children()) < max_windows + 1:
        rect = Rectangle(root)
        rect.animate()
        root.after(spawn_delay, lambda: create_rectangle(root))
    root.after(100, check_mouse_movement)

def check_mouse_movement():
    global mouse_position
    current_pos = pyautogui.position()
    if current_pos != mouse_position:
        bg_window.destroy()
        sys.exit()
    mouse_position = current_pos
    root.after(100, check_mouse_movement)

root.withdraw()
bg_window = create_background(root)
create_rectangle(root)
check_mouse_movement()

root.mainloop()
