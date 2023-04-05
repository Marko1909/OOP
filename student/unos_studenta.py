from ispiti import get_ispit
def unos_studenta(ispiti, redni_broj):
    student = {}
    student["Ime"] = input(f"Unesite ime {redni_broj}. studenta: ")
    student["Prezime"] = input(f"Unesite prezime {redni_broj}. studenta: ")

    print("Popis ispita: ")
    for i, ispit in enumerate(ispiti, start=1):
        print(get_ispit(i, ispit))

    odabrani_ispit = int(input("Unesite kolegij: "))
    student["Ispit"] = ispiti[odabrani_ispit - 1]

    return student