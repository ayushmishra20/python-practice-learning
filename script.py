import pyautogui as s
import time

s.press("win")
time.sleep(1)

s.write("notepad", interval = 0.2)
s.press("enter")

time.sleep(1)

s.write("Hello World", interval= 0.2)
s.press("enter")

s.write("well done Ayush...", interval= 0.2)
s.press("enter")


s.write("This is created by scripting language...python", interval=0.2)
s.press("enter")
s.write("Pragya Mishra", interval= 0.2)


