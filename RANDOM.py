#importing the random libiary
import random

#Generate is the number which this program generates randomly
Generate = random.randrange(21)

#Guess, this is the number which the user has to input has his/her guess
Guess = int(input('Guess the number :'))
if Generate is Guess:
    print('You guessed the correct number')
if Guess < Generate :
    print('Wow!!!, your guess is too low')
elif Guess > Generate :
    print('Bravo, you guessed too high')
