from random import randrange
number = randrange(10)+1
print(number)
poop = input("Guess a number:")
if number == poop:
    print("pog")
elif number != poop:
    print ('not pog')
