#import random number
import random
def guess_number(lower_limit, upper_limit):
    random_number = random.randint (lower_limit, upper_limit)
    attempts = 0

    while True:
        guess= int(input('Deviner le nombre etre {} et {}:'.format(lower_limit, upper_limit)))
        attempts += 1

        if guess < random_number:
            print("Too low! Try again.")
            lower_limit = guess + 1
        elif guess > random_number:
            print("Too high! Try again.")
            upper_limit = guess - 1
        else:
            print("Bravo! Vous avez deviné le nombre {} correctement lors de {} essai".format
                (random_number, attempts))
            break
#
    play_again = input("Voulez-vous rejouer? (oui/non): ").lower()
    if play_again=="oui":
        return True
    return False

while True:
    lower_limit = int(input("Enter the lower limit of the range: "))
    upper_limit = int(input("Enter the upper limit of the range: "))

    play_again = guess_number (lower_limit, upper_limit)
    if not play_again:
        break
