from datetime import date
from kolegij import get_kolegij

def unos_ispita(kolegiji, redni_broj):
    ispit = {}

    print("Popis kolegija: ")
    for i, kolegij in enumerate(kolegiji, start=1):
        print(get_kolegij(i, kolegij))

    odabrani_kolegij = int(input("Unesite kolegij: "))

    ispit["Kolegij"] = kolegiji[odabrani_kolegij - 1]

    dan = int(input("Unesite dan ispita: "))
    mjesec = int(input("Unesite mjesec ispita: "))
    godina = int(input("Unesite godinu ispita: "))

    ispit["Datum"] = date(godina, mjesec, dan)

    return ispit
