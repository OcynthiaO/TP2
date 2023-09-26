#import random number
import random
n = random.randint(1, 100)

#Regles du jeu
print("C'est un jeu de devinettes, les regles sont：\n"
      "1.un nombre entier de 1 à 100\n"
      "2.Si le nombre deviné est trop grand,s'affichera:Trop grand!\n"
      "3.Si le nombre deviné est trop petit,s'affichera:Trop petit!\n"
      "4.Si vous devinez correctement, s'affichera:Bravo!\n")

#Le fonction donne un random nombre, on doit deviner, input int
while True:
    nombre = int(input("Entrez un nombre："))
    if nombre > n:
        print("Trop grand!")
    elif nombre < n:
        print("Trop petit!")
    else:
        print("Bravo!")
        break