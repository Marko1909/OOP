from ispiti import get_ispit
from utilities import unos_intervala
from redovni_student import RedovniStudent
from vanredni_student import VanredniStudent


def unos_studenta(ispiti, redni_broj):

    print('Odaberite tip studenta: ')
    print('\t1. Redovni student ')
    print('\t2. Vanredni student ')
    tip_studenta = int(input('unesite tip studenta: '))

    ime = input(f"Unesite ime {redni_broj}. studenta: ").capitalize()
    prezime = input(f"Unesite prezime {redni_broj}. studenta: ").capitalize()

    print("Popis ispita: ")
    for i, ispit in enumerate(ispiti, start=1):
        print(get_ispit(i, ispit))

    odabrani_ispit = unos_intervala(1,i)
    ispit = ispiti[odabrani_ispit - 1]

    if tip_studenta == 1:
        broj_prijava = input('Unesite broj prijava: ')

        return RedovniStudent(ime, prezime, ispit, broj_prijava)

    elif tip_studenta == 2:
        return VanredniStudent(ime, prezime,ispit)
