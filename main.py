#import random number
import random
def guess_number(borne_minimale, borne_maximale):
    random_number = random.randint (borne_minimale, borne_maximale)
    attempts = 0

    while True:
        guess= int(input('Deviner un nombre etre {} et {}:'.format(borne_minimale, borne_maximale)))
        attempts += 1

        if guess < random_number:
            print("Too low! Try again.")
            borne_minimale = guess + 1
        elif guess > random_number:
            print("Too high! Try again.")
            borne_maximale = guess - 1
        else:
            print("Bravo! Vous avez deviné le nombre {} correctement lors de {} essai(s)".format
                (random_number, attempts))
            break
#
    play_again = input("Voulez-vous faire une autre partie? (oui/non): ").lower()
    if play_again=="oui":
        return True
    return False

while True:
    borne_minimale = int(input("Enter la borne minimale que vous voulez: "))
    borne_maximale = int(input("Enter la borne maximale of vous voulez: "))

    play_again = guess_number(borne_minimale, borne_maximale)
    if not play_again:
        print('Merci et au revoir...')
        break
