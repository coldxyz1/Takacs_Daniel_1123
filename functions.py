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
    print("3 - Osztály átlaga matekból")
    print("4 - Tanuló törlése a listából")
    print("5 - Tanuló hozzáadása a listábhoz")
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

def jegyekTorlese():
    system("cls")
    print("----Tanuló törlése----")
    tanulokkiir()
    sSz=int(input("Kit töröljünk? Adja meg a sorszámát: "))
    Nevek.pop(sSz-1)
    Matek_jegy.pop(sSz-1)
    Fizika_jegy.pop(sSz-1)
    mentesFajlba()
    input("Törlés sikeres!...")

def tanulokkiir():
    system("cls")
    print("Tanulók listája:\n")
    for item in range(len(Nevek)):
        print(f"\t {item+1}. {Nevek[item]}")
    


def mentesFajlba():
    file=open(filename,"w",encoding="utf-8")
    for i in range(len(Nevek)):
        file.write(f"\n{Nevek[i]};{Fizika_jegy[i]};{Matek_jegy[i]}")
        if i<len(Nevek-1):
            file.write("\n")
    file.close()

def fizikaAtlag(Fizika_jegy):
    return sum(Fizika_jegy) / len(Fizika_jegy)

def matekAtlag(Matek_jegy):
    return sum(Matek_jegy) / len(Matek_jegy)
