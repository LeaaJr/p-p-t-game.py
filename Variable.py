from random import randint    

choise = ["Piedra","Papel","Tijera"]

computer = choise [randint(0,2)]
def main():
    print("Bienvenido al juego\n")

    player = input ("Que eliges:").lower()

    print( "computadora eligio: " + computer)

    if player == computer:
        print("dibujar")
    elif player == "Piedra" and computer == " Papel":
        print("computadora gana")
    elif player == "Piedra" and computer == " Tijera":
        print("Player gana")
    elif player == "Papel" and computer == " Piedra":
        print("player gana")
    elif player == "Papel" and computer == " Tijera":
        print("computadora gana")
    elif player == "Tijera" and computer == " Papel":
        print("Player gana")
    elif player == "Tijera" and computer == " Piedra":
        print("computadora gana")


main()