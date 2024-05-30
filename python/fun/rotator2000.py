import keyboard
import time

def sendCommand(txt):
    time.sleep(0.1)
    keyboard.write(txt)
    keyboard.send("Enter")

keyboard.send('Windows+r')
sendCommand("cmd /k mode con: cols=15 lines=1")
sendCommand("cd %temp%")