# Pim Droge, Christiaan Manenschijn & Maarten Tollenaar
#
# Dit is het main bestand van een programma een doolhof wordt gegenereed
# waarin vervolgens AI kunnen gaan racen
# Het programma is gemaakt en getest in PyCharm, Canopy en de Unix standaard
# text editor en iPython terminal, met Python versie 2.7. Verder is er gebruik
# gemaakt van NumPy v.1.11.0 en MatPlotLib v.1.5.1
# Voor het laatst bewerkt op 1/12/2017

import AI
import Mazegen as mg
import Painter
import sys
import numpy as np

def welke(maze, begin, eind):
    AIs=[AI.Maarten1]
    print("Welke AI wil je runnen?")
    return AIs[check(1, 1)-1](maze, begin, eind)



def check(laag, hoog, dtype=int, wisselv=False, wdtype=float):
    """Hiermee wordt gechekt of iets het juiste datatype is, of het de
    juiste range heeft, en wordt mogelijk het datatype aangepast"""
    keuzecheck = False
    while not keuzecheck:  # Met dit loopje wordt ervoor gezorgd
        # dat er een keuze wordt gemaakt
        keuze = input()
        if wisselv:  # Hier wordt gekeken of het gewenst is om het
            # dtype aan te passen en wordt het vervolgens meteen aangepast
            keuze = wdtype(keuze)
        keuzecheck = True
        try:  # Hiermee wordt gekeken of de keuze het dtype is dat het moet
            # zijn
            keuze = dtype(keuze)
            if hoog != False:  # Hiermee wordt gekeken of de keuze wel binnen
                #  het gekozen domein valt
                if keuze > hoog:
                    keuzecheck = False
                    print("Geen geldige invoer, voer een integer tussen",
                        laag, "en", hoog, "in.")
            if laag != False:
                if keuze < laag:
                    keuzecheck = False
                    print("Geen geldige invoer, voer een integer tussen",\
                        laag, "en", hoog, "in.")
        except ValueError:
                keuzecheck = False
                print("Geen geldige invoer, voer een integer tussen", laag,\
                    "en", hoog, "in.")
    return keuze

def stop():
    return True

def menu():
    """Het main menu"""
    mazegen = np.array(mg.mazegen(20, 20))
    maze = mazegen[0]

    begin = [mazegen[1], mazegen[3]]
    eind = [mazegen[2], mazegen[3]]


    menuopties = [stop, Painter.once, Painter.gif, welke]
    # Een list met fucties die in het menu gebruikt kunnen worden
    gestopt = False
    path = []
    while not gestopt:  # Dit zorgt er voor dat dit runt todat het
        # programma wordt gestopt
        print("1.Stop 2.Paint 3.Gif 4.Run")
        keuze = check(1, 5)
        if keuze == 2:
            menuopties[1](maze)
        elif keuze == 3:
            menuopties[2](maze, path)
        elif keuze == 4:
            path = menuopties[3](maze, begin, eind)
        elif keuze == 5:
            mazegen = np.array(mg.mazegen(20, 20))
            maze = mazegen[0]
            begin = [mazegen[1], mazegen[3]]
            eind = [mazegen[2], mazegen[3]]
        elif keuze == 1:
            gestopt = menuopties[0]()  # Dit runt de gekozen functie en
        # geeft het door als het programma gestopt wordt
    sys.exit()

menu()