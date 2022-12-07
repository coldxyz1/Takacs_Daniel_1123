from functions import *


load_osztalyzatok()
choice=""

while choice!="0":
    choice=menu()
    if choice=="1":
        printTalulok()
    elif choice=="2":
       print(f"Az tanulók fizika átlaga: {round(fizikaAtlag(Fizika_jegy),2)}")
       input("Tovább...")
    elif choice=="3":
        print(f"Az tanulók fizika átlaga: {round(matekAtlag(Matek_jegy),2)}")
        input("Tovább...")
    elif choice=="4":
        jegyekTorlese()
    elif choice=="5":
        tanulo_hozzaadasa()