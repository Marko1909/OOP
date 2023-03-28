from datetime import date

kolegiji = []

broj_kolegija = int(input("Unesite broj kolegija: "))

for i in range(1, broj_kolegija+1):
    kolegij = {}
    kolegij["Ime"] = input(f'Unesite naziv {i}. kolegija: ')
    kolegij["ECTS"] = int(input(f'Unesite ECTS bodove za {i}. kolegij: '))
    kolegiji.append(kolegij)

"""
print("Popis svih kolegija: ")
for kolegij in kolegiji:
    print(f'\tKolegij {kolegij["Ime"]} nosi {kolegij["ECTS"]} ECTS bodova')
"""

ispiti = []

broj_ispita = int(input("Unesite broj ispita: "))

for i in range(1, broj_ispita+1):
    ispit = {}
    print("Popis kolegija: ")
    for j, kolegij in enumerate(kolegiji, start=1):
        print(f'\t{j}. {kolegij["Ime"]}')

    odabrani_kolegij = int(input("Unesite kolegij: "))
    dan = int(input("Unesite dan ispita: "))
    mjesec = int(input("Unesite mjesec ispita: "))
    godina = int(input("Unesite godinu ispita: "))
    ispit["Datum"] = date(godina, mjesec, dan)
    ispit["Kolegij"] = kolegiji[odabrani_kolegij-1]
    ispiti.append(ispit)

"""
print("Popis svih ispita: ")
for ispit in ispiti:
    print(f'\t Ispit iz kolegija {ispit["Kolegij"]["Ime"]}, koji nosi {ispit["Kolegij"]["ECTS"]} ECTS bodova, održati \
će se {ispit["Datum"]}')
"""

studenti = []

broj_studenata = int(input("Unesite broj studenata: "))

for i in range(1, broj_studenata+1):
    student = {}
    student["Ime"] = input(f"Unesite ime {i}. studenta: ")
    student["Prezime"] = input(f"Unesite prezime {i}. studenta: ")

    print("Popis ispita: ")
    for j, ispit in enumerate(ispiti, start=1):
        print(f'{j}. Ispit iz kolegija {ispit["Kolegij"]["Ime"]} ')

    odabrani_ispit = int(input("Unesite kolegij:"))
    student["Ispit"] = ispiti[odabrani_ispit-1]
    studenti.append(student)

print("Popis svih studenata: ")
for student in studenti:
     print(f'\tStudent {student["Ime"]} {student["Prezime"]} je prijavio: ')
     print(f'\t\tIspit iz kolegija {student["Ispit"]["Kolegij"]["Ime"]} koji će se održati {student["Ispit"]["Datum"]}')
