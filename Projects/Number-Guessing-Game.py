import random
num = random.randint(1, 100) 
guess = None
while guess != num: 
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == num:
        print("Congratulations! You guessed the number.") 
    elif guess < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.") 
        