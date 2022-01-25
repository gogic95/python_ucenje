import random

izbor = ["papir", "kamen", "makaze"]


def rules(player1, result1, player2, result2):
    # if player1 == player2:
    #     return

    if player1 == "papir":
        if player2 == "makaze":
            result2 += 1
        if player2 == "kamen":
            result1 += 1

    if player1 == "kamen":
        if player2 == "makaze":
            result1 += 1
        if player2 == "papir":
            result2 += 1

    if player1 == "makaze":
        if player2 == "papir":
            result1 += 1
        if player2 == "kamen":
            result2 += 1

    return result1, result2


rezultat1 = rezultat2 = 0
while rezultat1 < 3 and rezultat2 < 3:
    computer = random.choice(izbor)
    while True:
        player = input("Izaberite papir, kamen ili makaze: ").lower()
        if player in izbor:
            break
        else:
            print("Neispravan format, pokusajte ponovo")

    print("Igrac: " + player.capitalize())
    print("Kompjuter: " + computer.capitalize())
    rezultat1, rezultat2 = rules(player, rezultat1, computer, rezultat2)
    print("Trenutni rezultat {}:{}".format(rezultat1, rezultat2))
    print("######################################\n")

print("Kraj! Konacan rezultat - {}:{}".format(rezultat1, rezultat2))
if rezultat1 > rezultat2:
    print("Pobednik je prvi igrac!")
else:
    print("Pobednik je drugi igrac!")
