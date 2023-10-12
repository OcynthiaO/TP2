#import random number
import random
def guess_number(lower_limit, upper_limit):
    random_number = random.randint (lower_limit, upper_limit)
    attempts=0

while True:
    guess= int(input('Guess the number'.format(lower_limit, upper_limit)))
    attempts += 1

    if guess <random_number:
        print("Too low! Try again.")
        lower_limit = guess + 1
    elif guess > random_number:
        print("Too high! Try again.")
        upper_limit = guess - 1
    else:
        print("Congratulations! You guessed the number () correctly in () attempts.".format
              (random_number, attempts))
        break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again "yes":
        return True
    return false

while True:
    lower_limit = int(input("Enter the lower limit of the range: "))
    upper_limit = int(input("Enter the upper limit of the range: "))

    play again guess_number (lower_limit, upper limit)
    if not play again:
        break
