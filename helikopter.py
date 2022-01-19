#!/usr/bin/env python3


from time import sleep
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

num = 2
boolean = num % 2 == 0
try:
    while True:
        clear()

        if num % 2 == 0:
            print("COMI:ATUA:MAE:")
        else:
            print("         :MAE:ATUA:COMI")

        print("           A")
        if num % 2 == 0:
            print("  L    /--------")

        else:
            print("       /--------")

        print(" NOOB==== DRIP []\\")
        if not num % 2 == 0:
            print("  L    \\         \\")
        else:
            print("       \\         \\")

        print("        \\---------]")
        print("           I     I")
        print("        -----------/")

        num += 1

        sleep(0.3)





except:
    pass
