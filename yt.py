import webbrowser
import pyautogui as s
import time

youtube_url = "https://youtu.be/cx2mC18op-o?si=ispziVPI2_qcA9Hf"

webbrowser.open(youtube_url)
time.sleep(10)
s.click("space")