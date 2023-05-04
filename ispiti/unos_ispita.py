from datetime import date
from kolegij import get_kolegij
from utilities import unos_intervala
from.ispit import Ispit

def unos_ispita(kolegiji, redni_broj):
    print("Popis kolegija: ")
    for i, kolegij in enumerate(kolegiji, start=1):
        print(get_kolegij(i, kolegij))

    odabrani_kolegij = unos_intervala(1,i)

    kolegij = kolegiji[odabrani_kolegij - 1]

    dan = int(input("Unesite dan ispita: "))
    mjesec = int(input("Unesite mjesec ispita: "))
    godina = int(input("Unesite godinu ispita: "))

    datum = date(godina, mjesec, dan)

    return Ispit(kolegij, datum)
