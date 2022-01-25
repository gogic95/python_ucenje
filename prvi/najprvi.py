# ime = "Filip Gogic"
#
# print(ime[::-2])
#
# google1 = "www.google.com"
# facebook2 = "www.facebook.com"
# instagram3 = "www.instagram.com"
#
# kriska = slice(4, -4)
#
# print(google1[kriska], facebook2[kriska], instagram3[kriska])
#
# age = 36
# if age > 20 or age <= 35:
#     print("dobro je")
########################################### PETLJE ###################################################
# i = 1
# while i <= 3:
#     print("Petljaa " + str(i))
#     i += 1
#
# while 1:
#     naziv = input("Upisi naziv: ")
#     if naziv:
#         break
#
# print("Naziv je: " + naziv)
#
# godine = None
#
# while not godine:
#     godine = input("Upisite godine: ")
#
# for i in range(2, 9):
#     print(i)
#     i = i - 2
#     print("Drugi",i)
#
# ime = "Filip"
# i: str
# for i in ime:
#     print(i)
########################################### VREME, TIME, SLEEP ####################################################
# import time
#
# for i in range(10, -1, -1):
#     time.sleep(1)
#     print(i)
#     if i == 5:
#         print("POLA")
#     if i == 0:
#         print("KRAJ!!!")
#
# k = 1
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(k, end=" | ")
#         k += 1
#     print()
######################################## UGNEZDENE PETLJE #######################################################
# kolone = input("Koliko kolona: ")
# redovi = input("Koliko redova: ")
# znak = input("Znak koji zelite: ")
#
# for i in range(0, int(redovi)):
#     for j in range(0, int(kolone)):
#         print(znak, end="")
#     print()
#
# print()
# print()
#
# for i in range(0, int(redovi)):
#     print(znak * int(kolone))
#

# for i in range(1, 21):
#     if (i == 13):
#         continue
#     print(i)
#
# print()
# print()
#
# for i in range(1, 21):
#     if (i == 13):
#         pass
#     else:
#         print(i)
#
#
########################################### LISTE ####################################################
# hrana = ["jaja i jogurt", -0.58934, "virsle", 3, "sok"]
# print(hrana[2])
#
# hrana[2] = "nema vise"
# print(hrana[2])
#
# print(hrana)
############################################## TUPLES (UREDJENE N-TORKE) ######################################
# student = ("1055/2016", "Filip", 8.03)
#
# print(student[1])
#
################################################## SETS (SKUPOVI) ############################################
# skup = {"brojevi", "slova", "znakovi"}
# print(skup)
#
# for i in skup:
#     print(i)
############################################### DICTIONARY (HASHMAP) ###############################################
# hashmap = {1: "Prvi", 2: "Drugi", "Tri": "Treci"}
#
# print(hashmap["Tri"])
# print(hashmap.get(5))
# print(hashmap)
# print(hashmap.items())
# print()
# for k, v in hashmap.items():
#     print(k, v)

# ############################### FUNCTIONS (FUNKCIJE) ##########################################
# def prvaFunkcija(broj1, broj2, ime):
#     print("Zbir brojeva je: ", broj1 + broj2)
#     print("Ime je: " + ime)
#     return broj1 + broj2
#
#
# br1 = int(input("Prvi broj: "))
# br2 = int(input("Drugi broj: "))
# name = "Filip"
#
# zbir = prvaFunkcija(br1, br2, name)
# print("Nakon funkcije zbir je: ", zbir)
#
# def varirajuci_argumenti(*args):
#     args = list(args)
#     suma = 0
#     for i in args:
#         suma += i
#     print(suma)
#
#
# varirajuci_argumenti(1, 2, 3, 4, 3.14)
# varirajuci_argumenti()
#
####################################### EXCEPTIONS (IZUZECI) ############################################
#
# try:
#     print(6 / 0)
# except ZeroDivisionError as e:
#     print(e)
#     print("Ne mozes deliti sa nulom!\n"+str(e))
#
# print("aaaa")
#
####################################### RAD SA FAJLOVIMA (FILES) ############################################

# import os
#
# path = "C:\\Users\\Gogic\\Desktop\\raspored.txt"

# if os.path.exists(path):
#     print(True)
#     if os.path.isfile(path):
#         print("jeste file")
#
# else:
#     print("Nema")

# with open(path) as file:
#     print(file.read())
#     print(file.closed)
#
# print(file.closed)
#
# text = input("Upisite text: ")
#
# with open(path, 'w') as file:
#     file.write(text)
#
# os.remove(path)

# help("graphlib")

from student import Student

prvi_student = Student("Filip", "Gogic", "1055/2016", 8.03)
drugi_student = Student("Test", "Testovski", "11/333", 6.43)

print(prvi_student.ime, prvi_student.prezime, prvi_student.indeks, prvi_student.prosek)
print(drugi_student.ime, drugi_student.prezime, drugi_student.indeks, drugi_student.prosek)

print("-------------------------")
prvi_student.uci()
drugi_student.partija()

prvi_student.prosek += 1
print(prvi_student.ime, prvi_student.prezime, prvi_student.indeks, prvi_student.prosek)
print(prvi_student.noge)