import math
import pyautogui
import random
import time
from tkinter import *

interval = math.floor((1/120)*1000)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
dvdtext = "DVD"

class DVD:
    def __init__(self):
        self.window = Tk()
        self.window.attributes('-topmost', True)
        self.window.eval('tk::PlaceWindow . center')
        self.window.overrideredirect(1)
        self.window.resizable(0,0)

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window_width = 100
        self.window_height = 100

        self.startx = random.randint(self.window_width, (self.screen_width - (self.window_width + 10)))
        self.starty = random.randint(self.window_height, (self.screen_height - (self.window_height + 10)))
        self.movex = self.movey = 5

        self.window.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.window.configure(bg="black")
        self.canvas = Canvas(self.window, width = self.window_width, height = self.window_height, bg = "black", highlightthickness = 0)
        self.text = self.canvas.create_text(50, 50, text=dvdtext, fill="purple", font=("Arial", 30, "bold"))
        self.canvas.place(x = self.startx, y = self.starty)

        self.mouse_position = pyautogui.position()

    def dvd(self):
        if self.startx <= 0 or self.startx + self.window_width >= self.screen_width:
            self.movex *= -1
            self.canvas.itemconfig(self.text, fill=colors[random.randint(0,len(colors)-1)])
        if self.starty <= 0 or self.starty + self.window_height >= self.screen_height:
            self.movey *= -1
            self.canvas.itemconfig(self.text, fill=colors[random.randint(0,len(colors)-1)])
        self.startx += self.movex
        self.starty += self.movey
        self.canvas.place(x = self.startx, y = self.starty)
        self.window.after(interval, self.dvd)

    def check_mouse_movement(self):
        current_pos = pyautogui.position()
        if current_pos != self.mouse_position:
            self.window.destroy()
        self.mouse_position = current_pos
        self.window.after(interval, self.check_mouse_movement)

    def run(self):
        self.check_mouse_movement()
        self.dvd()
        self.window.mainloop()

screensaver = DVD()
screensaver.run()

