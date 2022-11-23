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
    global cimsor
    cimsor=file.readline().strip()
    for row in file:
        splitted=row.strip().split(";")
        Nevek.append(splitted[0])
        Fizika_jegy.append(float(splitted[1]))
        Matek_jegy.append(float(splitted[1]))
    file.close()

def printTalulok():
    system("cls")
    print("Tanulók listája:\n")
    for item in Nevek:
        print(f"\t{item}")
    input("Tovább...")