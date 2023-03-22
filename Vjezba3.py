kolegiji = []

broj_kolegija = int(input("Unesite broj kolegija: "))

for index, i in enumerate(range(broj_kolegija), start=1):
    kolegiji.append(dict(Kolegij=input("Unesite naziv kolegija: ")))
    kolegiji[i]["ECTS"] = input(f'Unesite ECTS bodove za {index}. kolegij: ')

print("Popis svih kolegija: ")
print(f'\t Kolegij {kolegiji[0]["Kolegij"]} nosi {kolegiji[0]["ECTS"]} ECTS bodova ')
print(f'\t Kolegij {kolegiji[1]["Kolegij"]} nosi {kolegiji[1]["ECTS"]} ECTS bodova ')
print(f'\t Kolegij {kolegiji[2]["Kolegij"]} nosi {kolegiji[2]["ECTS"]} ECTS bodova ')


