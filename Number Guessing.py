import random

secret_number = random.randint(0, 7)
guess = int
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_number and not out_of_guesses:
    if guess_count < guess_limit:
        print()
        guess = int(input("Guess the number and you'll be free or you'll be punished\nThe number is between 0-7\nYou have 3 chances to guess the number : "))
        if guess == secret_number:
            break
        else:
            guess_count += 1

    if guess_count < guess_limit:
        guess = int(input("Nope, Try Again : "))
        if guess == secret_number:
            break
        else:
            guess_count += 1

    if guess_count < guess_limit:
        guess = int(input("This is your last chance : "))
        if guess == secret_number:
            break
        else:
            guess_count += 1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Lose! " + "Correct answer: " + str(secret_number) + "")
else:
    print("Congratulations, You Win")
