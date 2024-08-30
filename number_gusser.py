import random

top_or_range = input("Enter a Number: ")

if top_or_range.isdigit():
    top_or_range = int(top_or_range)

    if top_or_range <= 0:
        print("Oops!!! Enter a number greater then 0 next time...")
        quit()
else:
    print("Please typ a number  next time!")
    quit()

random_number = random.randint(0, top_or_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time...")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print('You are above the number!')
    else:
        print('you are below the number!')

print("You got it in", guesses, "guesses")