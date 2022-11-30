from data import Nevek,Matek_jegy,Fizika_jegy
from os import system

filename="osztalyzatok.csv"
cimsor=""

def menu():
    system("cls")
    print("-----MENÜ-----")
    print("0 - Kilépés")
    print("1 - Tanulók listája(jegyekkel)")
    print("2 - Osztály átlaga fizikából")
    print("2 - Osztály átlaga matekból")
    print("3 - Tanuló törlése a listából")
    print("4 - Tanuló hozzáadása a listábhoz")
    return input("Kérem válasszon egy menüpontot:...")

def load_osztalyzatok():
    file=open(filename,"r",encoding="utf-8")
    file.readline()
    for egysor in file:
        darabolt=egysor.strip().split(";")
        Nevek.append(darabolt[0])
        Fizika_jegy.append(int(darabolt[1]))
        Matek_jegy.append(int(darabolt[2]))
    file.close()

def printTalulok():
    system("cls")
    print("Tanulók listája:\n")
    for item in range(len(Nevek)):
        print(f"\tTanuló neve:{Nevek[item]} \nMatek jegye:{Matek_jegy[item]}\nFizika jegye:{Fizika_jegy[item]}")
    input("\nTovább...")

"""def tanulo_torlese():
    system("cls")
    print("Tanuló törlése:..")
    Nev=input("Törlendő tanuló neve a listából: ")
    pass"""

def tanulo_hozzaadasa():
    system("cls")
    print("Új tanuló hozzáadása:\n")
    uj_tanulo=input("Uj tanuló neve:...")
    uj_matek=int(input("Matek jegye:.."))
    uj_fizika=int(input("Fizika jegye:.."))
    Nevek.append(uj_tanulo)
    Fizika_jegy.append(uj_fizika)
    Matek_jegy.append(uj_matek)
    TanuloMenteseFajlba(uj_tanulo,uj_matek,uj_fizika)
    input("Tanuló sikeresen hozzáadva...")

def TanuloMenteseFajlba(tanulo,matek,fizika):
    file=open(filename,"a",encoding="utf-8")
    file.write(f"\n{tanulo};{fizika};{matek}")
    file.close