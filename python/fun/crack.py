import keyboard
import time
import os

def hacktime():
    keyboard.write("google.fr", delay=0.01)
    keyboard.send('enter')

def brute(n):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    '''for i in range(len(ALPHABET)):
        for j in range(len(ALPHABET)):
            for k in range(len(ALPHABET)):
                print(ALPHABET[i]+ALPHABET[j]+ALPHABET[k])'''
    
    for i in range(len(ALPHABET) ** n):
        x = i % (len(ALPHABET) - 1)
        y = x % (len(ALPHABET) - 1)
        z = y % (len(ALPHABET) - 1)
        print(x, y, z)

'''while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
        hacktime()
    elif event.event_type == keyboard.KEY_DOWN and event.name == 'b':
        brute(3)
    elif event.event_type == keyboard.KEY_DOWN and event.name == 'e':
        exit()'''

brute(3)
##keyboard.unhook_all()b