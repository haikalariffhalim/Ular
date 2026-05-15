import random

# print("Welcome to Guess the Number!")
# print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1, 50)

isCorrect = False

while isCorrect != True:
    guess = int(input("Guess a number between 1 and 50: "))

    if guess == number:
        print(f"You guessed {guess}. That is correct!")
        isCorrect = True
    # another option to use break
    else:
        print(f"You guessed {guess}. Sorry that isn't corrent.")
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")
