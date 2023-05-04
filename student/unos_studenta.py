from ispiti import get_ispit
from utilities import unos_intervala
from .student import Student

def unos_studenta(ispiti, redni_broj):
    ime = input(f"Unesite ime {redni_broj}. studenta: ").capitalize()
    prezime = input(f"Unesite prezime {redni_broj}. studenta: ").capitalize()

    print("Popis ispita: ")
    for i, ispit in enumerate(ispiti, start=1):
        print(get_ispit(i, ispit))

    odabrani_ispit = unos_intervala(1,i)
    ispit = ispiti[odabrani_ispit - 1]

    return Student(ime, prezime, ispit)