lijst = []
fouten = []

def teken_galg(fouten):

    if fouten == 1:
        print(" _________")
        print("|/        |")
        print("|         O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif fouten == 2:
        print(" _________")
        print("|/        |")
        print("|         O")
        print("|         |")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif fouten == 3:
        print(" _________")
        print("|/        |")
        print("|         O")
        print("|         |/")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif fouten == 4:
        print(" _________")
        print("|/        |")
        print("|         O")
        print("|        \|/")
        print("|           ")
        print("|")
        print("|")
        print("|___")
    elif fouten == 5:
        print(" _________")
        print("|/        |")
        print("|         O")
        print("|        \|/")
        print("|         |")
        print("|")
        print("|")
        print("|___")
    elif fouten == 6:
        print(" _________")
        print("|/        |")
        print("|         O")
        print("|        \|/")
        print("|         |")
        print("|       ._/\_.")
        print("|")
        print("|___")

    elif fouten == 0:
        print(" _________")
        print("|/        ")
        print("|         ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|___")


def welkom():
    print(" _    _  ____  __    _  _  _____  __  __    ____  ____   ____     ___    __    __    ___   ____  ____  ")
    print("( \/\/ )( ___)(  )  ( )/ )(  _  )(  \/  )  (  _ \(_  _) (_  _)   / __)  /__\  (  )  / __) (_  _)( ___)")
    print(" )    (  )__)  )(__  )  (  )(_)(  )    (    ) _ < _)(_ .-_)(    ( (_-. /(__)\  )(__( (_-..-_)(   )__)")
    print("(__/\__)(____)(____)(_)\_)(_____)(_/\/\_)  (____/(____)\____)    \___/(__)(__)(____)\___/\____) (____)")
    print("")


def spel():
    woorden = ["galgje", "banaan", "metis", "mahoniehoutenpennenmesjesfabrikantenverenigingsgebouwtjes", "oortjes", "coderclass", "apple", "autoventieldopje", "kaas", "vliegtuig", "toetsenbord"]

    import random
    woord = random.choice(woorden)
    #print(woord)

    letter = input("Kies een letter of kies een '?' om het geheime woord te raden: ")
    fouten = 0

    while letter != woord:
        if letter not in woord:
            fouten += 1
            print("Jouw letter ", "-", " zit er niet in!")
        else:
            print("jouw letter ", letter, " zit erin!")
            lijst.append(letter)
        print(fouten)
        teken_galg(fouten)

        if fouten == 6:
            print("Het woord was ", woord)
            print("Je hebt verloren!")
            return

        print(lijst)
        print(fouten)
        letter = input("Kies een letter of kies een '?' om het geheime woord te raden: ") #Er moet ergens een nieuwe input komen

    print("Je hebt gewonnen")



def main():
    welkom()
    spel()
    vraag = input("Wil je nog een keer spelen? ")
    while vraag != 'nee':
        spel()
        vraag = input("Wil je nog een keer spelen? ")


main()
