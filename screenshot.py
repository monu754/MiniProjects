import time
import pyautogui
import random
import tkinter as tk


def screenshot():
    name = random.randint(1,1000000000)
    name = 'E:/Project/ScreenShot App/Screenshots/{}.jpg'.format(name)
        
    time.sleep(3)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)

frame.pack()

button = tk.Button(
    frame,
    text="Take screenshot",
    command=screenshot
)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="Quit",
    command=quit
)

close.pack(side=tk.LEFT)

root.mainloop()