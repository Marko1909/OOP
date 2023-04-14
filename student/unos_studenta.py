from ispiti import get_ispit
from utilities import unos_intervala

def unos_studenta(ispiti, redni_broj):
    student = {}
    student["Ime"] = input(f"Unesite ime {redni_broj}. studenta: ")
    student["Prezime"] = input(f"Unesite prezime {redni_broj}. studenta: ")

    print("Popis ispita: ")
    for i, ispit in enumerate(ispiti, start=1):
        print(get_ispit(i, ispit))

    odabrani_ispit = unos_intervala(1,i)
    student["Ispit"] = ispiti[odabrani_ispit - 1]

    return student