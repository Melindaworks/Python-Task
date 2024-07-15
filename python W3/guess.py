import random
selectnumber = random.randint(1, 100)

print("Try to guess the number between 1 to 100.")
while True:
    guess = int(input("Enter your guess: "))

    if guess > selectnumber:
        print("Too high!")
    elif guess < selectnumber:
        print("Too low!")
    else:
        print("Congratulations! You guessed it!")
        break 
