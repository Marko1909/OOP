from datetime import date

kolegiji = []

broj_kolegija = int(input("Unesite broj kolegija: "))

for index, i in enumerate(range(broj_kolegija), start=1):
    kolegiji.append(dict(Kolegij=input("Unesite naziv kolegija: ")))
    kolegiji[i]["ECTS"] = input(f'Unesite ECTS bodove za {index}. kolegij: ')


ispiti = []

broj_ispita = int(input("Unesite broj ispita: "))

for i in range(broj_ispita):
    for index, j in enumerate(range(broj_kolegija), start=1):
        print(f'{index}. {kolegiji[j]["Kolegij"]}')

    ispiti.append(dict(Kolegij=kolegiji[int(input("Unesite kolegij: "))-1]["Kolegij"]))
    dan = int(input("Unesite dan ispita: "))
    mjesec = int(input("Unesite mjesec ispita: "))
    godina = int(input("Unesite godinu ispita: "))
    ispiti[i]["Datum"] = date(godina, mjesec, dan)


print("Popis svih ispita: ")
for i in range(broj_ispita):
    print(f'\t Ispit iz kolegija {ispiti[i]["Kolegij"]}, koji nosi {kolegiji[i]["ECTS"]} ECTS bodova održati\
će se {ispiti[i]["Datum"]}')

