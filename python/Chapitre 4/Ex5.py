import random

continuer = True
secret = random.randint(1, 100)
while continuer:
    guess = int(input("=> "))
    if(guess > secret):
        print("Trop Grand")
    elif(guess < secret):
        print("Trop petit")
    elif(guess == secret):
        print("Gagné")
        continuer = False